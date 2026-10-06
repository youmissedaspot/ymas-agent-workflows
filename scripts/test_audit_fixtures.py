"""Executable fixture controls, not model trials or audit efficacy measurements."""

import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

from audit_fixtures import DATA, create_fixture


class AuditFixtureTest(unittest.TestCase):
    def exercise(self, root, *args):
        result = subprocess.run([sys.executable, "-B", str(root / "tools/check_lookup.py"), *args],
                                cwd=root, capture_output=True, text=True, timeout=15)
        self.assertTrue(result.stdout, result.stderr)
        return result.returncode, json.loads(result.stdout)

    def snapshot(self, root):
        return {path.relative_to(root).as_posix(): path.read_bytes()
                for path in root.rglob("*") if path.is_file()}

    def test_known_good_checks_actual_boundaries_without_writes(self):
        with tempfile.TemporaryDirectory() as directory:
            root = create_fixture("known-good", Path(directory) / "subject")
            before = self.snapshot(root)
            code, result = self.exercise(root)
            self.assertEqual(code, 0)
            self.assertTrue(all(result["checks"].values()))
            self.assertEqual(self.snapshot(root), before)

    def test_seeded_defect_fails_original_boundary_but_preserves_correct_neighbors(self):
        with tempfile.TemporaryDirectory() as directory:
            root = create_fixture("seeded-defect", Path(directory) / "subject")
            code, result = self.exercise(root)
            self.assertEqual(code, 1)
            self.assertEqual(result["checks"], {"present": True, "absent_raises": False, "reads_preserve_data": True})

    def test_broken_fixture_blocks_before_exercise_and_valid_data_passes_same_product(self):
        with tempfile.TemporaryDirectory() as directory:
            root = create_fixture("broken-fixture", Path(directory) / "subject")
            before = (root / "src/lookup.py").read_bytes()
            code, result = self.exercise(root)
            self.assertEqual((code, result["phase"], result["cause"]), (2, "preflight", "fixture"))
            self.assertNotIn("checks", result)
            (root / "data.json").write_text(json.dumps(DATA), encoding="utf-8")
            self.assertEqual(self.exercise(root)[0], 0)
            self.assertEqual((root / "src/lookup.py").read_bytes(), before)

    def test_competing_reports_are_bound_to_same_actual_failing_source(self):
        with tempfile.TemporaryDirectory() as directory:
            root = create_fixture("competing-audits", Path(directory) / "subject")
            code, result = self.exercise(root)
            self.assertEqual(code, 1)
            for report in ("report-a.json", "report-b.json"):
                recorded = json.loads((root / "reports" / report).read_text())
                self.assertEqual(recorded["source_sha256"], result["source_sha256"])
            # The recorded severity/recommendations are trial inputs, not an executable verdict.
            self.assertTrue(result["checks"]["present"])
            self.assertTrue(result["checks"]["reads_preserve_data"])

    def test_original_regression_detects_before_source_and_passes_repair(self):
        with tempfile.TemporaryDirectory() as directory:
            root = create_fixture("original-closure", Path(directory) / "subject")
            before = self.exercise(root, "--source", str(root / "history/lookup-before.py"))
            after = self.exercise(root)
            self.assertEqual((before[0], after[0]), (1, 0))
            self.assertFalse(before[1]["checks"]["absent_raises"])
            self.assertTrue(after[1]["checks"]["absent_raises"])
            self.assertNotEqual(before[1]["source_sha256"], after[1]["source_sha256"])

    def test_stale_evidence_identifies_prior_failure_without_condemning_current_source(self):
        with tempfile.TemporaryDirectory() as directory:
            root = create_fixture("stale-evidence", Path(directory) / "subject")
            report = json.loads((root / "reports/prior.json").read_text())
            old = self.exercise(root, "--source", str(root / report["source_path"]))
            current = self.exercise(root)
            self.assertEqual(report["source_sha256"], old[1]["source_sha256"])
            self.assertNotEqual(report["source_sha256"], current[1]["source_sha256"])
            self.assertEqual((old[0], current[0]), (1, 0))

    def test_factory_rejects_existing_targets_and_unknown_cases_without_overwriting(self):
        with tempfile.TemporaryDirectory() as directory:
            root = create_fixture("known-good", Path(directory) / "subject")
            before = self.snapshot(root)
            with self.assertRaises(FileExistsError):
                create_fixture("seeded-defect", root)
            with self.assertRaises(ValueError):
                create_fixture("unknown", Path(directory) / "other")
            self.assertEqual(before, self.snapshot(root))
            self.assertFalse((Path(directory) / "other").exists())


if __name__ == "__main__":
    unittest.main()
