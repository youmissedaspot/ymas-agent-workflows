"""Regression checks for package links and materialized template references."""

from pathlib import Path
import shutil
import tempfile
import unittest
from unittest.mock import patch

import validate_package


def materialized_link_errors(document):
    errors = []
    for target in validate_package.LINK.findall(document.read_text(encoding="utf-8-sig")):
        validate_package.check_local_path(document, target, errors)
    return errors


class PackageLinksTest(unittest.TestCase):
    def test_fenced_and_inline_html_do_not_make_real_anchors(self):
        text = '````html\n<a id="fake">\n```\n## Still fake\n````\n`<a id="inline-fake">`\n<a id="real">\n# Real heading\n'
        self.assertEqual(validate_package.markdown_anchors(text), {"real", "real-heading"})

    def test_blockquoted_fences_and_unequal_inline_delimiters(self):
        text = '> ```html\n> <a id="quoted-fake">\n> ```\n``literal `<a id="inline-fake">` more``\n<a id="real">\n'
        self.assertEqual(validate_package.markdown_anchors(text), {"real"})

    def test_anchors_same_file_cross_file_duplicates_and_fenced_examples(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            source = root / "README.md"
            source.write_text("# Owner\n## systems.md\n## Same\n## Same\n```md\n## Fake\n```\n", encoding="utf-8")
            with patch.object(validate_package, "ROOT", root):
                errors = []
                for target in ("#owner", "README.md#systemsmd", "#same-1"):
                    validate_package.check_local_path(source, target, errors)
                self.assertEqual(errors, [])
                for target in ("#fake", "README.md#absent"):
                    validate_package.check_local_path(source, target, errors)
                self.assertEqual(len(errors), 2)

    def test_materialized_template_links_resolve_without_the_package(self):
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
                    self.assertEqual(materialized_link_errors(document), [])

    def test_materialized_worksheet_link_accepts_project_owner_and_rejects_package_path(self):
        package_root = validate_package.ROOT
        with tempfile.TemporaryDirectory() as directory:
            adopter = Path(directory) / "adopter"
            document = adopter / "docs/sot/SOT_PRODUCT_001_product-truth.md"
            worksheet = adopter / "docs/worksheets/product-truth.md"
            document.parent.mkdir(parents=True)
            worksheet.parent.mkdir(parents=True)
            worksheet.write_text("# Product decisions\n", encoding="utf-8")
            template = (package_root / "skills/spec-driven-development/assets/true_specification_template.md").read_text(encoding="utf-8-sig")
            project_target = "../worksheets/product-truth.md"
            package_target = "../../true-spec-worksheet/assets/true_spec_worksheet_template.md"
            document.write_text(template + f"\nDecision worksheet: [Worksheet]({project_target}).\n", encoding="utf-8")
            with patch.object(validate_package, "ROOT", adopter), \
                    patch.object(validate_package, "check_local_path", wraps=validate_package.check_local_path) as check:
                self.assertEqual(materialized_link_errors(document), [])
                self.assertGreater(check.call_count, 0)
                self.assertIn(project_target, [call.args[1] for call in check.call_args_list])
                document.write_text(document.read_text(encoding="utf-8").replace(project_target, package_target), encoding="utf-8")
                errors = materialized_link_errors(document)
                self.assertEqual(len(errors), 1)
                self.assertIn(package_target, errors[0])
                self.assertTrue(worksheet.is_file())

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
