"""Exercise real Codex installation in a disposable home; never run a model.

Requires Codex CLI 0.159.1, Git, and requirements-dev.txt dependencies.
Use --source checkout to test the working package instead of published main.
"""

import argparse
import json
import os
from pathlib import Path
import shutil
import subprocess
import tempfile

import validate_package


ROOT = Path(__file__).resolve().parents[1]
MARKETPLACE = "ymas-workflows"
PLUGIN = "ymas-agent-workflows"
SELECTOR = f"{PLUGIN}@{MARKETPLACE}"
SKILLS = {"project-bootstrap", "spec-driven-development", "audit-repair", "bug-knowledge"}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source", choices=("published", "checkout"), default="published")
    args = parser.parse_args()
    codex = shutil.which("codex.cmd" if os.name == "nt" else "codex")
    if not codex or not shutil.which("git"):
        raise RuntimeError("Install Codex CLI 0.159.1 and Git, then rerun this check.")

    # TemporaryDirectory owns this exact directory and only removes its contents.
    with tempfile.TemporaryDirectory(prefix="ymas-install-") as directory:
        scratch = Path(directory)
        task_home = scratch / "codex-home"
        task_home.mkdir()
        env = dict(os.environ, CODEX_HOME=str(task_home), GIT_TERMINAL_PROMPT="0")

        def run(*arguments):
            result = subprocess.run(
                [codex, *arguments], cwd=scratch, env=env,
                capture_output=True, text=True, encoding="utf-8", timeout=180,
            )
            if result.returncode:
                raise RuntimeError(
                    f"codex {' '.join(arguments)} failed ({result.returncode})\n"
                    f"{result.stdout}\n{result.stderr}"
                )
            return result.stdout

        print(run("--version").strip(), flush=True)
        run("plugin", "marketplace", "--help")
        source = "YouMissedASpot/ymas-agent-workflows"
        if args.source == "checkout":
            catalog_root = scratch / "catalog"
            shutil.copytree(ROOT, catalog_root / "plugin", ignore=shutil.ignore_patterns(".git", "__pycache__"))
            catalog = catalog_root / ".agents" / "plugins"
            catalog.mkdir(parents=True)
            (catalog / "marketplace.json").write_text(json.dumps({
                "name": MARKETPLACE,
                "plugins": [{"name": PLUGIN, "source": {"source": "local", "path": "./plugin"},
                             "policy": {"installation": "AVAILABLE", "authentication": "ON_INSTALL"}}],
            }), encoding="utf-8")
            source = str(catalog_root)

        run("plugin", "marketplace", "add", source)
        if MARKETPLACE not in run("plugin", "marketplace", "list"):
            raise RuntimeError("Marketplace registration was not discoverable.")

        def verify_install():
            run("plugin", "add", SELECTOR)
            listing = json.loads(run("plugin", "list", "--marketplace", MARKETPLACE, "--json"))
            entries = [entry for entry in listing["installed"] if entry["pluginId"] == SELECTOR]
            if len(entries) != 1 or not entries[0]["installed"] or not entries[0]["enabled"]:
                raise RuntimeError("Plugin must be installed and enabled exactly once.")
            manifests = list((task_home / "plugins" / "cache" / MARKETPLACE / PLUGIN).glob("*/plugin.json"))
            if len(manifests) != 1:
                raise RuntimeError(f"Expected one installed package, found {len(manifests)}.")
            installed = manifests[0].parent
            if {path.parent.name for path in (installed / "skills").glob("*/SKILL.md")} != SKILLS:
                raise RuntimeError("Installed skill set differs from the four documented skills.")
            validate_package.ROOT = installed
            validate_package.SKILL_ROOT = installed / "skills"
            validate_package.MARKETPLACE = installed / ".agents/plugins/marketplace.json"
            failures = validate_package.validate()
            if failures:
                raise RuntimeError("\n".join(failures))

        verify_install()
        print("PASS: fresh registration, installation, four skills, and package validation", flush=True)
        verify_install()
        print("PASS: repeat installation", flush=True)
        if args.source == "published":
            run("plugin", "marketplace", "upgrade", MARKETPLACE)
            verify_install()
            print("PASS: marketplace refresh and reinstall", flush=True)
        run("plugin", "remove", SELECTOR)
        listing = json.loads(run("plugin", "list", "--marketplace", MARKETPLACE, "--json"))
        if any(entry["pluginId"] == SELECTOR for entry in listing["installed"]):
            raise RuntimeError("Plugin still listed as installed after removal.")
        verify_install()
        print("PASS: removal and reinstall; no model session or user-home changes", flush=True)


if __name__ == "__main__":
    main()
