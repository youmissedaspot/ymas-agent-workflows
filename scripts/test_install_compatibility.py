"""Disposable installation identity and validator controls; no CLI install or model."""

from pathlib import Path
import shutil
import tempfile
import unittest

from check_receipt import package_inventory
from smoke_install import verify_installed_package, verify_installed_snapshot


class InstallationIdentityTest(unittest.TestCase):
    def test_installed_validator_owns_its_contract_and_failures_propagate(self):
        with tempfile.TemporaryDirectory() as directory:
            installed = Path(directory)
            scripts = installed / "scripts"
            scripts.mkdir()
            validator = scripts / "validate_package.py"
            validator.write_text('print("installed release contract checked")\n', encoding="utf-8")
            self.assertIn("installed release contract checked", verify_installed_package(installed))
            validator.write_text(
                'from pathlib import Path\n'
                'import sys\n'
                'if not Path("required-asset.json").is_file():\n'
                '    sys.exit("required installed asset missing")\n'
                'print("required installed asset checked")\n', encoding="utf-8")
            with self.assertRaisesRegex(RuntimeError, "required installed asset missing"):
                verify_installed_package(installed)
            (installed / "required-asset.json").write_text("{}", encoding="utf-8")
            self.assertIn("required installed asset checked", verify_installed_package(installed))

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
