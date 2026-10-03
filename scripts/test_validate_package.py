"""Regression checks for package links and materialized versioning references."""

from pathlib import Path
import shutil
import tempfile
import unittest
from unittest.mock import patch

import validate_package


class PackageLinksTest(unittest.TestCase):
    def test_materialized_template_versioning_links_resolve_without_the_package(self):
        package_root = validate_package.ROOT
        outputs = (
            ("skills/project-bootstrap/assets/documentation_standard_template.md",
             "docs/OPS_WORKFLOW_DOCS_001_documentation-standard.md"),
            ("skills/spec-driven-development/assets/true_specification_template.md",
             "docs/sot/SOT_PRODUCT_001_product-truth.md"),
            ("skills/spec-driven-development/assets/canonical_specification_template.md",
             "docs/specifications/SPEC_PRODUCT_001_requirements.md"),
            ("skills/spec-driven-development/assets/detailed_system_specification_template.md",
             "docs/specifications/SPEC_PRODUCT_002_system-behavior.md"),
            ("skills/spec-driven-development/assets/architecture_specification_template.md",
             "docs/specifications/SPECARC_PRODUCT_001_architecture.md"),
            ("skills/spec-driven-development/assets/systems_map_template.md",
             "docs/systems/systems.md"),
            ("skills/spec-driven-development/assets/systems_map_template.md",
             "systems.md"),
        )
        with tempfile.TemporaryDirectory() as directory:
            adopter = Path(directory) / "adopter"
            for template, destination in outputs:
                document = adopter / destination
                document.parent.mkdir(parents=True, exist_ok=True)
                shutil.copyfile(package_root / template, document)
                with self.subTest(template=template, destination=destination), \
                        patch.object(validate_package, "ROOT", adopter):
                    errors = []
                    for target in validate_package.LINK.findall(document.read_text(encoding="utf-8-sig")):
                        if "document_versioning" in target:
                            validate_package.check_local_path(document, target, errors)
                    self.assertEqual(errors, [])

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
