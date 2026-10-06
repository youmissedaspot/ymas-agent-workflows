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
        self.assertEqual(len(self.cases), 12)
        for case in self.cases:
            with self.subTest(case=case["id"]):
                observation = self.good(case)
                self.assertEqual(grade(case, observation), [])
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


if __name__ == "__main__":
    unittest.main()
