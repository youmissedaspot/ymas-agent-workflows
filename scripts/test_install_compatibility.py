"""Disposable byte-copy compatibility checks; no CLI install or model execution."""

from pathlib import Path
import shutil
import tempfile
import unittest

from check_receipt import package_inventory
from smoke_install import verify_installed_snapshot


class InstallationIdentityTest(unittest.TestCase):
    def test_equal_version_and_skills_do_not_hide_changed_supporting_files(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            source = root / "source"
            source.mkdir()
            (source / "plugin.json").write_text('{"version":"0.4.0"}', encoding="utf-8")
            (source / "contract.md").write_text("stop known blockers", encoding="utf-8")
            expected = package_inventory(source, ["plugin.json", "contract.md"])
            installed = root / "copied-package"
            shutil.copytree(source, installed)
            verify_installed_snapshot(expected, installed)
            (installed / "contract.md").write_text("retry known blockers", encoding="utf-8")
            with self.assertRaisesRegex(RuntimeError, "contract.md"):
                verify_installed_snapshot(expected, installed)

    def test_missing_installed_path_fails(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "contract.md").write_text("contract", encoding="utf-8")
            expected = package_inventory(root, ["contract.md"])
            empty = root / "empty"
            empty.mkdir()
            with self.assertRaises(OSError):
                verify_installed_snapshot(expected, empty)


if __name__ == "__main__":
    unittest.main()
