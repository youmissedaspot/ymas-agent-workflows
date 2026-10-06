"""Release-specific catalog checks; no CLI installation or model discovery."""

import json
from pathlib import Path
import unittest

from smoke_install import SKILLS_BY_VERSION, verify_skill_contract


class SkillContractTest(unittest.TestCase):
    def test_candidate_catalog_matches_the_actual_package(self):
        root = Path(__file__).resolve().parents[1]
        version = json.loads((root / "plugin.json").read_text(encoding="utf-8"))["version"]
        skills = {path.parent.name for path in (root / "skills").glob("*/SKILL.md")}
        self.assertEqual(version, "0.5.1")
        self.assertEqual(len(skills), 9)
        verify_skill_contract(version, skills)
        with self.assertRaisesRegex(RuntimeError, "9 documented skills"):
            verify_skill_contract(version, skills - {"like-im-5"})

    def test_previous_eight_skill_catalogs_are_retained(self):
        previous = {"project-bootstrap", "spec-driven-development", "audit-repair", "bug-knowledge",
                    "evaluate-repository", "documentation-consolidation", "workflow-orientation", "true-spec-worksheet"}
        for version in ("0.4.0", "0.4.1"):
            with self.subTest(version=version):
                self.assertEqual(SKILLS_BY_VERSION[version], previous)
                verify_skill_contract(version, previous)
                with self.assertRaisesRegex(RuntimeError, "8 documented skills"):
                    verify_skill_contract(version, previous | {"like-im-5"})

    def test_unexpected_skills_and_unknown_versions_fail(self):
        self.assertEqual(SKILLS_BY_VERSION["0.5.0"], SKILLS_BY_VERSION["0.5.1"])
        verify_skill_contract("0.5.0", SKILLS_BY_VERSION["0.5.0"])
        with self.assertRaisesRegex(RuntimeError, "9 documented skills"):
            verify_skill_contract("0.5.1", SKILLS_BY_VERSION["0.5.1"] | {"unrelated"})
        with self.assertRaisesRegex(RuntimeError, "No documented skill contract"):
            verify_skill_contract("0.5.2", SKILLS_BY_VERSION["0.5.1"])


if __name__ == "__main__":
    unittest.main()
