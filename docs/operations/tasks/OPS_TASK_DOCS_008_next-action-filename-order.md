# OPS_TASK_008 — Next-action filename order

Status: Implemented for review; integration pending.

The user requested one narrow naming exception: new `OPS_NEXT` filenames use `OPS_NEXT_<ID>_<L2_CATEGORY>_<l3-description>.md`. Other numbered families retain `<FAMILY>_<L2_CATEGORY>_<ID>_<l3-description>.md`. Earlier naming history established category-first retrieval; this refinement prioritizes chronological/current-action retrieval for next-action records while retaining the same searchable Level 2 vocabulary.

Updated the repository standard, reusable standard template, bootstrap skill, consolidation skill, and README. Numeric IDs remain family-wide across categories and are never restarted, reused, or renumbered. The highest numeric next-action ID remains current unless project authority explicitly establishes otherwise. Retrieval accounts for legacy locations and filenames; category sorting is not recency. Historical files are not mass-renamed without an explicitly scoped normalization migration. The prohibition on planning-derived Level 2 tokens remains in place, and no other family gains an exception.

Validation: reviewed all active generic filename statements and the examples against the requested rules. All six skill front-matter validations passed. Package validation passed for 31 Markdown files and 43 links, including metadata and index routes; the scoped diff check passed. No historical files, package version, or marketplace metadata were changed. Historical task records describe their original convention and remain intact.

Files changed: `README.md`, `INDEX.md`, `docs/OPS_WORKFLOW_001_documentation_standard.md`, `skills/project-bootstrap/SKILL.md`, `skills/project-bootstrap/assets/documentation_standard_template.md`, `skills/documentation-consolidation/SKILL.md`, and this task record.
