# OPS_WORKFLOW_<ID> — Documentation standard

Status: Draft until the project's authority owners and directories are confirmed.

Adapt this template to the adopting YMAS project. Preserve existing rules and document IDs. Remove instructions and examples that do not fit the project. This template has no authority in a repository until adopted there.

## Scope and permitted Markdown locations

Name the permitted root Markdown files, functional directories, and any exceptions. For a new standard, choose its adopted Level 2 category and the next family-wide ID, then use `docs/OPS_WORKFLOW_<L2_CATEGORY>_<ID>_documentation-standard.md`; preserve an existing standard's legacy filename and ID. Keep repository instructions at root `AGENTS.md` or the repository's established equivalent. Use purpose-specific directories under `docs/` rather than scattering files.

## Document IDs and naming

Use `<FAMILY>_<L2_CATEGORY>_<ID>_<l3-description>.md` for new numbered documents. `FAMILY` names the record type and may contain an underscore, as in `OPS_TASK`. The actual Level 2 value is one uppercase token without internal underscores. `ID` is a zero-padded three-digit number. Level 2 identifies the durable domain, system, capability, or technical area that owns the record; the final description uses short, durable lowercase words separated by hyphens. Underscores separate structural segments, not words inside the description.

Define this project's adopted Level 2 taxonomy or its category-selection rules below using established project terminology. Treat Level 2 as controlled retrieval vocabulary: choose one canonical token per concept across families and avoid synonyms, plurals, unnecessary abbreviations, spelling variants, overlapping names, or narrower labels for the same area unless the project explicitly distinguishes them. A search for an adopted `_<L2_CATEGORY>_` should return that area's records across families; `OPS_TASK_` should return all tasks, and durable words in the final description should find specific subjects. Prefer retrieval consistency to a more natural sounding variation in one filename. Preserve sensible existing categories. If ownership is unresolved, use a documented project fallback or mark classification unresolved; do not invent a category. For a new project without a taxonomy, keep any minimal proposed set provisional until adopted. This template supplies no universal Level 2 vocabulary.

Never use roadmap, milestone, phase, sprint, release, campaign, or other temporary planning labels as Level 2 categories. Planning identifiers may remain in roadmap-owned documents, plans, commits, pull requests, changelogs, and explanatory historical notes where the adopting project's governance allows them; they do not become durable classifications for unrelated records.

IDs are project-scoped, never reused or renumbered, even after archiving or moving. The logical record ID remains `<FAMILY>_<ID>`; Level 2 classifies the filename without changing that ID. Unless the project's current authority explicitly establishes another rule, every family has one independent sequence across all Level 2 categories; category changes do not restart numbering. Find the highest family ID across current, archived, and legacy locations before allocating a new one. Existing filenames without Level 2 remain valid legacy names. Rename them only during an intentional migration that preserves logical IDs, history, and links.

Adopt only the families the project actually needs: `SOT` (product source of truth), `RM` (roadmap), `SYS` (systems), `SPEC` (specifications), `PLAN` (plans), `AUDIT` (audits), `ADR` (architecture decisions), `BUG` (individual bugs), `OPS_TASK` (completed tasks), `OPS_STATE` (state snapshots), `OPS_NEXT` (next actions), `OPS_DECISION` (operational decisions), `OPS_SPECDEF` (provisional specification work), `OPS_WORKFLOW` (workflows), and `REF` (references).

## Level 2 taxonomy — project owner must complete

Record adopted durable categories, their meanings, and any documented fallback here. Keep the vocabulary small, mutually distinguishable where practical, and broad enough to remain stable. Before adding a token, search the existing taxonomy and current and legacy filenames, decide whether an established category owns the concept, and add a new one only for a durable distinction. If legacy aliases exist, record their mapping without automatically renaming records. Label proposals as provisional until the project adopts them. Do not put planning periods or campaign names in this taxonomy.

## Operational memory and workflow discovery

- `docs/operations/tasks/` — `OPS_TASK` substantive completed work.
- `docs/operations/state/` — `OPS_STATE` current project-state snapshots.
- `docs/operations/next/` — `OPS_NEXT` current recommended next actions.
- `docs/operations/decisions/` — `OPS_DECISION` durable operational decisions; explicit supersession only.
- `docs/operations/specdef/` — `OPS_SPECDEF` provisional design, research, observations, proposals, open questions, and accepted working decisions awaiting promotion. Label their status. They do not amend canonical product authority.
- `docs/operations/workflows/` — additional `OPS_WORKFLOW` records. Keep the primary standard at its adopted path, including any valid legacy path.

When present, the highest numbered `OPS_TASK`, `OPS_STATE`, and `OPS_NEXT` is respectively the latest task, current snapshot, and current next action. Find relevant records in legacy locations during migrations. Operational records are context and evidence, not product authority. Discover specialized workflows through the repository's instructions and installed skills; load only those relevant to the task.

During authorized adoption, keep agent instructions concise: point to this project's standard and the available workflow index, and ask the agent to use relevant workflows for ordinary requests without requiring users to name skills or assign record IDs. Preserve local approval and Git rules. Evaluation assesses the current repository without edits; consolidation requires a request and preserves information by default; destructive cleanup requires explicit intent. An audit target must come from the request or conversation, not these operational records. Detailed procedures belong in the specialized skills, not the always-on instructions. Installation alone does not adopt this standard or guarantee automatic skill selection.

## Authority hierarchy — project owner must complete

List this project's current product, architecture, specification, and decision authorities in their real precedence order, with exact paths or discovery rules. State who resolves conflicts. Do not fill this section by guessing from filenames, Git history, or implementation. Until completed, record authority as unresolved and seek the actual governing source before changing contested behavior.

Distinguish authority, implementation evidence, observation, inference, proposal, recommendation, unresolved question, and accepted decision. Implementation, tests, operational memory, bug records, and historical documents do not automatically override current approved authority.

## Functional documentation directories

Map each adopted family to its actual directory. Recommended when applicable: `docs/sot/`, `docs/roadmap/`, `docs/systems/`, `docs/specifications/`, `docs/plans/`, `docs/audits/`, `docs/decisions/`, `docs/references/`, `docs/engineering/bugs/` for `BUG`, and `docs/engineering/knowledge/` for generalized `REF`. Do not create empty directories or relocate existing files merely to match these examples.

## Creation, updates, and archival

Update an existing owner before creating a duplicate. Create a new ID for a new durable identity, a needed chronological record, or a distinct specification, decision, or workflow. Prefer references over copied rules. Archive useful superseded material with an explicit historical label; preserve its ID, filename, history, and links. Archived records do not regain current authority. Validate links and stale paths after moves.

At task completion, update only operational records needed to capture a material transition, state, decision, or next action, and report which changed.
