"""Neutral permanent-ID collision and preserved-edition cases."""

from pathlib import Path
import tempfile
import unittest

from diagnose_documents import diagnose


class DocumentTest(unittest.TestCase):
    def test_version_examples_inside_fences_are_not_metadata(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            self.write(root, "docs/SPEC_STORAGE_001_access.md", 'Version: v1\nStatus: Current\n````md\nVersion: v2\n```\nVersion: v3\n````\n')
            self.assertEqual(diagnose(root)["findings"], [])

    def test_blockquoted_version_example_is_not_metadata(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            self.write(root, "docs/SPEC_STORAGE_001_access.md", 'Version: v1\nStatus: Current\n> ```text\n> Version: v2\n> ```\n')
            self.assertEqual(diagnose(root)["findings"], [])

    def write(self, root, name, text="Version: v1\nStatus: Current\n"):
        path = root / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text, encoding="utf-8")

    def test_concurrent_categories_and_legacy_next_collide(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            for name in ("docs/OPS_TASK_DOCS_012_one.md", "docs/OPS_TASK_API_012_two.md",
                         "docs/OPS_NEXT_013_DOCS_action.md", "legacy/OPS_NEXT_API_013_other.md"):
                self.write(root, name)
            errors = [row for row in diagnose(root)["findings"] if row["severity"] == "error"]
            self.assertEqual({row["id"] for row in errors}, {"OPS_TASK_012", "OPS_NEXT_013"})

    def test_archives_keep_id_without_colliding_with_current(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            self.write(root, "docs/SPEC_STORAGE_001_access.md", "Version: v3.1\nStatus: Current\n")
            self.write(root, "docs/archive/SPEC_STORAGE_001_access_v2.md", "Version: v2\nStatus: Historical\n")
            self.write(root, "docs/archive/SPEC_STORAGE_001_access_v3.md", "Version: v3\nStatus: Historical\n")
            self.write(root, "docs/archive/SPEC_STORAGE_001_access_v1.md", "> Status: Historical / superseded\n> Version: v1\nVersion: v1\nStatus: Current\n")
            self.assertEqual(diagnose(root)["findings"], [])

    def test_archive_metadata_and_duplicate_editions(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            self.write(root, "docs/SPEC_STORAGE_001_access.md")
            self.write(root, "docs/archive/SPEC_STORAGE_001_access_v3dot1.md", "Version: v3\nStatus: Current\n")
            self.write(root, "docs/archive/old/SPEC_STORAGE_001_access_v3.md", "Version: v3\nStatus: Historical\n")
            issues = [row["issue"] for row in diagnose(root)["findings"]]
            self.assertIn("archive suffix differs from recorded edition", issues)
            self.assertIn("archive claims current status", issues)
            self.assertIn("duplicate archived edition v3", issues)

    def test_read_only_and_custom_archive(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            self.write(root, "docs/OPS_TASK_001_legacy.md", "legacy text")
            self.write(root, "history/OPS_TASK_001_legacy_v1.md", "Status: Historical\n")
            before = {str(p): p.read_bytes() for p in root.rglob("*.md")}
            result = diagnose(root, ("history",))
            self.assertFalse(any(r["severity"] == "error" for r in result["findings"]))
            self.assertEqual(before, {str(p): p.read_bytes() for p in root.rglob("*.md")})
            with self.assertRaises(ValueError):
                diagnose(root, ("../outside",))


if __name__ == "__main__":
    unittest.main()
