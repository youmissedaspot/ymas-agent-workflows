"""Feature Map constraints, scoped freshness and synthetic executable portability.

These checks do not establish application behavior, acceptance, or agent efficacy.
"""

import copy
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch

from check_feature_map import SCHEMA, check_freshness, export_graph, load_json, validate_map


EXAMPLE = SCHEMA.parent / "feature_map_example"
CHECKER = Path(__file__).with_name("check_feature_map.py")


class FeatureMapTest(unittest.TestCase):
    def setUp(self):
        self.document = load_json(EXAMPLE / "feature_map.json")

    def codes(self, document):
        return {row["code"] for row in validate_map(document)}

    def cli(self, *args):
        result = subprocess.run([sys.executable, "-B", str(CHECKER), *map(str, args)],
                                capture_output=True, text=True, timeout=20)
        return result.returncode, json.loads(result.stdout)

    def test_schema_template_and_real_example(self):
        self.assertEqual(validate_map(load_json(SCHEMA.parent / "feature_map_template.json")), [])
        self.assertEqual(validate_map(self.document), [])
        self.assertEqual(check_freshness(self.document, EXAMPLE), [])

    def test_invalid_shapes_schema_version_and_unknown_fields(self):
        for mutation in (None, [], {**self.document, "schema_version": 2},
                         {**self.document, "execute": True}):
            self.assertIn("schema", self.codes(mutation))
        altered = copy.deepcopy(self.document)
        altered["sources"][0]["sha256"] = "unrecorded"
        self.assertIn("schema", self.codes(altered))
        altered = copy.deepcopy(self.document)
        altered["scenarios"][0]["evidence"] = []
        self.assertIn("schema", self.codes(altered))

    def test_duplicate_ids_and_planning_identifiers(self):
        altered = copy.deepcopy(self.document)
        altered["features"].append(copy.deepcopy(altered["features"][0]))
        self.assertIn("duplicate_id", self.codes(altered))
        altered = copy.deepcopy(self.document)
        altered["map_id"] = "release2.records"
        self.assertIn("planning_id", self.codes(altered))

    def test_identifier_version_and_hash_patterns_reject_final_line_terminators(self):
        for value in ("records\n", "release2\n", "records\r", "records\u2028", "records\u2029"):
            altered = copy.deepcopy(self.document)
            altered["map_id"] = value
            self.assertIn("schema", self.codes(altered))
        for group in ("sources", "features", "scenarios", "tools"):
            altered = copy.deepcopy(self.document)
            altered[group][0]["id"] += "\n"
            self.assertIn("schema", self.codes(altered))
        altered = copy.deepcopy(self.document)
        altered["document_version"] += "\n"
        self.assertIn("schema", self.codes(altered))
        altered = copy.deepcopy(self.document)
        altered["sources"][0]["sha256"] += "\n"
        self.assertIn("schema", self.codes(altered))

    def test_dangling_wrong_typed_and_duplicate_edges(self):
        for target in ("unknown.feature", "tool.records-check"):
            altered = copy.deepcopy(self.document)
            altered["relations"][0]["to"] = target
            self.assertIn("reference", self.codes(altered))
        altered = copy.deepcopy(self.document)
        altered["relations"].append(copy.deepcopy(altered["relations"][0]))
        self.assertIn("duplicate_edge", self.codes(altered))
        altered = copy.deepcopy(self.document)
        altered["relations"][1]["to"] = "source.records"
        self.assertIn("edge_source_type", self.codes(altered))

    def test_contains_and_dependency_cycles_have_different_meanings(self):
        edge = {"from": "records.lookup", "type": "contains", "to": "records.storage",
                "basis": "observed", "provenance": ["source.records"]}
        altered = copy.deepcopy(self.document)
        altered["relations"].append(edge)
        self.assertEqual(validate_map(altered), [])
        altered["relations"].append({**edge, "from": "records.storage", "to": "records.lookup"})
        self.assertIn("containment_cycle", self.codes(altered))
        for row in altered["relations"]:
            if row["type"] == "contains":
                row["type"] = "depends_on"
        # Remove the duplicated forward dependency; valid dependency cycles remain data.
        altered["relations"].pop(-2)
        self.assertEqual(validate_map(altered), [])

    def test_authority_cannot_come_from_code_or_unaccepted_requirements(self):
        altered = copy.deepcopy(self.document)
        altered["sources"][0]["status"] = "draft"
        self.assertIn("expectation_authority", self.codes(altered))
        self.assertIn("edge_authority", self.codes(altered))
        altered["scenarios"][0]["status"] = "blocked"
        for edge in altered["relations"]:
            edge["basis"] = "unresolved"
        self.assertEqual(validate_map(altered), [])
        altered = copy.deepcopy(self.document)
        altered["scenarios"][0]["expectations"][0]["source"] = "source.records"
        self.assertIn("expectation_authority", self.codes(altered))
        altered["sources"][1]["status"] = "accepted"
        altered["sources"][1]["acceptance"] = "claimed"
        self.assertIn("authority", self.codes(altered))

    def test_missing_verification_and_mutation_limits(self):
        altered = copy.deepcopy(self.document)
        altered["relations"] = [edge for edge in altered["relations"] if edge["type"] != "uses_tool"]
        self.assertIn("scenario_tool", self.codes(altered))
        altered = copy.deepcopy(self.document)
        altered["tools"][0]["effects"] = "destructive"
        altered["tools"][0]["limits"] = []
        self.assertIn("preview", self.codes(altered))
        altered["tools"][0]["preview_argv"] = ["custom-check", "--preview"]
        self.assertNotIn("preview", self.codes(altered))

    def test_declared_path_traversal_absolute_devices_and_git_are_rejected(self):
        for name in ("../outside", "/outside", "C:/outside", "dir\\file", "dir/../file",
                     "dir//file", "dir/./file", ".git/config", ".GIT/config", "dir/file\n",
                     "NUL", "dir/CON.txt", "dir/.. /file"):
            altered = copy.deepcopy(self.document)
            altered["sources"][0]["path"] = name
            with self.subTest(path=name):
                self.assertIn("unsafe_path", self.codes(altered))

    def test_raw_frontmatter_changes_and_missing_files_are_drift(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory) / "fixture"
            shutil.copytree(EXAMPLE, root)
            self.assertEqual(check_freshness(self.document, root), [])
            path = root / "requirements.md"
            path.write_bytes(b"---\nnote: metadata only\n---\n" + path.read_bytes())
            findings = check_freshness(self.document, root)
            self.assertEqual([row["code"] for row in findings], ["changed_source"])
            self.assertEqual(findings[0]["location"], "source.lookup-contract")
            path.unlink()
            self.assertEqual(check_freshness(self.document, root)[0]["code"], "unavailable_source")

    def test_symlink_or_windows_junction_escape_is_not_read(self):
        with tempfile.TemporaryDirectory() as directory:
            scratch = Path(directory)
            root = scratch / "root"
            outside = scratch / "outside"
            root.mkdir()
            outside.mkdir()
            (outside / "secret.txt").write_text("outside", encoding="utf-8")
            link = root / "alias"
            try:
                link.symlink_to(outside, target_is_directory=True)
            except OSError:
                if os.name != "nt":
                    raise
                subprocess.run(["cmd", "/c", "mklink", "/J", str(link), str(outside)],
                               check=True, capture_output=True, text=True, timeout=10)
            source = {**self.document["sources"][0], "path": "alias/secret.txt"}
            with patch("check_feature_map.hashlib.file_digest") as digest:
                findings = check_freshness({"sources": [source]}, root)
                digest.assert_not_called()
            self.assertEqual(findings[0]["code"], "unavailable_source")

    def test_graph_is_typed_deterministic_and_scoped(self):
        graph = export_graph(self.document)
        reversed_map = copy.deepcopy(self.document)
        for group in ("sources", "features", "scenarios", "tools", "relations"):
            reversed_map[group].reverse()
        self.assertEqual(graph, export_graph(reversed_map))
        self.assertEqual(graph["map_id"], "records")
        self.assertEqual({row["type"] for row in graph["nodes"]}, {"feature", "source", "scenario", "tool"})
        first = self.cli("graph", EXAMPLE / "feature_map.json", "--repo", EXAMPLE)
        self.assertEqual(first, self.cli("graph", EXAMPLE / "feature_map.json", "--repo", EXAMPLE))
        self.assertEqual(first[0], 0)
        self.assertEqual(first[1]["checks"]["semantics"], "not_checked")

    def test_cli_never_executes_commands_and_rejects_stale_graph(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            fixture = root / "fixture"
            shutil.copytree(EXAMPLE, fixture)
            marker = root / "executed.txt"
            altered = copy.deepcopy(self.document)
            altered["tools"][0]["argv"] = [sys.executable, "-c", f"open({str(marker)!r}, 'w').write('executed')"]
            path = fixture / "feature_map.json"
            path.write_text(json.dumps(altered), encoding="utf-8")
            for mode in ("validate", "check", "graph"):
                args = () if mode == "validate" else ("--repo", fixture)
                code, result = self.cli(mode, path, *args)
                self.assertEqual(code, 0)
                self.assertTrue(result["passed"])
                self.assertFalse(marker.exists())
            (fixture / "src/records.py").write_text("changed", encoding="utf-8")
            code, result = self.cli("graph", path, "--repo", fixture)
            self.assertEqual(code, 1)
            self.assertNotIn("graph", result)
            self.assertFalse(marker.exists())

    def test_duplicate_json_keys_and_malformed_cli_input(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "map.json"
            for payload in ('{"kind":1,"kind":2}', "{broken"):
                path.write_text(payload, encoding="utf-8")
                with self.assertRaises(ValueError):
                    load_json(path)
                code, result = self.cli("validate", path)
                self.assertEqual(code, 1)
                self.assertEqual(result["findings"][0]["code"], "input")

    def test_deep_input_returns_an_actionable_json_failure(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "deep.json"
            path.write_text("[" * 10000 + "]" * 10000, encoding="utf-8")
            code, result = self.cli("validate", path)
            self.assertEqual(code, 1)
            self.assertFalse(result["passed"])
            self.assertEqual(result["findings"][0]["code"], "input_depth")
            self.assertIn("flatten", result["findings"][0]["correction"])

    def test_materialized_example_runs_without_package_paths(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory) / "neutral"
            shutil.copytree(EXAMPLE, root)
            self.assertEqual(check_freshness(load_json(root / "feature_map.json"), root), [])
            result = subprocess.run([sys.executable, "-B", "tools/check_records.py"], cwd=root,
                                    capture_output=True, text=True, timeout=10)
            self.assertEqual(result.returncode, 0)
            evidence = json.loads(result.stdout)
            self.assertTrue(evidence["passed"])
            self.assertEqual(evidence["observed"], {"existing": "value", "missing": None, "unchanged": True})
            self.assertEqual(sorted(path.relative_to(root).as_posix() for path in root.rglob("*") if path.is_file()),
                             ["feature_map.json", "requirements.md", "src/records.py", "tools/check_records.py"])


if __name__ == "__main__":
    unittest.main()
