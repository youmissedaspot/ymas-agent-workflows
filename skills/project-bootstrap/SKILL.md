---
name: project-bootstrap
description: Use when asked to orient or bootstrap a repository, establish or repair its documentation-governance structure, discover its authority hierarchy, or adopt the YMAS documentation standard.
---

# Project bootstrap

Use for repository orientation and documentation setup. This skill does not make an arbitrary third-party repository adopt YMAS document families.

1. Read repository `AGENTS.md` or its established equivalent. Locate its documentation standard or equivalent; if none exists, discover the actual conventions before proposing any structure.
2. Identify the project's explicit authority hierarchy and the documents relevant to this task: current product truth, architecture, specifications, accepted decisions, and current operational context. Report gaps or conflicts rather than inventing authority.
3. Inspect the applicable operational families for their highest sequence numbers across Level 2 categories, including archived and legacy locations. Distinguish current records from archives. Load only material needed for the task.
4. Before creating documentation, search for an existing owner to update. Preserve IDs, filenames, and historical links when moving numbered files; never restart a family sequence because of a category or directory change.
5. Before code changes, inspect affected implementation and tests. Inspect Git history when existing behavior has a non-obvious purpose. Record material historical constraints as evidence, not authority.

When the repository has adopted YMAS documentation conventions, use its own standard for family names, paths, authority, and durable Level 2 taxonomy. Identify established project terminology and record the adopted categories or selection rules in that project's documentation standard. Treat Level 2 as controlled retrieval vocabulary: reuse one canonical token per concept, checking existing and legacy filenames before adding a category; avoid synonymous or singular/plural variants for the same area. New numbered files use `<FAMILY>_<L2_CATEGORY>_<ID>_<L3_DESCRIPTION>.md`; each family has one independent three-digit sequence across all categories. Never use roadmap, milestone, phase, sprint, release, campaign, or other temporary planning labels as Level 2 categories. Preserve legacy IDs; do not invent a category when ownership is unresolved. Follow a documented fallback or mark classification unresolved. For a new YMAS project, a minimal proposed taxonomy remains provisional until adopted. Do not impose YMAS naming or taxonomy on an unrelated repository.

The common families are `SOT`, `RM`, `SYS`, `SPEC`, `PLAN`, `AUDIT`, `ADR`, `BUG`, `OPS_TASK`, `OPS_STATE`, `OPS_NEXT`, `OPS_DECISION`, `OPS_SPECDEF`, `OPS_WORKFLOW`, and `REF`. Adopt only those the project needs.

For an explicitly YMAS project that needs a new documentation standard, adapt [the standard template](assets/documentation_standard_template.md) to that repository's actual authority and directories. Preserve any existing project rules. Add a short pointer to the standard in the repository instruction file. Do not copy the template unchanged when its authority fields are unresolved.

When a repository explicitly adopts the YMAS workflow system, establish concise defaults in its own agent instructions (or equivalent) that route through this package's `INDEX.md`, apply the [agent execution loop](../../docs/workflows/agent_execution_loop.md) automatically to substantive work, and require [isolated workbranches](../../docs/rules/multi_agent_workbranches.md) for repository writes. Use actual installed paths and adapt to the repository's existing routing and Git process. Preserve equivalent or stronger rules; do not overwrite existing agent or Git governance. Surface conflicts and follow the repository's governing authority.

For substantive product or system work, make `spec-driven-development` and its [workflow](../../docs/workflows/specification_driven_development.md) discoverable through the adopting repository's established routing. Map its layers to existing authority; add only layers the work needs. Do not turn routine or already specified tasks into mandatory document creation.

End with a concise map of governing sources, current context, unresolved authority questions, and the files changed, if any.
