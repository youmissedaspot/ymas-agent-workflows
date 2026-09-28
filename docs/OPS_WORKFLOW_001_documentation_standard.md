# OPS_WORKFLOW_001 — Documentation standard

Status: Current
Scope: This repository only. The reusable template in `skills/project-bootstrap/assets/` is adapted by an adopting project; this file does not govern other repositories.

## Locations and names

Markdown is permitted at repository root for `README.md`, `AGENTS.md`, `LICENSE` when applicable, and package-facing files; in `docs/` for numbered project records; and inside `skills/<skill>/` for `SKILL.md`, references, and output assets. Keep other documentation under a clearly named `docs/` functional directory. Do not scatter new Markdown at the root.

Numbered records use `<FAMILY>_<three-digit sequence>_<durable-slug>.md`. IDs are scoped to this project, never reused or renumbered, including after a move or archive. Each family has its own sequence. Inspect current and legacy locations before allocating the next number.

The standard families are `SOT_###`, `RM_###`, `SYS_###`, `SPEC_###`, `PLAN_###`, `AUDIT_###`, `ADR_###`, `BUG_###`, `OPS_TASK_###`, `OPS_STATE_###`, `OPS_NEXT_###`, `OPS_DECISION_###`, `OPS_SPECDEF_###`, `OPS_WORKFLOW_###`, and `REF_###`. Use a family only when the record has that purpose. In this package, `README.md`, `plugin.json`, and skill files are package artifacts rather than numbered project records.

## Operational memory

- `docs/operations/tasks/` — `OPS_TASK_###`, substantive completed work.
- `docs/operations/state/` — `OPS_STATE_###`, project-state snapshots.
- `docs/operations/next/` — `OPS_NEXT_###`, recommended next actions.
- `docs/operations/decisions/` — `OPS_DECISION_###`, durable operational decisions; supersession must be explicit.
- `docs/operations/specdef/` — `OPS_SPECDEF_###`, provisional specification work. Label observations, proposals, unresolved questions, and accepted working decisions; promote accepted product decisions to their authoritative owner.
- `docs/operations/workflows/` — additional `OPS_WORKFLOW_###` records. Keep this primary standard at `docs/OPS_WORKFLOW_001_documentation_standard.md`.

When these chronological families exist, the highest numbered `OPS_TASK`, `OPS_STATE`, and `OPS_NEXT` is respectively the latest task, current snapshot, and current next action. Read relevant records, including legacy locations during a migration. Create a new chronological record when it is needed to preserve a meaningful transition; do not generate all three mechanically for every edit.

## Authority

Repository `AGENTS.md` governs agent conduct here. This standard governs this repository's documentation. Root `plugin.json` defines package identity and declared components; each skill's `SKILL.md` defines that workflow. The README describes usage and installation. Accepted ADRs can govern technical decisions within their scope. Operational records, audits, tests, implementation, and Git history are context or evidence, not automatic authority over these contracts. An adopting repository supplies its own product and architecture authority; this package must not substitute for it.

Distinguish authority, implementation evidence, observation, inference, proposal, recommendation, unresolved question, and accepted decision in records and reports. When sources conflict, identify the conflict and its governing owner rather than inventing a resolution.

## Functional directories

Use `docs/engineering/bugs/` for `BUG_###` records and `docs/engineering/knowledge/` for generalized engineering `REF_###` records when those workflows are used in this repository. Other families belong in purpose-specific `docs/` directories chosen once and recorded here before use: `docs/sot/`, `docs/roadmap/`, `docs/systems/`, `docs/specifications/`, `docs/plans/`, `docs/audits/`, `docs/decisions/`, and `docs/references/`. Do not create empty directories merely to express this map.

## Creation, updates, and archives

Update an existing document when it owns the subject. Create a new ID only for a new durable identity, a required chronological record, or a distinct decision, specification, or workflow. Never duplicate a record because files moved. Prefer links over repeated rules.

Archive superseded material under a clearly marked `docs/archive/` path when useful history must remain. Preserve IDs, filenames, content history, and working links during moves; verify links and stale paths. Archived material must be marked historical and must not be cited as current authority.

At the end of substantive work, create or update only operational records that capture a material transition, decision, state, or next action. Report which records changed; if none were needed, say so.
