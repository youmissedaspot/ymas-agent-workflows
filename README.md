# YouMissedASpot Agent Workflows

A portable library of agent-readable engineering workflows, templates, and operational patterns for improving software development without replacing project-specific authority. It is distributed as an instruction-only Codex/OpenAI plugin and contains no MCP server.

The library has three layers: **skills** select and run workflows, **reusable operating files** hold templates and rules, and **repository guidance** explains how to use them under local authority. [`INDEX.md`](INDEX.md) routes agents to the smallest relevant set of files, so they can mine the library without reading it all.

Global `AGENTS.md` stays small so common invariants are always visible. These skills load their detailed procedures only when the task calls for them. Each adopting repository remains the source of truth for its own product, architecture, specifications, and authority hierarchy.

## Included skills

| Skill | Use it for |
| --- | --- |
| `project-bootstrap` | Orient in an unfamiliar repository; locate authority, current context, and documentation conventions. Adapt the YMAS documentation template only for a project adopting it. |
| `spec-driven-development` | Settle product and system requirements, architecture, and increment scope before planning and implementing consequential changes. |
| `audit-repair` | Audit requirements against implementation and repair a verified failure at the smallest supported scope. |
| `bug-knowledge` | Log natural-language bug reports, investigate prior failures, and distill recurring lessons into engineering references. |

The package has a portable root [`plugin.json`](plugin.json), four `skills/<name>/SKILL.md` entrypoints, and a repository [marketplace catalog](.agents/plugins/marketplace.json). Templates sit next to the skills that use them. [`AGENTS.md`](AGENTS.md) and the [documentation standard](docs/OPS_WORKFLOW_001_documentation_standard.md) govern this repository only.

## Install in Codex

The repository is a Git-backed marketplace with one plugin entry. Marketplace registration makes the package discoverable; installing the plugin is a separate step.

You need Git on `PATH`, network access to GitHub, and a Codex CLI with plugin commands. Check `git --version` before starting. The npm installation route below also requires Node.js and npm (`node --version` and `npm --version`). The public repository does not require collaborator access. You do not need to clone it, install Python, or configure an MCP server to use the plugin. Normal Codex sign-in is needed to use workflows in a model session.

1. Check the CLI version and required command:

   ```powershell
   codex --version
   codex plugin marketplace --help
   ```

   Codex CLI `0.101.0` does not support this command. For an npm-managed installation, upgrade with `npm install -g @openai/codex@0.159.1`, then repeat both checks. Version `0.159.1` is verified below, not a claim about the minimum supported or latest version. If installed through another package manager, update through that manager and verify command support.

   On Windows, if the old version still runs, use `Get-Command codex -All` and `where.exe codex` to identify which executable or wrapper wins on `PATH`. Update that installation or correct its precedence, reopen the terminal, and repeat the checks. The desktop app can bundle a different CLI version; updating it does not necessarily update the npm command your shell resolves.

2. Register the marketplace after obtaining GitHub access if required:

   ```powershell
   codex plugin marketplace add YouMissedASpot/ymas-agent-workflows
   codex plugin marketplace list
   ```

   Confirm that `ymas-workflows` appears. If already registered, refresh it with `codex plugin marketplace upgrade ymas-workflows`.

3. Install and verify the plugin:

   ```powershell
   codex plugin add ymas-agent-workflows@ymas-workflows
   codex plugin list --marketplace ymas-workflows
   ```

   Confirm `installed, enabled`. Alternatively, after registration, use the app's Plugins Directory, select **YouMissedASpot Workflows**, and install **ymas-agent-workflows**, or use `/plugins` in a supported CLI.

4. Start a new chat after installation or refresh. Confirm the available skills include `ymas-agent-workflows:project-bootstrap`, `ymas-agent-workflows:spec-driven-development`, `ymas-agent-workflows:audit-repair`, and `ymas-agent-workflows:bug-knowledge`. Use the plugin-qualified name when a standalone skill has the same name; existing standalone skills do not need to be removed.

   For a discovery-only check, ask: "From your available skills, list the four ymas-agent-workflows plugin skills and their installed paths. Do not execute a workflow or modify files." Successful installation means both an installed/enabled listing and discovery in the client where you intend to use the workflows.

### If installation fails

Stop at the failed step; an earlier successful step does not prove that later steps completed.

| Symptom | Recovery |
| --- | --- |
| `codex`, `npm`, or `git` is not found | Install the missing prerequisite through its normal installer/package manager, reopen the terminal, and repeat the version checks. |
| `plugin` or `marketplace` is unrecognized | Upgrade the CLI that the shell actually resolves. Use `Get-Command codex -All` / `where.exe codex` on Windows or `command -v codex` / `type -a codex` on macOS/Linux. Repeat the help check before registration. |
| PowerShell blocks the npm `.ps1` wrapper | Try `codex.cmd --version` and use `codex.cmd` for these commands; similarly use `npm.cmd` for the upgrade. Follow your organization's execution policy rather than disabling it globally. |
| GitHub connection, proxy, certificate, or clone failure | Check `git ls-remote https://github.com/YouMissedASpot/ymas-agent-workflows.git HEAD`. Resolve the reported Git/network problem, then retry the failed registration or installation step. Do not disable TLS verification. |
| Marketplace already exists | Check `codex plugin marketplace list`, then run `codex plugin marketplace upgrade ymas-workflows` and continue to installation. If the existing entry points somewhere else, inspect it before changing it. |
| Marketplace exists but plugin is absent | Run the separate `codex plugin add ymas-agent-workflows@ymas-workflows` step, then check the marketplace-filtered plugin listing. |
| Plugin is installed but skills are missing | Start a fresh chat in the intended client; restart the desktop app if needed. Check whether the CLI and app use different Codex homes or project settings. An isolated test home does not install into your usual home. Capture the exact version, client, error, and failing step in a [GitHub issue](https://github.com/youmissedaspot/ymas-agent-workflows/issues) if it persists; omit credentials and private configuration. |

To retry an incomplete or damaged installation, refresh the marketplace and rerun `codex plugin add ymas-agent-workflows@ymas-workflows`. To uninstall only this plugin, run `codex plugin remove ymas-agent-workflows@ymas-workflows`; optionally remove its catalog with `codex plugin marketplace remove ymas-workflows`. Do not delete your Codex home or unrelated skills/plugins.

### Verification status

On September 29, 2026, the Windows npm CLI was upgraded from `0.101.0` to `0.159.1`. Marketplace registration and installation of plugin `0.2.0` succeeded in the actual user Codex home. The installed package passed validation, and a fresh read-only CLI session discovered all four plugin skills from their installed cache paths. This verifies installation and skill discovery, not execution of each workflow. Desktop installation and discovery remain unverified; start a new desktop chat and, if necessary, restart the app before checking its skill list. The earlier isolated `0.158.0` smoke test remains documented in its [historical task record](docs/operations/tasks/OPS_TASK_004_package_validation_and_installation_smoke.md).

The official [plugin packaging and marketplace guide](https://developers.openai.com/plugins/build/plugins) documents the portable manifest and `codex plugin marketplace add` command. The [skill guide](https://developers.openai.com/plugins/build/skills) documents `SKILL.md` front matter and supporting resources.

For a repository that adopts these workflows, keep its local agent instructions concise: point to its own documentation standard and installed workflows. Make that repository's product and architecture authority explicit there. Do not copy the YMAS document families into an unrelated repository merely because the plugin is installed.

YMAS numbered documents use `<FAMILY>_<L2_CATEGORY>_<ID>_<l3-description>.md`: underscores separate the structural segments, and lowercase words in the final description use hyphens. The adopting repository defines its own durable Level 2 categories and reuses one canonical token per concept across families, so a search such as `_STORAGE_` retrieves that area's tasks, bugs, audits, and references. Each family keeps one three-digit sequence across categories. Existing numbered files without Level 2 remain valid legacy records and are not renamed automatically. The [documentation standard template](skills/project-bootstrap/assets/documentation_standard_template.md) gives adoption guidance.

For substantive development work, the [agent execution loop](docs/workflows/agent_execution_loop.md) carries a task through verification and required durable updates; the [workbranch rule](docs/rules/multi_agent_workbranches.md) isolates repository writes. Installing the plugin makes the skills available. A repository adopting the YMAS workflow system must establish these defaults in its own agent instructions, using `project-bootstrap` to preserve equivalent or stronger existing governance and surface conflicts.

When consequential product or system rules are unresolved, [specification-driven development](docs/workflows/specification_driven_development.md) connects accepted product intent, system specifications, implementation review, verification, and any human acceptance gate. Small work with settled requirements stays in its focused workflow.

## Update and version

Edit the relevant skill and its supporting files, then run `python -m pip install -r requirements-dev.txt` and `python scripts/validate_package.py`. The check validates skill front matter, the portable manifest against its online schema, marketplace identity, index routes, and local Markdown links; GitHub Actions runs it on pushes and pull requests. Increment `plugin.json`'s semantic version for a distributable release and tag that commit. Users can refresh the Git marketplace with `codex plugin marketplace upgrade ymas-workflows` and reinstall or refresh the plugin in the app as needed; start a new chat to pick up changed instructions. The marketplace follows the repository's default branch, so tag and branch policies should be chosen deliberately before relying on a release snapshot.

Installation is part of the package's usability contract. Maintainers must also run `python scripts/smoke_install.py --source checkout` to test the candidate package and `python scripts/smoke_install.py --source published` to test the public GitHub installation route. Each uses a disposable Codex home, checks all four installed skills and their package links, repeats installation, and verifies removal/reinstallation. The published-source check also exercises marketplace refresh. These checks require network access and the validation dependencies, but no model session or API key. They do not change the user's Codex home.

CI defines these installation checks for Windows, macOS, and Linux with Codex CLI `0.159.1`. A configured CI job is not a passing result: inspect each platform's run before claiming support. Windows, macOS, and Linux checks passed on September 29, 2026 ([CI run](https://github.com/youmissedaspot/ymas-agent-workflows/actions/runs/36633783998)). Desktop discovery remains unverified. These tests cannot guarantee every proxy, filesystem policy, future CLI version, or client configuration; report each failure at its actual step and keep recovery guidance current.

## License

MIT. See [LICENSE](LICENSE).

## Credit

The execution loop was informed by the `loop-library` skill's guidance on triggers, verification, stopping conditions, and handoffs. Skill entrypoints were checked against the `skill-creator` skill. The operating rules here are adapted for YMAS.
