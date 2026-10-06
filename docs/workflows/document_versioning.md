# Document versioning

Version: v1.2
Previous version: [v1.1](../archive/workflows/document_versioning_v1dot1.md)
Change summary: Clarify coordinated permanent-ID allocation and read-only edition diagnostics.

Use this procedure when creating or substantively revising an adopting project's documents under its documentation standard. Keep its governing approval process and any explicitly established version convention. This package's skill contracts, templates, README, and index are distribution artifacts governed by the plugin release; versions in output templates describe the resulting project documents, not the template or plugin release.

## Identity and revision

A family sequence number identifies a document; it is never a version. For example, `SPEC_STORAGE_012_access-rules.md` remains `SPEC_012` through `v1`, `v2`, `v3`, and `v3.1`. Likewise, `SPECARC_006` and `OPS_TASK_021` identify records, not revisions. Do not allocate a new SPEC or SPECARC ID to revise the same owner. Each family retains its independent sequence across all Level 2 categories. A new subject, distinct decision, or chronological task/state/next-action record can need a new ID; another revision of that same record keeps its ID. An unnumbered established owner such as `systems.md` can be versioned without inventing a sequence ID.

Use explicit `Version: v1` metadata for a new document; an existing `Document version:` field can retain its label. Metadata uses normal dotted notation, such as `Version: v3.1`. Use `v2`, `v3`, and so on for substantial document-generation/redefinition; use a dotted increment such as `v3.1` for a meaningful compatible refinement/correction. Keep this simple major/minor convention unless the repository explicitly adopts another scheme. Compare numeric components, so `v3.10` follows `v3.9`. Inspect the current document and all its archives before selecting a later unused version; never reuse a version or infer it from a family ID, timestamp, or plugin version.

When a version appears in a YMAS filename, replace the metadata dot with the literal word `dot`: `v3.1` becomes `v3dot1`, `v3.10` becomes `v3dot10`, and whole-number `v3` stays `v3`. Do not use `_v3.1.md` for a new versioned archive. This filename representation does not change the document's dotted version metadata or logical identity. Preserve unrelated legacy filenames; do not mass-rename prior archives solely for conformity.

Typographical, formatting, and link-only corrections can retain the document version when meaning is unchanged. If meaning changes, create a versioned revision and archive its predecessor. For an existing unversioned document, preserve it as a `v1` baseline when first making a substantive revision, then publish the revision as `v2`; do not mass-rename or rewrite unrelated legacy documents.

Version metadata records revision, not acceptance. Mark drafts, accepted decisions, and unresolved questions according to project authority; a higher version never grants approval or resolves an authority conflict.

For concurrent document creation, the integration owner coordinates family-ID reservations across active workers/branches. Recheck the proposed ID against current, archived, legacy and reserved identities before integration. A branch-local next number is provisional until reconciled. If a collision exists, stop the affected allocation/integration, preserve both records and their evidence, and resolve through the owning coordinator; do not overwrite, silently renumber historical records or ask the user to choose routine IDs. [Read-only diagnostics](../../scripts/diagnose_documents.py) can expose duplicate current IDs and edition metadata, but cannot infer semantic ownership or unseen branch reservations.

## Publish a revision

1. Identify the current owning document, its stable ID and path, version, governing status, and relevant links. Prepare the revision from accepted decisions; keep unsettled choices visibly provisional. Satisfy the project's approval requirements before replacing accepted authority.
2. Before overwriting the current content, preserve the complete predecessor in the project's archive. Default to `docs/archive/`, mirroring the functional path beneath `docs/` and appending `_<old-version-in-filename-form>` to the filename stem: `_v3dot1` for metadata `v3.1`. This version-qualified suffix is the explicit exception to preserving an identical filename during an ordinary move; retain the logical ID and stem. For a root document such as `systems.md`, use `docs/archive/root/systems_v2.md`. An archive destination must not already exist; resolve a collision without overwriting history.
3. Mark the archive historical, record its original version and replacement, and link to the current owner. Preserve its original content and decision evidence; a historical notice and rebased relative links may be added so the moved document remains usable. Do not edit historical rules to match the replacement or treat embedded old acceptance/status text as current authority.
4. Write the newer version in the **same current folder and stable filename**, preserving the logical ID. Record its version, predecessor archive link, and a concise change summary. Do not put the newer version in the archive, create an active `v2/` or `v3/` directory, or leave two current owners for the same document.
5. Include the new current content and predecessor archive together in the same scoped change. Keep normal index and authority links pointing to the current stable path; use archive links only for historical evidence. Consumers follow the canonical path to the current document rather than sorting versioned filenames. Update or rebase links affected by archiving.
6. Verify one current owner, the later unused version, preserved identity, the complete prior revision in the archive, working links, and correct current/historical status. Report the new version and archived predecessor.

For example, revising `SPEC_012` from `v3` to `v3.1` leaves the new content at `docs/specifications/SPEC_STORAGE_012_access-rules.md` with `Document version: v3.1`. The old content belongs at `docs/archive/specifications/SPEC_STORAGE_012_access-rules_v3.md`. The `012` sequence remains unchanged.

Revising `SPECARC_EVENTS_001_event-reconciliation.md` from `v3.1` to `v3.2` leaves `Version: v3.2` at the same canonical path and preserves the complete old revision as `docs/archive/specifications/SPECARC_EVENTS_001_event-reconciliation_v3dot1.md` with historical `Version: v3.1`. `SPECARC_001` does not change. Consumers follow the canonical path, not filename sorting.

With an established `spec/` structure, the same revision keeps `spec/systems.md` current at `v3.1` and preserves its old `v3` at `spec/archive/systems_v3.md`. Keep that local structure instead of relocating the current map to the default directories.
