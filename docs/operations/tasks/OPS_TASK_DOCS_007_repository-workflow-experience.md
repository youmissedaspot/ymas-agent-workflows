# OPS_TASK_007 — Repository workflow experience

Status: Implementation complete; validation results recorded below. Not published.

## Accepted request and scope

Make ordinary YMAS work usable without memorizing skill names or filing rules. Add a read-only repository evaluation and an explicit documentation consolidation workflow while retaining a small always-on bootstrap and project-owned authority. Carry forward the user's pending audit target-selection rule verbatim. The existing `work/audit-target-selection` branch contains this continuing workflow work; no unrelated changes were present.

Inspected all four existing skill entrypoints, their templates, the index, documentation standard, manifest/catalog, installation validation, and recent history before edits. Existing naming history establishes canonical Level 2 retrieval tokens and family-wide IDs; valid legacy filenames and unrelated behavior remain intact. PR #5 is merged; its earlier task record's integration-pending statement is historical, not current status.

## Changes and activation boundaries

- `evaluate-repository`: bare invocation targets the current repository; assessment and recommendations only, with no file changes or inferred authority.
- `documentation-consolidation`: bare invocation explicitly requests preserve-mode migration of the current repository. Cleanup needs explicit user intent and preserved information, known authority, updated references, Git recovery, and no lost unique evidence. Ambiguous material stays.
- `project-bootstrap`: orientation supporting the current task and authorized foundation setup; no automatic adoption, migration, or takeover of routine tasks.
- `audit-repair`: target from the request or conversation; otherwise ask. Repository records and failing tests cannot independently supply intent.
- `bug-knowledge`: natural-language bug intake and requested investigation/knowledge work; existing project record systems remain authoritative and intake alone does not authorize repair.
- `spec-driven-development`: unresolved specification needs for a requested change, not routine already specified work or invented product rules.

The README adds normal-language examples and the supplied welcome message, including its final filing-cabinet line. It distinguishes verified installation from adoption and automatic selection from guaranteed execution. The welcome text is guidance, not an installer hook. The index, documentation standard, and adoption template route to the new skills without expanding `AGENTS.md`.

Prepared version `0.3.0` for the two additive workflows and changed descriptions. The portable format discovers `skills/` automatically; no marketplace identity or source change was required. The installation check now validates exact skill sets by package version: four for published `0.2.0`, six for candidate `0.3.0`. Unknown versions fail rather than silently weakening completeness checks.

## Validation and limits

Review scenarios: a bare evaluation stays read-only; a bare consolidation uses preserve mode; a tidy/consolidate request does not permit deletion; explicit cleanup still retains ambiguous/unique evidence; a bare audit with only a next-action record asks for a target; an audit following an established conversational concern uses that concern; natural bug language routes to intake; ordinary implementation uses only needed orientation. This is an instruction review, not an empirical claim about model compliance.

All six skills passed the skill-creator validator. Package validation passed for six front-matter blocks, 30 Markdown files, and 43 Markdown links, including manifest schema, marketplace identity, and index routes. The package-link regression test passed. On Windows with Codex CLI `0.159.1`, candidate `0.3.0` passed isolated installation, repeat installation, removal/reinstallation, and validation of all six skills; published `0.2.0` passed its four-skill contract plus marketplace refresh. The diff check passed. Reviewed descriptions and workflow bodies against the scenarios above, retained the audit target rule verbatim, and checked added content for personal paths, private data, and product-specific rules; none were introduced.

No installed plugin cache or other repository was migrated. Actual automatic selection and desktop discovery of the new version remain unverified; publication and client refresh are separate steps. Prior `0.2.0` hosted results do not establish macOS/Linux verification of `0.3.0`.

## Files changed

- `README.md`
- `INDEX.md`
- `plugin.json`
- `scripts/smoke_install.py`
- `skills/evaluate-repository/SKILL.md` (new)
- `skills/documentation-consolidation/SKILL.md` (new)
- `skills/project-bootstrap/SKILL.md`
- `skills/project-bootstrap/assets/documentation_standard_template.md`
- `skills/audit-repair/SKILL.md`
- `skills/bug-knowledge/SKILL.md`
- `skills/spec-driven-development/SKILL.md`
- `docs/OPS_WORKFLOW_001_documentation_standard.md`
- This task record.

`AGENTS.md`, marketplace metadata, and existing product/specification templates required no changes.
