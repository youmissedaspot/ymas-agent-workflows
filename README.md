# YouMissedASpot Agent Workflows

YMAS is a portable agent harness for engineering work. Its skills, templates and operating rules help agents specify, implement, verify and document changes under each repository's own authority. It ships as an instruction-only Codex/OpenAI plugin and has no MCP server.

The harness uses skills to select and run workflows, operating guides to hold reusable templates and rules, and repository guidance to apply them under local authority. [`INDEX.md`](INDEX.md) points agents to the files needed for the task.

Keep always-on `AGENTS.md` instructions short and load detailed procedures through the relevant skills. The adopting repository governs its own product, architecture, specifications and authority hierarchy.

## Work normally

Install YMAS once, then tell the agent what you need. You do not need to memorize skill names, document families, IDs, or filing rules for ordinary work in a repository that uses YMAS.

- "I found a bug. Log it."
- "Audit the authentication flow against the spec."
- "Update the API behavior we discussed."
- "What's the current state of this project?"

Codex can select a skill from its description. Selection depends on the client, enabled skills and conversation, so some requests need an explicit workflow name. The agent records work under the repository's adopted instructions. See the [official skill guidance](https://developers.openai.com/plugins/build/skills).

Installing the plugin makes its workflows available and leaves repository files unchanged. For an existing project, ask "Evaluate this repository's documentation and how it fits YMAS" for an assessment without changes. When ready to adopt it, ask "Consolidate this repository's documentation into YMAS, preserving its history." For a new project, ask the agent to establish a documentation foundation. The agent adapts it to existing rules and keeps always-on instructions short.

## Begin or resume a project

Ask “How do I start with YMAS?” for [workflow-orientation](skills/workflow-orientation/SKILL.md). It explains where to begin or resume and suggests a relevant next prompt. The informal `/start` name is not a registered slash-command alias; orientation does not orchestrate execution. Then describe the work you want done. For an existing project, the agent inspects its current stage before continuing.

**Discuss → True Spec Worksheet → Decide → SPEC and/or SPECARC → systems.md → Plan → Implement → Verify → Human Acceptance where applicable**

The [worksheet skill](skills/true-spec-worksheet/SKILL.md) explores consequential choices that remain unresolved. It records questions, recommendations, alternatives, reasoning and consequences for the decision owner. Its output is provisional source material. The project's acceptance process governs which decisions can enter authoritative specifications.

Accepted SPEC defines what must be true for a product or system. Accepted SPECARC defines its architecture for a durable concern. Either can come first. `systems.md` relates the complete current specification set once it can support a useful map. ADR records a specific decision's context and rationale; SYS retains the adopting project's system-documentation role. The project controls approval and precedence. Small or already-specified work skips unnecessary stages.

Examples: “I have an idea for an economic simulation”; “Help me figure out how shipping contracts should work”; “We need to define the architecture for event reconciliation”; “These decisions are settled; turn them into specifications”; “Update the architecture map from the current specifications.”

## Included skills

| Skill | Use it for |
| --- | --- |
| `workflow-orientation` | Explain how to start or resume YMAS; orientation only. |
| `like-im-5` | Explain an unfamiliar technical, architectural, domain or project concept in clear adult language, using actual repository evidence where available. |
| `true-spec-worksheet` | Prepare a provisional decision worksheet before formal specifications. |
| `project-bootstrap` | Understand repository context and establish a foundation when authorized, then return to the task. |
| `evaluate-repository` | Assess the current repository's documentation, authority, and YMAS fit without changing files. Bare invocation is valid. |
| `documentation-consolidation` | Explicitly migrate existing documentation. Bare invocation uses the current repository and preserves information; deletion requires an explicit cleanup request. |
| `spec-driven-development` | Settle product and system requirements, architecture, and increment scope before planning and implementing consequential changes. |
| `audit-repair` | Audit or repair the target you named or established in conversation. Without a target it asks for one; it cannot pick work from repository state. |
| `bug-knowledge` | Log natural-language bug reports, investigate prior failures, and distill recurring lessons into engineering references. |

[`plugin.json`](plugin.json) declares the portable package. Candidate `0.5.1` has nine `skills/<name>/SKILL.md` entrypoints and a repository [marketplace catalog](.agents/plugins/marketplace.json). Each skill keeps its templates nearby. [`AGENTS.md`](AGENTS.md) and the [documentation standard](docs/OPS_WORKFLOW_001_documentation_standard.md) govern this repository only.

The audit-repair update supports an explicitly requested whole-project audit, comparison
of supplied reports under selected precedence, consequence separate from evidence
confidence, and regression closure against the original failure. Its optional
[assessment guidance](skills/audit-repair/references/audit_assessment.md) follows each
project's accepted rules. Six neutral fixtures exercise known-good, defect, fixture,
report-comparison, original-closure and stale-evidence cases. See the
[release preparation record](docs/operations/tasks/OPS_TASK_DOCS_018_audit-release-preparation.md)
for the candidate's scope and remaining gates.

## Install in Codex

The repository is a Git-backed marketplace with one plugin entry. Marketplace registration makes the package discoverable; installing the plugin is a separate step.

You need Git on `PATH`, network access to GitHub, and a Codex CLI with plugin commands. Check `git --version` before starting. The npm installation route below also requires Node.js and npm (`node --version` and `npm --version`). The public repository does not require collaborator access. You do not need to clone it, install Python, or configure an MCP server to use the plugin. Normal Codex sign-in is needed to use workflows in a model session.

1. Check the CLI version and required command:

   ```powershell
   codex --version
   codex plugin marketplace --help
   ```

   Codex CLI `0.101.0` does not support this command. For an npm-managed installation, upgrade with `npm install -g @openai/codex@0.159.1`, then repeat both checks. The checks below used `0.159.1`; they do not establish the minimum supported or latest version. For another installation method, update through its package manager and verify command support.

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

4. Start a new chat after installation or refresh. For candidate `0.5.1`, confirm all nine skills in the table above are available with the `ymas-agent-workflows:` prefix. Use the plugin-qualified name when a standalone skill has the same name; existing standalone skills do not need to be removed.

   `0.4.0` and the retained `0.4.1` checkpoint have eight entrypoints and exclude `like-im-5`. `0.3.0` has six skills and excludes orientation and worksheet; `0.2.0` has four and also excludes evaluation/consolidation. A version and skill-name match alone does not identify installed bytes.

   `0.5.0` was integrated through [PR14](https://github.com/youmissedaspot/ymas-agent-workflows/pull/14). Its [main-source CI](https://github.com/youmissedaspot/ymas-agent-workflows/actions/runs/37479242824) records package and installation checks for that source; it does not establish authenticated client discovery or validate this candidate. `0.5.1` remains a release candidate until its own required checks and authenticated discovery pass. Refresh the normal installation only after authorized, verified integration and release.

   For a discovery-only check, ask: "From your available skills, list the ymas-agent-workflows plugin skills and their installed paths. Do not execute a workflow or modify files." Successful installation means both an installed/enabled listing and discovery in the client where you intend to use the workflows.

### Once installation is verified

After verifying installation and discovery, the agent can use this welcome message. It is documented guidance, not an automatic installer hook:

> YMAS Workflows installed.
>
> Tell the agent what you want done, report a bug or ask for an audit. You do not need to remember skill names or filing rules.
>
> In a repository that adopts YMAS, the agent follows its rules for documentation, operational records, bug records, IDs, categories and project memory.
>
> Explicit skill commands are still available when you want a specific workflow on demand.
>
> If this repository already contains documentation, you can also run the repository evaluation workflow to see how the current project maps into YMAS before changing anything.
>
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

On October 2, 2026, candidate `0.4.0` passed the disposable-home checkout installation checks on Windows with CLI `0.159.1`: all eight skills, package validation, repeat installation, and removal/reinstallation. The published `0.3.0` route separately passed its six-skill installation, marketplace refresh, and recovery checks. These results verify packaged/installed files, not live agent execution, desktop discovery, automatic selection, or cross-platform candidate CI. See the [workflow task record](docs/operations/tasks/OPS_TASK_DOCS_010_product-definition-and-architecture-workflow.md).

On October 6, 2026, source checkpoint `2165f1d42d62e1cf7ffb241c6608f3ce1de434e2`, still labeled `0.4.0`, passed all 24 deterministic regression methods and disposable checkout/public installation checks. Its [PR CI](https://github.com/youmissedaspot/ymas-agent-workflows/actions/runs/37407895011) passed package validation and installation on Linux, Windows and macOS; the CI preview tree matched that reviewed checkpoint. These results belong to that exact source and do not establish `0.4.1` verification. The fresh discovery-only CLI attempt was unauthenticated and returned HTTP 401, so no skill-catalog response was obtained. Installation/listing success is not live discovery. No user installation was updated.

The retained `0.4.1` checkpoint prepared distribution of the source-evidence and verification improvements with the same eight entrypoints. It is included in the combined `0.5.0` candidate. The [release-preparation record](docs/operations/tasks/OPS_TASK_DOCS_013_release-version-and-evidence.md) preserves its history.

On October 6, combined `0.5.0` checkpoint `ebae6ffbe9f5f81cca4531e0833f1a64fb2b0c2d` passed 45 deterministic tests, package validation and installation checks. Its [PR CI](https://github.com/youmissedaspot/ymas-agent-workflows/actions/runs/37419555934) passed package validation and checkout/public installation on Linux, Windows and macOS. The Windows checkout test compared all 99 tracked files with installed bytes. The public route separately tested the existing `0.4.0` release. These results identify that exact checkpoint; later changes need their own evidence. Authenticated nine-skill discovery remains pending. Automatic selection, real compaction recovery, desktop discovery and token/quota savings remain unverified.

## Repository adoption

Evaluation is read-only, including bare `$evaluate-repository`. Consolidation is a requested migration: bare `$documentation-consolidation` defaults to preserve mode. Preserve mode retains information, establishes clear current owners, and archives superseded material where appropriate. `$documentation-consolidation cleanup`, or a clear natural-language request to remove superseded material, enables deletion only after information is preserved, authority is understood, references are updated, and Git recovery is established. Ambiguous or uniquely historical material stays.

When a repository adopts YMAS, its local agent instructions should name its product and architecture authority and point to its documentation standard and installed workflows. Keep those instructions concise. Plugin installation alone does not authorize adopting the YMAS document families.

By default, YMAS numbered documents use `<FAMILY>_<L2_CATEGORY>_<ID>_<l3-description>.md`: underscores separate the structural segments, and lowercase words in the final description use hyphens. The adopting repository defines its own durable Level 2 categories and reuses one canonical token per concept across families, so a search such as `_STORAGE_` retrieves that area's tasks, bugs, audits, and references. Each family keeps one three-digit sequence across categories. Existing numbered files without Level 2 remain valid legacy records and are not renamed automatically. The [documentation standard template](skills/project-bootstrap/assets/documentation_standard_template.md) gives adoption guidance.

`OPS_NEXT` alone uses `OPS_NEXT_<ID>_<L2_CATEGORY>_<l3-description>.md`, such as `OPS_NEXT_005_DOCS_update-installation-guidance.md`. Most families optimize domain retrieval; next-action records optimize chronological sorting while retaining searchable Level 2 categories. The highest numeric family-wide ID identifies the current recommended next action unless project authority says otherwise. Never normalize this exception back to category-first order or renumber historical records.

Document sequence IDs are not versions. [Document versions](docs/workflows/document_versioning.md) use `v1`, `v2`, `v3`, and minor revisions such as `v3.1`. A revised document keeps its ID, current folder, and stable filename with updated version metadata; its complete predecessor moves to the archive with its old version recorded. Metadata uses `Version: v3.1`; filenames encode it as `v3dot1`, such as `SPECARC_EVENTS_001_event-reconciliation_v3dot1.md`. The logical family ID remains unchanged. Current links keep pointing to the current path.

The [agent execution loop](docs/workflows/agent_execution_loop.md) carries substantive work through verification and required durable updates. The [workbranch rule](docs/rules/multi_agent_workbranches.md) isolates repository writes. An adopting repository must establish these defaults in its own agent instructions. Use `project-bootstrap` to preserve equivalent or stronger existing rules and identify conflicts.

Use [specification-driven development](docs/workflows/specification_driven_development.md) when consequential product or system rules remain unresolved. It carries accepted product intent through system specifications, implementation review, verification and any required human acceptance. Small work with settled requirements stays in its focused workflow.

Accepted True Spec decisions become SPEC and/or SPECARC, then inform `systems.md`. SPECARC can precede surrounding product specifications or a complete map. After creating or substantively revising SPEC/SPECARC, review the complete current set. Update `systems.md` when architecture, ownership, boundaries, dependencies, interfaces, flows or cross-system behavior change. Record specification versions and acceptance status, preserve settled higher product decisions, and return consequential integration gaps to their owners. Defer a map while the specifications cannot support a useful one. Keep an accurate existing map without a mechanical version bump.

## Human understanding

Before substantial specification, architecture or implementation, use the
[Understanding Check](docs/workflows/human_understanding.md#understanding-check) to explain
the problem, affected behavior, governing authority, constraints and unresolved conflicts.
Keep it concise; it introduces no report template or approval gate. **Teach for human
understanding. Trace for evidence.** The shared [editorial guidance](docs/workflows/human_understanding.md)
asks for clear explanations and readable documentation, judged in context without word bans.

Use `$like-im-5` or the qualified `ymas-agent-workflows:like-im-5` skill to explain an
unfamiliar concept in adult language. `/like-im-5` is an informal spelling; command
presentation and automatic discovery depend on the client and need verification.
An explanation request alone does not authorize file changes. The skill explains the
repository's actual behavior and evidence, including gaps or conflicts, without inventing
a missing implementation.

The [specification workflow](docs/workflows/specification_driven_development.md) keeps
thick definitions authoritative, uses probes for material empirical uncertainty, and
stops expansion immediately when implementation reveals an architectural discrepancy.
The three-failed-attempt repair ceiling remains in force. Decision worksheets compare
credible alternatives and evidence that could overturn a consequential recommendation.

The combined candidate includes verification addition `69bb414e5ae2ca10ed617d7f358d4e4b98627470`
and PR13 checkpoint `cd41c538e153e293e728932bd9804e2effb93c86`. Authenticated discovery
remains a release gate; the guidance itself grants no publication or installation authority.
See the [task record](docs/operations/tasks/OPS_TASK_DOCS_015_human-understanding.md).

## Source evidence and behavioral checks

Bind tests and reviews to exact source through [source receipts](docs/workflows/source_receipts.md), and record blocked, superseded or integrated status there. [Task context](docs/workflows/task_context.md) preserves authority, dependencies, resume invariants and project-selected model/skill preferences. It does not replace full specification review. [Boundary verification](docs/workflows/verification_boundaries.md) checks affected caller lifecycles and failure classes. Use existing document owners for this evidence; no new record families are required.

Run `python scripts/diagnose_documents.py .` to inspect adopted YMAS IDs, current paths and edition metadata without changes. Configure the repository's archive directories and assess warnings under its rules. The diagnostic does not rename records, validate semantic authority or reserve IDs across branches. Package link checks cover common Markdown heading anchors; inspect complex renderer-specific syntax separately.

The [bounded behavioral cases](docs/workflows/behavioral_checks.md) and outcome grader use positive and negative controls. Run `python -m unittest discover -s scripts -p "test_*.py"` for deterministic regressions, including exact copied-package identity. Synthetic fixtures test the diagnostics and graders; they do not establish agent efficacy. Actual replays need independently inspected traces and filesystem effects. Automatic client selection remains unproved.

[Optional concept-to-source navigation](docs/workflows/source_navigation.md) uses existing indexes to locate relevant candidates, scoped identities and aliases, with freshness checks. It adds no retrieval service or mandatory graph.

Checkout installation smoke checks now compare every tracked candidate file against installed raw bytes. They require a clean committed source; a manifest version or skill-name match alone is insufficient. Existing installation evidence above remains historical; candidate changes need fresh checks within the authorized installation scope before release.

## Update and version

After editing a skill or its supporting files, run `python -m pip install -r requirements-dev.txt` and `python scripts/validate_package.py`. Validation checks skill front matter, the portable manifest's online schema, marketplace identity, index routes and local Markdown links. GitHub Actions runs it on pushes and pull requests.

Increment `plugin.json`'s semantic version for a distributable release and tag the verified release commit after the required gates pass. Users can refresh the marketplace with `codex plugin marketplace upgrade ymas-workflows`, then reinstall or refresh the plugin in the app and start a new chat to load changed instructions. The marketplace follows the repository's default branch; choose tag and branch policies before relying on a release snapshot.

A merge to main changes what users obtain from the catalog, even before a release announcement. Put the version bump in the final candidate before merging. A version change needs its own source identity, affected validation and review, and installation evidence. Preserve earlier checkpoint receipts and keep discovery blockers visible. An installed listing or a tag cannot substitute for authenticated discovery.

Installation is part of the package's usability contract. Maintainers must also run `python scripts/smoke_install.py --source checkout` to test the candidate package and `python scripts/smoke_install.py --source published` to test the public GitHub installation route. Each uses a disposable Codex home, checks the complete skill set for the installed version and its package links, repeats installation, and verifies removal/reinstallation. The checkout check also requires the candidate version; the public check accepts the documented older release until the new version is published. The published-source check also exercises marketplace refresh. These checks require network access and the validation dependencies, but no model session or API key. They do not change the user's Codex home.

CI runs these installation checks on Windows, macOS and Linux with Codex CLI `0.159.1`. Inspect every platform's result for the exact candidate before claiming support. Version `0.2.0` passed all three platforms on September 29, 2026 ([CI run](https://github.com/youmissedaspot/ymas-agent-workflows/actions/runs/36633783998)). Historical results do not establish coverage for later source; retain each candidate's final-source CI evidence separately.

Desktop discovery of the new skills and their automatic selection remain unverified. Installation tests do not cover every proxy, filesystem policy, future CLI version or client configuration. Report a failure at its actual step and update the recovery guidance when needed.

## License

MIT. See [LICENSE](LICENSE).

## Credit

The execution loop draws on `loop-library` guidance for triggers, verification, stopping conditions and handoffs. Skill entrypoints were checked against `skill-creator`. The operating rules are adapted for YMAS.
