# OPS_WORKFLOW_001 — Documentation standard

Status: Current
Version: v3.1
Previous version: [v3](archive/OPS_WORKFLOW_001_documentation_standard_v3.md)
Change summary: Add collision-aware allocation and receipt-linked integration closeout.
Scope: This repository only. The reusable template in `skills/project-bootstrap/assets/` is adapted by an adopting project; this file does not govern other repositories.

## Locations and names

Markdown is permitted at repository root for `README.md`, `AGENTS.md`, `INDEX.md`, `LICENSE` when applicable, and package-facing files; in `docs/` for numbered project records; and inside `skills/<skill>/` for `SKILL.md`, references, and output assets. Keep other documentation under a clearly named `docs/` functional directory. Do not scatter new Markdown at the root.

By default, new numbered records use `<FAMILY>_<L2_CATEGORY>_<ID>_<l3-description>.md`, in that order. `FAMILY` names the record type and may itself contain an underscore, as in `OPS_TASK`. The actual Level 2 value is one uppercase token without internal underscores. `ID` is a zero-padded three-digit number. The final description uses short, durable lowercase words separated by hyphens. Underscores separate the structural segments; do not use them inside the final description. Level 2 names the enduring domain, system, capability, or technical area that owns the record.

`OPS_NEXT` is the one intentional retrieval-order exception: use `OPS_NEXT_<ID>_<L2_CATEGORY>_<l3-description>.md`, for example `OPS_NEXT_005_DOCS_update-installation-guidance.md`, not `OPS_NEXT_DOCS_005_update-installation-guidance.md`. Most families put Level 2 first for domain retrieval; `OPS_NEXT` puts the zero-padded numeric sequence first so alphabetical sorting places the highest sequence at the bottom for current-action retrieval. Both retain Level 2: searching `_DOCS_` still finds documentation-domain records across families. Do not normalize `OPS_NEXT` back to the default ordering or introduce another family-specific exception without a similarly clear retrieval reason.

`OPS_NEXT` keeps one family-wide sequence across all categories. Never restart numbering when Level 2 changes, create per-category sequences, reuse an ID, or renumber an existing record. The highest numeric `OPS_NEXT` ID is the current recommended next action unless project authority explicitly establishes otherwise. Inspect current, archived, and legacy locations during migrations; alphabetical Level 2 grouping does not establish recency. Preserve historical filenames unless an explicitly scoped migration includes filename normalization.

This repository uses `DOCS` for documentation governance. Level 2 is controlled retrieval vocabulary: use one canonical token per concept across document families. Searching `_DOCS_` should find documentation records regardless of family, while `OPS_TASK_` finds all task records, `BUG_` finds all bug records, and a durable term in the final description finds a specific subject. Keep the vocabulary small, broad enough to remain durable, and mutually distinguishable where practical. Do not fragment a concept across synonyms, plural variants, unnecessary abbreviations, spelling variants, overlapping names, or narrower labels unless this project's taxonomy explicitly distinguishes those concepts. Before adding a category, inspect adopted categories and existing filenames, prefer an established owner, and add a term only for a durable distinction. Record its meaning and any legacy aliases in this local standard without automatically renaming records. Flag unclear ownership instead of inventing a term. This local classification does not govern adopting repositories.

Level 2 must not use roadmap, milestone, phase, sprint, release, campaign, or other temporary planning identifiers. Those identifiers may still appear in roadmap-owned and other planning documents, commits, pull requests, changelogs, and explanatory historical notes where this project's governance permits them; they must not become durable Level 2 vocabulary for unrelated records.

Each family has one independent sequence across all its Level 2 categories. The logical record ID remains `<FAMILY>_<ID>`; Level 2 classifies the filename without changing that ID. If `AGENT` is later adopted, `OPS_TASK_DOCS_005_level-2-record-naming.md` and `OPS_TASK_AGENT_006_agent-instruction-update.md` would continue the same `OPS_TASK` sequence. IDs are never reused or renumbered, including after a move or archive. Inspect current, archived, and legacy locations across all categories before allocating the next family ID. Existing filenames without Level 2 remain valid legacy names; rename them only in an intentional migration that preserves IDs, Git history, and links.

The standard families are `SOT`, `RM`, `SYS`, `SPEC`, `SPECARC`, `PLAN`, `AUDIT`, `ADR`, `BUG`, `OPS_TASK`, `OPS_STATE`, `OPS_NEXT`, `OPS_DECISION`, `OPS_SPECDEF`, `OPS_WORKFLOW`, and `REF`. Use a family only when the record has that purpose. In this package, `README.md`, `plugin.json`, and skill files are package artifacts rather than numbered project records.

SPEC defines what must be true for a product/system; SPECARC defines accepted architecture for a durable concern. They are sibling specification types without a fixed design order. ADR records a specific architectural decision and its context/rationale, supporting but not automatically replacing SPECARC. SYS retains its adopted system-level documentation role. `systems.md` integrates the complete current specification set once that set supports a useful map. Worksheet output is provisional source material, not product authority. The adopting project owns acceptance and precedence; a family prefix alone grants no authority.

Coordinate new family-ID reservations across active workers and recheck collisions before integration; see [document versioning](workflows/document_versioning.md#identity-and-revision). [Read-only document diagnostics](../scripts/diagnose_documents.py) report current-owner collisions and edition metadata. They preserve legitimate archive editions and do not repair or normalize files.

## Operational memory

- `docs/operations/tasks/` — `OPS_TASK` records of substantive completed work.
- `docs/operations/state/` — `OPS_STATE` project-state snapshots.
- `docs/operations/next/` — `OPS_NEXT` recommended next actions.
- `docs/operations/decisions/` — `OPS_DECISION` durable operational decisions; supersession must be explicit.
- `docs/operations/specdef/` — `OPS_SPECDEF` provisional specification work. Label observations, proposals, unresolved questions, and accepted working decisions; promote accepted product decisions to their authoritative owner.
- `docs/operations/workflows/` — additional `OPS_WORKFLOW` records. Keep this primary standard at its existing legacy path, `docs/OPS_WORKFLOW_001_documentation_standard.md`.

When these chronological families exist, the highest numbered `OPS_TASK`, `OPS_STATE`, and `OPS_NEXT` is respectively the latest task, current snapshot, and current next action. Read relevant records, including legacy locations during a migration. Create a new chronological record when it is needed to preserve a meaningful transition; do not generate all three mechanically for every edit.

After a material integration, the owning coordinator reconciles current state and the next action with live source, linking their small deltas to [one detailed source receipt](workflows/source_receipts.md). Preserve historical pre-integration task claims; do not copy the complete verification narrative into every family.

## Authority

Repository `AGENTS.md` governs agent conduct here. This standard governs this repository's documentation. Root `plugin.json` defines package identity and declared components; each skill's `SKILL.md` defines that workflow. The README describes usage and installation. Accepted ADRs can govern technical decisions within their scope. Operational records, audits, tests, implementation, and Git history are context or evidence, not automatic authority over these contracts. An adopting repository supplies its own product and architecture authority; this package must not substitute for it.

Distinguish authority, implementation evidence, observation, inference, proposal, recommendation, unresolved question, and accepted decision in records and reports. When sources conflict, identify the conflict and its governing owner rather than inventing a resolution.

## Repository workflow boundaries

Use the index to discover specialized procedures; do not expand always-on instructions with their full contents. Repository evaluation is read-only and returns its assessment in conversation unless a separate write is requested. Documentation consolidation is an explicitly requested migration, with preservation as the default and destructive cleanup requiring explicit intent. Follow the respective skill's authority and information-preservation checks. Ordinary work uses relevant workflows under these project rules without requiring users to choose IDs, categories, or skill commands; repository state alone does not authorize an audit target or a migration.

## Functional directories

Use `docs/engineering/bugs/` for `BUG` records and `docs/engineering/knowledge/` for generalized engineering `REF` records when those workflows are used in this repository. Other families belong in purpose-specific `docs/` directories chosen once and recorded here before use: `docs/sot/`, `docs/roadmap/`, `docs/systems/`, `docs/specifications/`, `docs/plans/`, `docs/audits/`, `docs/decisions/`, and `docs/references/`. Use `docs/specifications/` for SPEC and SPECARC when adopted here; no architecture-specification directory is required merely to add the family. A new integrated map defaults to `docs/systems/systems.md`; preserve an established owner and any existing SYS ID instead of assigning a new one solely for versioning. Do not create empty directories merely to express this map.

## Creation, updates, and archives

Update an existing document when it owns the subject. Create a new ID only for a new durable identity, a required chronological record, or a distinct decision, specification, or workflow. Never duplicate a record because files moved. Prefer links over repeated rules.

Follow [document versioning](workflows/document_versioning.md) for project documents. Sequence IDs identify records, not revisions. New documents start at `v1`; substantive revisions use `v2`, `v3`, or a minor version such as `v3.1`. Keep the current document in its existing functional folder and stable filename with explicit version metadata. Before replacing it, archive the complete predecessor under `docs/archive/`, retaining its ID and filename stem with an old-version suffix in filename form: metadata `Version: v3.1` becomes `_v3dot1.md`, not `_v3.1.md`. This suffix is the explicit exception to retaining an identical filename when archiving a revision. Record the predecessor link and change summary in the current revision. Treat an unversioned predecessor as the `v1` baseline on its first substantive revision; preserve unrelated legacy documents.

Archive every substantively superseded version, mark it historical, and link it to its current owner. Preserve content and decision evidence, rebase relative links when needed, and verify links and stale paths. Archived material must not be cited as current authority. Package artifacts such as skill contracts and templates follow the plugin release rather than receiving project-record IDs or archive copies for each package edit.

At the end of substantive work, create or update only operational records that capture a material transition, decision, state, or next action. Report which records changed; if none were needed, say so.
