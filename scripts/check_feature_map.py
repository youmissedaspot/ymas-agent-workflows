"""Read-only Feature Map validation, scoped raw-byte freshness and typed graph export.

Commands and acceptance claims are data, never executed or authenticated here.
No network, regeneration, repair, or integration action is performed.
"""

import argparse
import hashlib
import json
from pathlib import Path, PurePosixPath
import re

from jsonschema import Draft202012Validator


SCHEMA = Path(__file__).resolve().parents[1] / "skills/spec-driven-development/assets/feature_map.schema.json"
GROUPS = {"sources": "source", "features": "feature", "scenarios": "scenario", "tools": "tool"}
EDGE_TYPES = {
    "contains": ("feature", "feature"), "depends_on": ("feature", "feature"),
    "governed_by": ("feature", "source"), "implemented_by": ("feature", "source"),
    "verified_by": ("feature", "scenario"), "uses_tool": ("scenario", "tool"),
}
PLANNING = re.compile(r"^(roadmap|release|milestone|phase|sprint|campaign)\d*$")
DEVICE = re.compile(r"^(con|prn|aux|nul|com[1-9]|lpt[1-9])(?:\.|$)", re.I)


def finding(code, location, message, correction):
    return {"code": code, "location": location, "message": message, "correction": correction}


def path_problem(name):
    parts = name.split("/")
    if ("\\" in name or ":" in name or any(ord(char) < 32 or ord(char) == 127 for char in name)
            or PurePosixPath(name).is_absolute()
            or any(part in {"", ".", ".."} or part.casefold() == ".git" or part.endswith((".", " "))
                   or DEVICE.match(part) for part in parts)):
        return "source path must be a normalized repository-relative file path"
    return None


def load_json(path):
    def pairs(items):
        result = {}
        for key, value in items:
            if key in result:
                raise ValueError(f"duplicate JSON key: {key}")
            result[key] = value
        return result
    return json.loads(Path(path).read_text(encoding="utf-8-sig"), object_pairs_hook=pairs)


def validate_map(document, schema=None):
    schema = load_json(SCHEMA) if schema is None else schema
    Draft202012Validator.check_schema(schema)
    errors = [finding("schema", "/" + "/".join(map(str, error.absolute_path)),
                      error.message, "Correct the entry against the local Feature Map schema.")
              for error in Draft202012Validator(schema).iter_errors(document)]
    if errors:
        return sorted(errors, key=lambda row: (row["location"], row["message"]))

    nodes = {}
    for group, kind in GROUPS.items():
        for index, row in enumerate(document[group]):
            node_id = row["id"]
            location = f"/{group}/{index}"
            if node_id in nodes:
                errors.append(finding("duplicate_id", location, f"duplicate ID: {node_id}",
                                      "Retain distinct durable identities; fix only this collision."))
            nodes[node_id] = (kind, row)
    for node_id in [document["map_id"], *nodes]:
        if any(PLANNING.fullmatch(part) for part in re.split(r"[.-]", node_id)):
            errors.append(finding("planning_id", node_id, "planning label in durable ID",
                                  "Use enduring domain terminology, preserving existing historical records."))

    def require(node_id, kinds, location):
        found = nodes.get(node_id)
        if not found or found[0] not in kinds:
            errors.append(finding("reference", location, f"missing or wrong node type: {node_id}",
                                  "Declare the intended node or correct the typed reference."))
            return None
        return found[1]

    for source in document["sources"]:
        problem = path_problem(source["path"])
        if problem:
            errors.append(finding("unsafe_path", source["id"], problem,
                                  "Reference only an authorized file inside the explicit repository root."))
        if source["status"] == "accepted" and (
                source["kind"] not in {"requirement", "architecture"} or not source["acceptance"].strip()):
            errors.append(finding("authority", source["id"], "accepted source lacks governing role or acceptance provenance",
                                  "Keep implementation observed; record actual project acceptance for requirements."))
    for feature in document["features"]:
        for entry in feature["entrypoints"]:
            source = require(entry["source"], {"source"}, feature["id"])
            if source and source["kind"] not in {"implementation", "tool"}:
                errors.append(finding("entrypoint", feature["id"], "entrypoint must reference an implementation or tool surface",
                                      "Inspect actual user/system reachability and reference its source."))
    for tool in document["tools"]:
        source = require(tool["source"], {"source"}, tool["id"])
        if source and source["kind"] != "tool":
            errors.append(finding("tool_source", tool["id"], "tool descriptor must reference tool source",
                                  "Record the maintained executable source and its limits."))
        if tool["effects"] != "read" and not tool["preview_argv"] and not tool["limits"]:
            errors.append(finding("preview", tool["id"], "mutating tool has neither preview nor an explained limit",
                                  "Describe a safe preview where practical, or why it is unavailable; preserve approval boundaries."))
    for scenario in document["scenarios"]:
        if scenario["status"] != "ready" and not scenario["limits"]:
            errors.append(finding("scenario_limit", scenario["id"], "blocked/unsupported scenario has no recorded limit",
                                  "Record the blocker or unsupported edge; it is not passing evidence."))
        for expectation in scenario["expectations"]:
            source = require(expectation["source"], {"source"}, scenario["id"])
            if source and (source["kind"] not in {"requirement", "architecture"} or (
                    scenario["status"] == "ready" and source["status"] != "accepted")):
                errors.append(finding("expectation_authority", scenario["id"], "expectation lacks accepted governing source for a ready scenario",
                                      "Resolve authority through its owner or mark the scenario blocked; do not derive expectations from code."))

    seen_edges = set()
    outgoing = {}
    containment = {}
    for index, edge in enumerate(document["relations"]):
        location = f"/relations/{index}"
        signature = (edge["from"], edge["type"], edge["to"])
        if signature in seen_edges:
            errors.append(finding("duplicate_edge", location, "duplicate typed relationship",
                                  "Keep one relationship and combine its supporting provenance."))
        seen_edges.add(signature)
        start_kind, end_kind = EDGE_TYPES[edge["type"]]
        start = require(edge["from"], {start_kind}, location)
        end = require(edge["to"], {end_kind}, location)
        provenance = [require(item, {"source"}, location) for item in edge["provenance"]]
        if edge["basis"] == "specified" and not any(
                source and source["kind"] in {"requirement", "architecture"} and source["status"] == "accepted"
                for source in provenance):
            errors.append(finding("edge_authority", location, "specified edge lacks accepted requirement/architecture provenance",
                                  "Reference the accepted clause, or label this relationship observed/unresolved."))
        if end and edge["type"] in {"governed_by", "implemented_by"}:
            allowed = {"requirement", "architecture"} if edge["type"] == "governed_by" else {"implementation", "tool"}
            if end["kind"] not in allowed:
                errors.append(finding("edge_source_type", location, "relationship targets the wrong source role",
                                      "Keep governing and implementation references distinct."))
        if start and end:
            outgoing.setdefault(edge["from"], set()).add(edge["type"])
            if edge["type"] == "contains":
                containment.setdefault(edge["from"], []).append(edge["to"])

    # Iterative traversal avoids recursion limits for untrusted containment chains.
    indegree = {node_id: 0 for node_id in nodes if nodes[node_id][0] == "feature"}
    for children in containment.values():
        for child in children:
            indegree[child] += 1
    pending = [node_id for node_id, degree in indegree.items() if not degree]
    visited = 0
    while pending:
        parent = pending.pop()
        visited += 1
        for child in containment.get(parent, []):
            indegree[child] -= 1
            if not indegree[child]:
                pending.append(child)
    if visited != len(indegree):
        errors.append(finding("containment_cycle", "/relations", "contains relationships form a cycle",
                              "Correct containment; dependency cycles are a separate architectural question."))
    for feature in document["features"]:
        required = {"governed_by"}
        if feature["status"] == "observed":
            required |= {"implemented_by", "verified_by"}
        missing = required - outgoing.get(feature["id"], set())
        if missing:
            errors.append(finding("feature_coverage", feature["id"], f"missing relationships: {', '.join(sorted(missing))}",
                                  "Trace the feature to authority and verification, or record its actual partial/planned status."))
    for scenario in document["scenarios"]:
        if scenario["status"] == "ready" and "uses_tool" not in outgoing.get(scenario["id"], set()):
            errors.append(finding("scenario_tool", scenario["id"], "ready scenario has no maintained tool",
                                  "Link an existing deterministic tool or mark the verification gap explicitly."))
    return sorted(errors, key=lambda row: (row["location"], row["code"], row["message"]))


def check_freshness(document, root):
    root = Path(root).resolve(strict=True)
    if not root.is_dir():
        raise ValueError("repository root must be an existing directory")
    findings = []
    for source in document["sources"]:
        name = source["path"]
        try:
            problem = path_problem(name)
            if problem:
                raise ValueError(problem)
            path = root
            for part in name.split("/"):
                path = path / part
                if path.is_symlink() or (hasattr(path, "is_junction") and path.is_junction()):
                    raise ValueError("symlink source or parent is unsupported")
            resolved = path.resolve(strict=True)
            if not resolved.is_relative_to(root) or not resolved.is_file():
                raise ValueError("source is outside the repository or is not a regular file")
            with resolved.open("rb") as handle:
                digest = hashlib.file_digest(handle, "sha256").hexdigest()
            if digest != source["sha256"]:
                findings.append(finding("changed_source", source["id"], f"raw bytes changed: {name}",
                                        "Inspect affected entries/relations/tools; update only reconciled hashes and semantic changes."))
        except (OSError, ValueError):
            findings.append(finding("unavailable_source", source["id"], f"missing, inaccessible or unsafe source: {name}",
                                    "Inspect authorized source ownership/path; report the gap without broadening access."))
    return sorted(findings, key=lambda row: (row["location"], row["code"]))


def export_graph(document):
    nodes = [{"id": row["id"], "type": kind, "data": row}
             for group, kind in GROUPS.items() for row in document[group]]
    edges = [{**edge, "provenance": sorted(edge["provenance"])} for edge in document["relations"]]
    return {"schema_version": 1, "kind": "derived-feature-graph", "map_id": document["map_id"],
            "document_version": document["document_version"], "coverage": document["coverage"],
            "nodes": sorted(nodes, key=lambda row: row["id"]),
            "edges": sorted(edges, key=lambda row: (row["from"], row["type"], row["to"]))}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("mode", choices=("validate", "check", "graph"))
    parser.add_argument("map", type=Path)
    parser.add_argument("--repo", type=Path, help="explicit authorized source root; required for check/graph")
    args = parser.parse_args()
    if args.mode != "validate" and args.repo is None:
        parser.error("check/graph require --repo; no repository root is inferred")
    result = {"passed": False, "scope": "declared map inputs only",
              "checks": {"structure": False, "freshness": "not_checked", "semantics": "not_checked"},
              "findings": []}
    try:
        document = load_json(args.map)
        result["findings"] = validate_map(document)
        result["checks"]["structure"] = not result["findings"]
        if not result["findings"] and args.mode != "validate":
            result["findings"] = check_freshness(document, args.repo)
            result["checks"]["freshness"] = not result["findings"]
        result["passed"] = not result["findings"]
        if result["passed"] and args.mode == "graph":
            result["graph"] = export_graph(document)
    except RecursionError:
        result["findings"] = [finding("input_depth", "/", "input nesting exceeds parser capability",
                                      "Use the compact map schema and flatten excessive nesting; do not raise runtime recursion limits.")]
    except (OSError, ValueError):
        # Do not echo OS error paths, which can disclose a resolved outside root.
        result["findings"] = [finding("input", "/", "map/schema/root could not be read or parsed",
                                      "Check local JSON, unique keys, dependency availability and the explicit authorized root.")]
    print(json.dumps(result, indent=2, sort_keys=True))
    raise SystemExit(not result["passed"])


if __name__ == "__main__":
    main()
