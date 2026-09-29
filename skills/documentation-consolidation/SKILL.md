---
name: documentation-consolidation
description: Migrate or consolidate the current repository's existing documentation into an adapted YMAS workflow when the user requests it. Bare invocation authorizes preserve-mode consolidation of the current repository; cleanup requires explicit intent. Do not infer deletion permission or authority from apparent duplication.
---

# Documentation consolidation

Use for an explicitly requested documentation migration or consolidation. Bare `$documentation-consolidation` targets the current repository in preserve mode. A natural-language consolidation request is sufficient; no special command is required. If the current repository is unclear, ask which one. A request only to assess fit belongs to [evaluate-repository](../evaluate-repository/SKILL.md).

## Establish the migration boundary

Before changing files, inspect existing conventions, authority, filenames/directories, agent instructions (including established casing), document IDs, Git status, and any migration already underway. Read relevant history to understand intentional structure. Preserve unrelated work and follow the repository's branch rules.

Identify the existing owner for each subject and adapt the YMAS method to that repository. Do not impose YMAS through an unrelated task or create a competing documentation system. Explicit invocation authorizes this adaptation, subject to local authority; it does not authorize inventing product rules or deciding contested precedence.

Make a concrete source-to-destination map for the requested scope: documents to retain, move, consolidate, cross-reference, or archive, with reasons and authority sources. Resolve routine placement using established rules. Leave ambiguous material intact and ask the owner only about decisions that block the affected changes; continue independent, authorized work.

## Preserve mode — default

- Establish or update the repository's own documentation standard and concise agent-instruction pointers using [project-bootstrap](../project-bootstrap/SKILL.md) and its [adaptable template](../project-bootstrap/assets/documentation_standard_template.md). Preserve stronger or equivalent existing rules and filenames; do not copy a universal hierarchy into the project.
- Map existing content into appropriate owners/families and reuse established IDs and retrieval categories. Do not rename valid legacy records just to match a newer convention. Update an existing owner before creating another document; create operational records only for meaningful transitions, decisions, or current state supported by evidence.
- Consolidate duplicate guidance in a clear current owner while retaining source material or archiving it with a historical label and a reference to its current owner. Preserve unique qualifications, rationale, decision evidence, and historical context. Do not replace a source with a stub that discards its information in preserve mode.
- Move clearly superseded material to the project's archive only when its status and ownership are understood and the move is permitted. Preserve IDs, filenames, and traceability. Update links and indexes affected by approved moves. Do not destructively remove historical information.

## Cleanup mode — explicit only

`$documentation-consolidation cleanup` or a clear request to remove superseded material enables cleanup within that scope. Requests to organize, tidy, evaluate, or consolidate alone do not enable it. No additional confirmation is required solely because cleanup mode was explicitly requested; honor any actual project approval requirements.

Before removing each obsolete duplicate, establish that:

- its information is preserved in the correct owner;
- its authority and supersession are understood;
- incoming references are updated;
- Git contains the removed content and provides a known recovery commit;
- removal loses no unique historical or decision evidence.

If any condition is uncertain, preserve the file. Untracked or uncommitted content has no guaranteed Git recovery; do not delete it on the assumption that history will recover it. Cleanup is not permission to discard unresolved conflicts or unrelated files.

## Retrieval and verification

For new YMAS records use `<FAMILY>_<L2_CATEGORY>_<ID>_<l3-description>.md`: underscores separate structural segments; lowercase hyphens separate description words. Reuse one stable, canonical uppercase Level 2 token per domain across families. Avoid synonyms, alternate plurals, arbitrary abbreviations, and overlapping categories unless established locally. Level 2 is a retrieval dimension, not a sequence: allocate IDs family-wide across current, archived, and legacy locations unless project authority explicitly says otherwise. Never turn roadmap, milestone, phase, sprint, release, or temporary planning labels into durable taxonomy. Use the adopting project's vocabulary, not a product-specific taxonomy supplied by this package.

Verify the scoped diff against the migration map, document IDs, content preservation, references/indexes, and stale paths. Use before/after hashes for content-preserving moves; for intentional consolidation, account for each source's unique information and retained historical location. Preserve mode must have no unexplained loss; cleanup must have recovery evidence for each removal. Run applicable documentation/package checks.

Report the mode used, files changed, owners established, preserved/archived material, any deletions with recovery commits, verification results, unresolved questions, and the next action. Keep recommendations separate from completed changes and product authority separate from organizational decisions.
