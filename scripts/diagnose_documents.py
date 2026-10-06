"""Read-only YMAS ID/current-path/edition diagnostics; never rename or repair.

Only use with an adopted YMAS naming scheme. Other authorities need their own
adapter. Unversioned legacy documents are warnings, not automatic violations.
"""

import argparse
from collections import defaultdict
import json
from pathlib import Path
import re


FAMILIES = "OPS_WORKFLOW|OPS_SPECDEF|OPS_DECISION|OPS_STATE|OPS_TASK|OPS_NEXT|SPECARC|SPEC|SOT|RM|SYS|PLAN|AUDIT|ADR|BUG|REF"
NAME = re.compile(rf"^(?P<family>{FAMILIES})_(?:[A-Z][A-Z0-9]*_)?(?P<id>\d{{3}})(?:_|$)")
EDITION = re.compile(r"_v(\d+(?:dot\d+)*)$")
VERSION = re.compile(r"^(?:>\s*)?(?:Document version|Version):\s*v(\d+(?:\.\d+)*)(?:\s+\([^\n]+\)\.?)?\s*$", re.M | re.I)
STATUS = re.compile(r"^(?:>\s*)?Status:\s*(.+)$", re.M | re.I)


def diagnose(root, archive_dirs=("docs/archive",)):
    root = Path(root).resolve()
    archives = [(root / name).resolve() for name in archive_dirs]
    if any(not path.is_relative_to(root) for path in archives):
        raise ValueError("archive directory must be inside the diagnostic root")
    current = defaultdict(list)
    historical = []
    findings = []
    documents = []
    for path in sorted(root.rglob("*.md")):
        if any(part in {".git", "node_modules", "__pycache__"} for part in path.parts):
            continue
        if path.is_symlink() or not path.resolve().is_relative_to(root):
            findings.append({"severity": "error", "path": path.relative_to(root).as_posix(), "issue": "unsafe document path"})
            continue
        match = NAME.match(path.stem)
        if not match:
            continue
        name = path.relative_to(root).as_posix()
        record_id = f"{match['family']}_{match['id']}"
        text = path.read_text(encoding="utf-8-sig")
        versions = list(dict.fromkeys(VERSION.findall(text)))
        status = STATUS.search(text)
        archived = any(path.resolve().is_relative_to(folder) for folder in archives)
        row = {"id": record_id, "path": name, "version": versions[0] if len(versions) == 1 else None,
               "status": status[1].strip() if status else None, "archived": archived}
        documents.append(row)
        if not versions:
            findings.append({"severity": "warning", "path": name, "issue": "unversioned legacy record; inspect local convention"})
        elif len(versions) != 1:
            findings.append({"severity": "error", "path": name, "issue": "ambiguous version metadata"})
        suffix = EDITION.search(path.stem)
        if archived:
            historical.append((row, suffix))
            if suffix and len(versions) == 1 and suffix[1].replace("dot", ".") != versions[0]:
                findings.append({"severity": "error", "path": name, "issue": "archive suffix differs from recorded edition"})
            if status and status[1].strip().lower() == "current":
                findings.append({"severity": "error", "path": name, "issue": "archive claims current status"})
        else:
            current[record_id].append(row)
            if suffix:
                findings.append({"severity": "warning", "path": name, "issue": "version-suffixed current path; inspect stable owner"})
            if status and status[1].strip().lower() in {"historical", "superseded", "archived"}:
                findings.append({"severity": "warning", "path": name, "issue": "historical status outside configured archive"})
    for record_id, rows in current.items():
        if len(rows) > 1:
            findings.append({"severity": "error", "id": record_id, "paths": [r["path"] for r in rows], "issue": "duplicate permanent ID across current owners"})
    editions = defaultdict(list)
    for row, suffix in historical:
        # Archive editions of one identity are legitimate; same edition twice is ambiguous.
        if row["version"]:
            editions[(row["id"], row["version"])].append(row["path"])
        if row["id"] not in current:
            findings.append({"severity": "warning", "path": row["path"], "issue": "no current owner found; may be intentionally retired"})
    for (record_id, version), paths in editions.items():
        if len(paths) > 1:
            findings.append({"severity": "error", "id": record_id, "paths": paths, "issue": f"duplicate archived edition v{version}"})
    return {"documents": documents, "findings": findings}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("root", type=Path)
    parser.add_argument("--archive", action="append", help="root-relative archive directory; repeat as needed")
    args = parser.parse_args()
    result = diagnose(args.root, args.archive if args.archive is not None else ("docs/archive",))
    print(json.dumps(result, indent=2))
    raise SystemExit(any(row["severity"] == "error" for row in result["findings"]))


if __name__ == "__main__":
    main()
