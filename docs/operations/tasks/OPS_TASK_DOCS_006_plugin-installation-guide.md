# OPS_TASK_006 — Plugin installation guide and local verification

Status: Complete on `work/plugin-installation`; integration pending.

The shell resolved npm-managed Codex CLI `0.101.0`, whose help exposed no plugin command. The desktop application's separate `0.158.0-alpha.2.1` executable did expose it. The earlier successful smoke test used a temporary Codex home and had not repaired the global npm installation.

On September 29, 2026, upgraded the existing global npm package to `@openai/codex@0.159.1`. PowerShell continued resolving the npm wrapper and reported the new version. Registered `YouMissedASpot/ymas-agent-workflows` as `ymas-workflows` and installed `ymas-agent-workflows@ymas-workflows` in the actual user Codex home. Marketplace listing confirmed the registration; plugin listing reported version `0.2.0` as installed and enabled.

Backed up user configuration before installation. The configuration diff added only the YMAS marketplace and enabled-plugin entries. Existing plugin settings and standalone skills were retained; the desktop executable was not changed.

The installed package validator passed: four skill front-matter blocks, 26 Markdown files, and 33 Markdown links. A fresh ephemeral read-only CLI session reported all four YMAS skills from `plugins/cache/ymas-workflows/ymas-agent-workflows/0.2.0/skills/`, separately from the existing standalone skills. The check requested only injected-catalog discovery, with no workflow execution or project-file modifications. Startup emitted unrelated existing-plugin/configuration compatibility warnings; this check does not establish the health of every other plugin.

Updated the README with capability checks, the verified npm upgrade, Windows command-resolution troubleshooting, separate registration and installation steps, and explicit verification boundaries. Package identity, version, manifests, skill behavior, and the historical installation record were unchanged. Desktop installation and discovery remain unverified and require a fresh desktop chat or app restart to check.

Repository verification: `python scripts/validate_package.py` and `git diff --check`. Work is isolated from the existing documentation branch in a separate worktree based on refreshed `origin/main`; integration is left for review.
