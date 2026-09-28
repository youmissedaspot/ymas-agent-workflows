---
name: project-bootstrap
description: Use when asked to orient or bootstrap a repository, establish or repair its documentation-governance structure, discover its authority hierarchy, or adopt the YMAS documentation standard.
---

# Project bootstrap

Use for repository orientation and documentation setup. This skill does not make an arbitrary third-party repository adopt YMAS document families.

1. Read repository `AGENTS.md` or its established equivalent. Locate its documentation standard or equivalent; if none exists, discover the actual conventions before proposing any structure.
2. Identify the project's explicit authority hierarchy and the documents relevant to this task: current product truth, architecture, specifications, accepted decisions, and current operational context. Report gaps or conflicts rather than inventing authority.
3. Inspect the applicable operational families for their highest sequence numbers, including legacy locations during migration. Distinguish current records from archives. Load only material needed for the task.
4. Before creating documentation, search for an existing owner to update. Preserve IDs, filenames, and historical links when moving numbered files; never restart a sequence because of a directory move.
5. Before code changes, inspect affected implementation and tests. Inspect Git history when existing behavior has a non-obvious purpose. Record material historical constraints as evidence, not authority.

When the repository has adopted YMAS documentation conventions, use its own standard for family names, paths, and authority. The common families are `SOT`, `RM`, `SYS`, `SPEC`, `PLAN`, `AUDIT`, `ADR`, `BUG`, `OPS_TASK`, `OPS_STATE`, `OPS_NEXT`, `OPS_DECISION`, `OPS_SPECDEF`, `OPS_WORKFLOW`, and `REF`, each with an independent three-digit sequence. Do not assume those conventions in another repository.

For an explicitly YMAS project that needs a new documentation standard, adapt [the standard template](assets/documentation_standard_template.md) to that repository's actual authority and directories. Preserve any existing project rules. Add a short pointer to the standard in the repository instruction file. Do not copy the template unchanged when its authority fields are unresolved.

When a repository explicitly adopts the YMAS workflow system, establish concise defaults in its own agent instructions (or equivalent) that route through this package's `INDEX.md`, apply the [agent execution loop](../../docs/workflows/agent_execution_loop.md) automatically to substantive work, and require [isolated workbranches](../../docs/rules/multi_agent_workbranches.md) for repository writes. Use actual installed paths and adapt to the repository's existing routing and Git process. Preserve equivalent or stronger rules; do not overwrite existing agent or Git governance. Surface conflicts and follow the repository's governing authority.

For substantive product or system work, make `spec-driven-development` and its [workflow](../../docs/workflows/specification_driven_development.md) discoverable through the adopting repository's established routing. Map its layers to existing authority; add only layers the work needs. Do not turn routine or already specified tasks into mandatory document creation.

End with a concise map of governing sources, current context, unresolved authority questions, and the files changed, if any.
