"""Deterministic synthetic fixture exercise; stdout JSON, no persisted resources."""

import json
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
from records import lookup


def exercise():
    records = {"entry": "value"}
    before = dict(records)
    observed = {"existing": lookup(records, "entry"), "missing": lookup(records, "absent"),
                "unchanged": records == before}
    passed = observed == {"existing": "value", "missing": None, "unchanged": True}
    return {"scenario": "scenario.records-lookup", "passed": passed, "observed": observed,
            "scope": "synthetic in-memory fixture", "cleanup": "no persisted resources"}


if __name__ == "__main__":
    result = exercise()
    print(json.dumps(result, sort_keys=True))
    raise SystemExit(not result["passed"])
