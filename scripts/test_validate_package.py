"""Regression checks for package link containment through path aliases."""

from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

import validate_package


class PackageLinksTest(unittest.TestCase):
    def test_noncanonical_root_accepts_internal_and_rejects_invalid_links(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory) / "package"
            (root / "child").mkdir(parents=True)
            (root / "target.md").write_text("target", encoding="utf-8")
            (root.parent / "outside.md").write_text("outside", encoding="utf-8")
            alias = root / "child" / ".."
            source = alias / "README.md"
            with patch.object(validate_package, "ROOT", alias):
                errors = []
                validate_package.check_local_path(source, "target.md", errors)
                self.assertEqual(errors, [])
                validate_package.check_local_path(source, "missing.md", errors)
                self.assertEqual(len(errors), 1)
                self.assertIn("missing.md", errors[0])
                validate_package.check_local_path(source, "../outside.md", errors)
                self.assertEqual(len(errors), 2)
                self.assertIn("../outside.md", errors[1])


if __name__ == "__main__":
    unittest.main()
