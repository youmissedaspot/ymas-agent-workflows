# OPS_WORKFLOW_001 — Documentation standard

Status: Draft until the project's authority owners and directories are confirmed.

Adapt this template to the adopting YMAS project. Preserve existing rules and document IDs. Remove instructions and examples that do not fit the project. This template has no authority in a repository until adopted there.

## Scope and permitted Markdown locations

Name the permitted root Markdown files, functional directories, and any exceptions. Keep the primary standard at `docs/OPS_WORKFLOW_001_documentation_standard.md`. Keep repository instructions at root `AGENTS.md` or the repository's established equivalent. Use purpose-specific directories under `docs/` rather than scattering files.

## Document IDs and naming

Use `<FAMILY>_<three-digit sequence>_<durable-slug>.md` for numbered documents. IDs are project-scoped, never reused or renumbered, even after archiving or moving. Every family has an independent sequence. Find the highest ID across current and legacy locations before allocating a new one. A move does not restart numbering.

Adopt only the families the project actually needs: `SOT_###` (product source of truth), `RM_###` (roadmap), `SYS_###` (systems), `SPEC_###` (specifications), `PLAN_###` (plans), `AUDIT_###` (audits), `ADR_###` (architecture decisions), `BUG_###` (individual bugs), `OPS_TASK_###` (completed tasks), `OPS_STATE_###` (state snapshots), `OPS_NEXT_###` (next actions), `OPS_DECISION_###` (operational decisions), `OPS_SPECDEF_###` (provisional specification work), `OPS_WORKFLOW_###` (workflows), and `REF_###` (references).

## Operational memory and workflow discovery

- `docs/operations/tasks/` — `OPS_TASK_###` substantive completed work.
- `docs/operations/state/` — `OPS_STATE_###` current project-state snapshots.
- `docs/operations/next/` — `OPS_NEXT_###` current recommended next actions.
- `docs/operations/decisions/` — `OPS_DECISION_###` durable operational decisions; explicit supersession only.
- `docs/operations/specdef/` — `OPS_SPECDEF_###` provisional design, research, observations, proposals, open questions, and accepted working decisions awaiting promotion. Label their status. They do not amend canonical product authority.
- `docs/operations/workflows/` — additional `OPS_WORKFLOW_###` records. Keep the primary standard at `docs/OPS_WORKFLOW_001_documentation_standard.md`.

When present, the highest numbered `OPS_TASK`, `OPS_STATE`, and `OPS_NEXT` is respectively the latest task, current snapshot, and current next action. Find relevant records in legacy locations during migrations. Operational records are context and evidence, not product authority. Discover specialized workflows through the repository's instructions and installed skills; load only those relevant to the task.

## Authority hierarchy — project owner must complete

List this project's current product, architecture, specification, and decision authorities in their real precedence order, with exact paths or discovery rules. State who resolves conflicts. Do not fill this section by guessing from filenames, Git history, or implementation. Until completed, record authority as unresolved and seek the actual governing source before changing contested behavior.

Distinguish authority, implementation evidence, observation, inference, proposal, recommendation, unresolved question, and accepted decision. Implementation, tests, operational memory, bug records, and historical documents do not automatically override current approved authority.

## Functional documentation directories

Map each adopted family to its actual directory. Recommended when applicable: `docs/sot/`, `docs/roadmap/`, `docs/systems/`, `docs/specifications/`, `docs/plans/`, `docs/audits/`, `docs/decisions/`, `docs/references/`, `docs/engineering/bugs/` for `BUG_###`, and `docs/engineering/knowledge/` for generalized `REF_###`. Do not create empty directories or relocate existing files merely to match these examples.

## Creation, updates, and archival

Update an existing owner before creating a duplicate. Create a new ID for a new durable identity, a needed chronological record, or a distinct specification, decision, or workflow. Prefer references over copied rules. Archive useful superseded material with an explicit historical label; preserve its ID, filename, history, and links. Archived records do not regain current authority. Validate links and stale paths after moves.

At task completion, update only operational records needed to capture a material transition, state, decision, or next action, and report which changed.
