"""Validate the portable plugin package and its local documentation routes."""

import json
import re
import sys
import unicodedata
from pathlib import Path
from urllib.parse import unquote, urlparse
from urllib.request import urlopen

import yaml
from jsonschema.validators import validator_for
from markdown_utils import visible_lines, without_inline_code
from check_feature_map import check_freshness, load_json, validate_map


ROOT = Path(__file__).resolve().parents[1]
SKILL_ROOT = ROOT / "skills"
MARKETPLACE = ROOT / ".agents/plugins/marketplace.json"
LINK = re.compile(r"!?\[[^\]]*\]\(([^)]+)\)")
INDEX_ROUTE = re.compile(r"→\s*`([^`]+)`")
SEMVER = re.compile(r"(?:0|[1-9]\d*)\.(?:0|[1-9]\d*)\.(?:0|[1-9]\d*)")


def markdown_anchors(contents: str) -> set[str]:
    """Common GitHub heading slugs and explicit HTML IDs; skip fenced examples."""
    anchors = set()
    counts = {}
    for line in visible_lines(contents):
        html = without_inline_code(line)
        for tag in re.findall(r"<[A-Za-z][^>]*>", html):
            anchors.update(re.findall(r'\bid=["\']([^"\']+)["\']', tag))
        heading = re.match(r"^ {0,3}#{1,6}\s+(.+?)\s*#*\s*$", line)
        if not heading:
            continue
        title = re.sub(r"<[^>]+>", "", heading[1]).lower()
        slug = "".join(c for c in title if c in " -_" or unicodedata.category(c)[0] in "LN").replace(" ", "-")
        count = counts.get(slug, 0)
        counts[slug] = count + 1
        anchors.add(f"{slug}-{count}" if count else slug)
    return anchors


def check_local_path(source: Path, target: str, errors: list[str]) -> None:
    target = target.strip().strip("<>").split(" ", 1)[0]
    if urlparse(target).scheme or target.startswith("//"):
        return
    path = unquote(target.split("#", 1)[0].split("?", 1)[0])
    resolved = (source.parent / path).resolve() if path else source.resolve()
    if not resolved.is_relative_to(ROOT.resolve()) or not resolved.exists():
        errors.append(f"{source.relative_to(ROOT)}: missing local target {target}")
        return
    fragment = unquote(target.partition("#")[2])
    if fragment and resolved.is_file() and resolved.suffix.lower() == ".md":
        if fragment not in markdown_anchors(resolved.read_text(encoding="utf-8-sig")):
            errors.append(f"{source.relative_to(ROOT)}: missing local anchor {target}")


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

    feature_assets = SKILL_ROOT / "spec-driven-development/assets"
    try:
        feature_schema = load_json(feature_assets / "feature_map.schema.json")
        for map_path, source_root in (
            (feature_assets / "feature_map_template.json", None),
            (feature_assets / "feature_map_example/feature_map.json", feature_assets / "feature_map_example"),
        ):
            feature_map = load_json(map_path)
            findings = validate_map(feature_map, feature_schema)
            if not findings and source_root is not None:
                findings = check_freshness(feature_map, source_root)
            errors.extend(f"{map_path.relative_to(ROOT)}: {row['code']}: {row['message']}" for row in findings)
    except (OSError, ValueError) as exc:
        errors.append(f"Feature Map assets unavailable: {exc}")

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
