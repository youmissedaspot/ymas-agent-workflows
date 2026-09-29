"""Validate the portable plugin package and its local documentation routes."""

import json
import re
import sys
from pathlib import Path
from urllib.parse import unquote, urlparse
from urllib.request import urlopen

import yaml
from jsonschema.validators import validator_for


ROOT = Path(__file__).resolve().parents[1]
SKILL_ROOT = ROOT / "skills"
MARKETPLACE = ROOT / ".agents/plugins/marketplace.json"
LINK = re.compile(r"!?\[[^\]]*\]\(([^)]+)\)")
INDEX_ROUTE = re.compile(r"→\s*`([^`]+)`")
SEMVER = re.compile(r"(?:0|[1-9]\d*)\.(?:0|[1-9]\d*)\.(?:0|[1-9]\d*)")


def check_local_path(source: Path, target: str, errors: list[str]) -> None:
    target = target.strip().strip("<>").split(" ", 1)[0]
    if target.startswith("#") or urlparse(target).scheme or target.startswith("//"):
        return
    path = unquote(target.split("#", 1)[0].split("?", 1)[0])
    if not path:
        return
    resolved = (source.parent / path).resolve()
    if not resolved.is_relative_to(ROOT.resolve()) or not resolved.exists():
        errors.append(f"{source.relative_to(ROOT)}: missing local target {target}")


def validate() -> list[str]:
    errors: list[str] = []
    try:
        manifest = json.loads((ROOT / "plugin.json").read_text(encoding="utf-8"))
        marketplace = json.loads(MARKETPLACE.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        return [f"Package JSON could not be read: {exc}"]

    schema_url = manifest.get("$schema")
    if schema_url != "https://agent-plugins.org/schemas/1.0.0/plugin.schema.json":
        errors.append("plugin.json: unexpected portable plugin schema")
    else:
        try:
            with urlopen(schema_url, timeout=15) as response:
                schema = json.load(response)
            validator = validator_for(schema)
            validator.check_schema(schema)
            for error in validator(schema).iter_errors(manifest):
                errors.append(f"plugin.json: {error.message}")
        except Exception as exc:
            errors.append(f"plugin.json: schema validation unavailable: {exc}")

    name = manifest.get("name")
    if not isinstance(name, str) or not name:
        errors.append("plugin.json: name must be nonempty")
    version = manifest.get("version")
    if not isinstance(version, str) or not SEMVER.fullmatch(version):
        errors.append("plugin.json: version must be major.minor.patch")
    if not (ROOT / "LICENSE").is_file():
        errors.append("LICENSE is missing")

    plugins = marketplace.get("plugins")
    if not isinstance(plugins, list) or len(plugins) != 1:
        errors.append("marketplace.json: expected one plugin entry")
    else:
        entry = plugins[0]
        if entry.get("name") != name:
            errors.append("marketplace.json: plugin name differs from plugin.json")
        source = entry.get("source", {})
        if source.get("source") != "url":
            errors.append("marketplace.json: expected a Git URL source")
        repository = manifest.get("repository", "")
        source_url = source.get("url", "")
        if not isinstance(repository, str) or not isinstance(source_url, str) or source_url.removesuffix(".git").lower() != repository.rstrip("/").lower():
            errors.append("marketplace.json: source URL differs from manifest repository")

    skills = sorted(SKILL_ROOT.glob("*/SKILL.md"))
    if not skills:
        errors.append("No skills/<name>/SKILL.md files found")
    for skill in skills:
        contents = skill.read_text(encoding="utf-8-sig")
        parts = contents.split("---", 2)
        if len(parts) < 3 or parts[0].strip():
            errors.append(f"{skill.relative_to(ROOT)}: missing YAML front matter")
            continue
        try:
            front = yaml.safe_load(parts[1])
        except yaml.YAMLError as exc:
            errors.append(f"{skill.relative_to(ROOT)}: invalid YAML: {exc}")
            continue
        if not isinstance(front, dict):
            errors.append(f"{skill.relative_to(ROOT)}: front matter must be a mapping")
            continue
        if front.get("name") != skill.parent.name:
            errors.append(f"{skill.relative_to(ROOT)}: name differs from directory")
        if not isinstance(front.get("description"), str) or not front["description"].strip():
            errors.append(f"{skill.relative_to(ROOT)}: description must be nonempty")

    markdown_files = sorted(ROOT.rglob("*.md"))
    markdown_files = [path for path in markdown_files if ".git" not in path.parts]
    link_count = 0
    for document in markdown_files:
        contents = document.read_text(encoding="utf-8-sig")
        for target in LINK.findall(contents):
            link_count += 1
            check_local_path(document, target, errors)
        if document == ROOT / "INDEX.md":
            for target in INDEX_ROUTE.findall(contents):
                check_local_path(document, target, errors)

    print(f"Checked {len(skills)} skill front-matter blocks, {len(markdown_files)} Markdown files, and {link_count} Markdown links.")
    return errors


if __name__ == "__main__":
    failures = validate()
    for failure in failures:
        print(f"ERROR: {failure}", file=sys.stderr)
    sys.exit(1 if failures else 0)
