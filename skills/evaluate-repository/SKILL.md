---
name: evaluate-repository
description: Assess the current repository's documentation, authority, agent instructions, and fit with YMAS without changing files. Use for repository evaluations or adoption assessments; bare invocation targets the current repository. Do not infer migration permission or product authority from repository state.
---

# Evaluate repository

Use for a read-only assessment of the current repository. Bare `$evaluate-repository` has that target; it does not require a separate audit subject. Confirm the repository root from the working directory and current conversation. If neither identifies one repository, ask which repository to evaluate rather than selecting an arbitrary neighboring checkout.

## Read-only boundary

Return the assessment in conversation by default. Do not reorganize, rename, delete, consolidate, create YMAS documents, rewrite agent instructions, or resolve authority conflicts. Do not run checks that modify files merely to evaluate documentation. A recommendation is not permission to implement it. If the user separately asks for changes, apply the relevant workflow only within that scope; use [documentation-consolidation](../documentation-consolidation/SKILL.md) for a requested migration.

## Assessment

1. Read repository agent instructions, documentation indexes, and any established documentation standard. Identify existing conventions before comparing them with YMAS. Use indexes and targeted searches to inventory the corpus, including archived and legacy locations; read the sources needed to assess it rather than loading every file.
2. Map agent instructions; specifications and architecture; planning and roadmaps; decisions; operational/current-state records; bugs and engineering knowledge. Record actual paths, owners, status, and explicit precedence where available. Missing categories are findings, not instructions to generate documents.
3. Determine authority from explicit project rules and accepted decisions. A filename such as `SOT`, a newer timestamp, implementation, or a recent commit does not itself confer authority. Use Git history when it helps explain a material duplication, move, or apparent conflict; label history as evidence.
4. Inspect naming, IDs, existing retrieval categories, references, and migrations already underway. Identify likely duplicates, stale statements, conflicting guidance, and apparently unowned content with concrete examples. Distinguish confirmed facts from uncertainty; similar wording alone does not establish that a document is disposable.
5. Compare the existing model with YMAS's small bootstrap, specialized workflows, repository-owned authority, and stable retrieval vocabulary. Equivalent existing structures can remain. Explain the smallest adoption or organization changes that would help without prescribing every YMAS family or a new parallel system.

## Result

Give a concise, source-linked assessment covering the repository model, authority, organization, operational memory, bugs/knowledge, naming/taxonomy, conflicts, YMAS compatibility, and the recommended next action. Scale detail to the repository; no mandatory report template or new record is needed.

Clearly distinguish established authority, implementation evidence, historical material, likely duplication, ambiguity, missing information, and recommendation. State any inspection limits. Recommend consolidation only where supported, and leave unresolved authority with the project's owner.
