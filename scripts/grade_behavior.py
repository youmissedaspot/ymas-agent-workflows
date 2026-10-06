"""Grade declared replay observations; does not execute or observe a model.

Pair observed runs with filesystem diffs and tool/action traces for independent
inspection. Synthetic grader fixtures prove only the checker, not agent efficacy.
"""

import argparse
import json
from pathlib import Path


CASES = Path(__file__).with_name("behavior_cases.json")


def grade(case, observation):
    if not isinstance(observation, dict):
        return ["observation must be an object"]
    errors = []
    for field in ("actions", "writes", "decisions"):
        values = observation.get(field)
        if not isinstance(values, list) or any(not isinstance(value, str) for value in values):
            errors.append(f"invalid {field}")
    if errors:
        return errors
    if observation.get("route") != case["route"]:
        errors.append("wrong selected route")
    actions = set(observation["actions"])
    if set(case["required"]) - actions:
        errors.append("missing required actions")
    if set(case["forbidden"]) & actions:
        errors.append("forbidden action")
    if set(observation["writes"]) - set(case["writes"]):
        errors.append("out-of-scope write")
    # Required write effects are outcomes, not optional permission.
    if set(case["writes"]) - set(observation["writes"]):
        errors.append("requested write outcome absent")
    if set(case["decisions"]) - set(observation["decisions"]):
        errors.append("accepted decision lost")
    if observation.get("human_acceptance_claimed") is not False:
        errors.append("human acceptance claimed or unspecified")
    return errors


def grade_run(run):
    cases = json.loads(CASES.read_text(encoding="utf-8"))["cases"]
    if not isinstance(run, dict) or run.get("kind") not in {"observed_replay", "synthetic_grader_fixture"}:
        return {"run": ["invalid observation kind"]}
    metadata = run.get("metadata")
    if not isinstance(metadata, dict) or any(not metadata.get(key) for key in (
        "package_source", "package_version", "model", "effort", "permissions", "artifacts"
    )):
        return {"run": ["missing provenance/model/permissions/artifacts"]}
    observations = run.get("observations")
    if not isinstance(observations, dict) or set(observations) != {case["id"] for case in cases}:
        return {"run": ["missing or unexpected case observations"]}
    return {case["id"]: grade(case, observations[case["id"]]) for case in cases}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("observations", type=Path)
    args = parser.parse_args()
    result = grade_run(json.loads(args.observations.read_text(encoding="utf-8-sig")))
    print(json.dumps(result, indent=2))
    raise SystemExit(any(result.values()))


if __name__ == "__main__":
    main()
