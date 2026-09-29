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

The repository is a Git-backed marketplace with one plugin entry. After obtaining GitHub access to the repository if required:

1. Add the marketplace: `codex plugin marketplace add YouMissedASpot/ymas-agent-workflows`.
2. In the Codex app, open the Plugins Directory, select **YouMissedASpot Workflows**, and install **ymas-agent-workflows**. In Codex CLI, open `/plugins` and install it there.
3. Start a new chat so the newly installed skills are discoverable. Invoke them by name when useful, such as `$project-bootstrap`, `$spec-driven-development`, `$audit-repair`, or `$bug-knowledge`.

If your Codex CLI does not expose `codex plugin marketplace`, update to a version that supports it or use the repository marketplace in the desktop app. Start a new chat after installation or refresh.

Marketplace registration and plugin installation were smoke-tested on Windows with `codex-cli 0.158.0` in a temporary `CODEX_HOME`. The installed `0.2.0` package contained all four skills and their supporting files. Skill invocation in a new chat and installation through the desktop app remain unverified. The machine's globally installed `codex-cli 0.101.0` still does not expose the marketplace command.

The official [plugin packaging and marketplace guide](https://developers.openai.com/plugins/build/plugins) documents the portable manifest and `codex plugin marketplace add` command. The [skill guide](https://developers.openai.com/plugins/build/skills) documents `SKILL.md` front matter and supporting resources.

For a repository that adopts these workflows, keep its local agent instructions concise: point to its own documentation standard and installed workflows. Make that repository's product and architecture authority explicit there. Do not copy the YMAS document families into an unrelated repository merely because the plugin is installed.

For substantive development work, the [agent execution loop](docs/workflows/agent_execution_loop.md) carries a task through verification and required durable updates; the [workbranch rule](docs/rules/multi_agent_workbranches.md) isolates repository writes. Installing the plugin makes the skills available. A repository adopting the YMAS workflow system must establish these defaults in its own agent instructions, using `project-bootstrap` to preserve equivalent or stronger existing governance and surface conflicts.

When consequential product or system rules are unresolved, [specification-driven development](docs/workflows/specification_driven_development.md) connects accepted product intent, system specifications, implementation review, verification, and any human acceptance gate. Small work with settled requirements stays in its focused workflow.

## Update and version

Edit the relevant skill and its supporting files, then run `python -m pip install -r requirements-dev.txt` and `python scripts/validate_package.py`. The check validates skill front matter, the portable manifest against its online schema, marketplace identity, index routes, and local Markdown links; GitHub Actions runs it on pushes and pull requests. Increment `plugin.json`'s semantic version for a distributable release and tag that commit. Users can refresh the Git marketplace with `codex plugin marketplace upgrade ymas-workflows` and reinstall or refresh the plugin in the app as needed; start a new chat to pick up changed instructions. The marketplace follows the repository's default branch, so tag and branch policies should be chosen deliberately before relying on a release snapshot.

## License

MIT. See [LICENSE](LICENSE).

## Credit

The execution loop was informed by the `loop-library` skill's guidance on triggers, verification, stopping conditions, and handoffs. Skill entrypoints were checked against the `skill-creator` skill. The operating rules here are adapted for YMAS.
