"""Synthetic outcome and negative-control tests, not model-run results."""

import copy
import json
import unittest

from grade_behavior import CASES, grade, grade_run


class GraderTest(unittest.TestCase):
    def setUp(self):
        self.cases = json.loads(CASES.read_text(encoding="utf-8"))["cases"]

    def good(self, case):
        return {"route": case["route"], "actions": case["required"].copy(),
                "writes": case["writes"].copy(), "decisions": case["decisions"].copy(),
                "human_acceptance_claimed": False}

    def test_positive_and_negative_controls_for_every_case(self):
        self.assertEqual(len(self.cases), 28)
        for case in self.cases:
            with self.subTest(case=case["id"]):
                observation = self.good(case)
                self.assertEqual(grade(case, observation), [])
                for route in case.get("routes", [case["route"]]):
                    self.assertEqual(grade(case, {**observation, "route": route}), [])
                for mutation in ("missing", "forbidden", "write", "route", "acceptance"):
                    bad = copy.deepcopy(observation)
                    if mutation == "missing":
                        bad["actions"] = []
                    elif mutation == "forbidden":
                        bad["actions"].append(case["forbidden"][0])
                    elif mutation == "write":
                        bad["writes"].append("unrelated/file.txt")
                    elif mutation == "route":
                        bad["route"] = "unrelated"
                    else:
                        bad["human_acceptance_claimed"] = True
                    self.assertTrue(grade(case, bad), mutation)
                for action in case["required"]:
                    bad = self.good(case)
                    bad["actions"].remove(action)
                    self.assertIn("missing required actions", grade(case, bad), action)
                for action in case["forbidden"]:
                    bad = self.good(case)
                    bad["actions"].append(action)
                    self.assertIn("forbidden action", grade(case, bad), action)
                if case["decisions"]:
                    observation["decisions"] = []
                    self.assertIn("accepted decision lost", grade(case, observation))
                if case["writes"]:
                    observation = self.good(case)
                    observation["writes"] = []
                    self.assertIn("requested write outcome absent", grade(case, observation))

    def test_missing_cases_metadata_and_malformed_observation(self):
        self.assertTrue(grade_run({"kind": "observed_replay"})["run"])
        self.assertTrue(grade(self.cases[0], {"actions": "ask_target"}))
        run = {"kind": "synthetic_grader_fixture", "metadata": {
            key: "synthetic" for key in ("package_source", "package_version", "model", "effort", "permissions", "artifacts")},
            "observations": {case["id"]: self.good(case) for case in self.cases}}
        self.assertFalse(any(grade_run(run).values()))
        del run["observations"][self.cases[0]["id"]]
        self.assertTrue(grade_run(run)["run"])

    def test_affected_cases_are_explicit_and_cannot_hide_missing_outcomes(self):
        case = self.cases[0]
        run = {"kind": "synthetic_grader_fixture", "case_ids": [case["id"]], "metadata": {
            key: "synthetic" for key in ("package_source", "package_version", "model", "effort", "permissions", "artifacts")},
            "observations": {case["id"]: self.good(case)}}
        self.assertEqual(grade_run(run), {case["id"]: []})
        for selected in ([], [case["id"], case["id"]], ["unknown"], [case["id"], self.cases[1]["id"]]):
            run["case_ids"] = selected
            self.assertTrue(grade_run(run)["run"])

    def test_explicitly_valid_supporting_route(self):
        case = {**self.cases[0], "routes": [self.cases[0]["route"], "supporting-contract"]}
        observation = self.good(case)
        observation["route"] = "supporting-contract"
        self.assertEqual(grade(case, observation), [])


if __name__ == "__main__":
    unittest.main()
