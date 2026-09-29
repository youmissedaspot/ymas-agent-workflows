# OPS_WORKFLOW_<ID> — Documentation standard

Status: Draft until the project's authority owners and directories are confirmed.

Adapt this template to the adopting YMAS project. Preserve existing rules and document IDs. Remove instructions and examples that do not fit the project. This template has no authority in a repository until adopted there.

## Scope and permitted Markdown locations

Name the permitted root Markdown files, functional directories, and any exceptions. For a new standard, choose its adopted Level 2 category and the next family-wide ID, then use `docs/OPS_WORKFLOW_<L2_CATEGORY>_<ID>_documentation_standard.md`; preserve an existing standard's legacy filename and ID. Keep repository instructions at root `AGENTS.md` or the repository's established equivalent. Use purpose-specific directories under `docs/` rather than scattering files.

## Document IDs and naming

Use `<FAMILY>_<L2_CATEGORY>_<ID>_<L3_DESCRIPTION>.md` for new numbered documents. `ID` is a zero-padded three-digit number. The uppercase Level 2 category identifies the durable domain, system, capability, or technical area that owns the record; Level 3 uses a short durable underscore-separated description. Do not use roadmap, milestone, phase, sprint, release, campaign, or other temporary planning labels as Level 2 categories.

Define this project's adopted Level 2 taxonomy or its category-selection rules below using established project terminology. Treat Level 2 as controlled retrieval vocabulary: choose one canonical token per concept and avoid singular/plural variants, synonyms, or narrower labels for the same area. Preserve sensible existing categories. If ownership is unresolved, use a documented project fallback or mark classification unresolved; do not invent a category. For a new project without a taxonomy, keep any minimal proposed set provisional until adopted. This template supplies no universal Level 2 vocabulary.

IDs are project-scoped, never reused or renumbered, even after archiving or moving. The logical record ID remains `<FAMILY>_<ID>`; Level 2 classifies the filename without changing that ID. Every family has one independent sequence across all Level 2 categories; category changes do not restart numbering. Find the highest family ID across current, archived, and legacy locations before allocating a new one. Existing filenames without Level 2 remain valid legacy names. Rename them only during an intentional migration that preserves logical IDs, history, and links.

Adopt only the families the project actually needs: `SOT` (product source of truth), `RM` (roadmap), `SYS` (systems), `SPEC` (specifications), `PLAN` (plans), `AUDIT` (audits), `ADR` (architecture decisions), `BUG` (individual bugs), `OPS_TASK` (completed tasks), `OPS_STATE` (state snapshots), `OPS_NEXT` (next actions), `OPS_DECISION` (operational decisions), `OPS_SPECDEF` (provisional specification work), `OPS_WORKFLOW` (workflows), and `REF` (references).

## Level 2 taxonomy — project owner must complete

Record adopted durable categories, their meanings, and any documented fallback here. Check existing and legacy filenames before adding a token, and reuse the canonical token for the same concept. If legacy aliases exist, record their mapping without automatically renaming records. Label proposals as provisional until the project adopts them. Do not put planning periods or campaign names in this taxonomy.

## Operational memory and workflow discovery

- `docs/operations/tasks/` — `OPS_TASK` substantive completed work.
- `docs/operations/state/` — `OPS_STATE` current project-state snapshots.
- `docs/operations/next/` — `OPS_NEXT` current recommended next actions.
- `docs/operations/decisions/` — `OPS_DECISION` durable operational decisions; explicit supersession only.
- `docs/operations/specdef/` — `OPS_SPECDEF` provisional design, research, observations, proposals, open questions, and accepted working decisions awaiting promotion. Label their status. They do not amend canonical product authority.
- `docs/operations/workflows/` — additional `OPS_WORKFLOW` records. Keep the primary standard at its adopted path, including any valid legacy path.

When present, the highest numbered `OPS_TASK`, `OPS_STATE`, and `OPS_NEXT` is respectively the latest task, current snapshot, and current next action. Find relevant records in legacy locations during migrations. Operational records are context and evidence, not product authority. Discover specialized workflows through the repository's instructions and installed skills; load only those relevant to the task.

## Authority hierarchy — project owner must complete

List this project's current product, architecture, specification, and decision authorities in their real precedence order, with exact paths or discovery rules. State who resolves conflicts. Do not fill this section by guessing from filenames, Git history, or implementation. Until completed, record authority as unresolved and seek the actual governing source before changing contested behavior.

Distinguish authority, implementation evidence, observation, inference, proposal, recommendation, unresolved question, and accepted decision. Implementation, tests, operational memory, bug records, and historical documents do not automatically override current approved authority.

## Functional documentation directories

Map each adopted family to its actual directory. Recommended when applicable: `docs/sot/`, `docs/roadmap/`, `docs/systems/`, `docs/specifications/`, `docs/plans/`, `docs/audits/`, `docs/decisions/`, `docs/references/`, `docs/engineering/bugs/` for `BUG`, and `docs/engineering/knowledge/` for generalized `REF`. Do not create empty directories or relocate existing files merely to match these examples.

## Creation, updates, and archival

Update an existing owner before creating a duplicate. Create a new ID for a new durable identity, a needed chronological record, or a distinct specification, decision, or workflow. Prefer references over copied rules. Archive useful superseded material with an explicit historical label; preserve its ID, filename, history, and links. Archived records do not regain current authority. Validate links and stale paths after moves.

At task completion, update only operational records needed to capture a material transition, state, decision, or next action, and report which changed.
