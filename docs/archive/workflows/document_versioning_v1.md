> Status: Historical / superseded; not current authority.
> Version: v1
> Superseded by: v1.1 at the [current document](../../workflows/document_versioning.md).
> Original revision follows; embedded status statements describe that historical revision.

# Document versioning

Document version: v1

Use this procedure when creating or substantively revising an adopting project's documents under its documentation standard. Keep its governing approval process and any explicitly established version convention. This package's skill contracts, templates, README, and index are distribution artifacts governed by the plugin release; versions in output templates describe the resulting project documents, not the template or plugin release.

## Identity and revision

A family sequence number identifies a document; it is never a version. For example, `SPEC_STORAGE_012_access-rules.md` remains `SPEC_012` through `v1`, `v2`, `v3`, and `v3.1`. Do not allocate `SPEC_013` to revise `SPEC_012`. A new subject, distinct decision, or chronological task/state/next-action record can need a new ID; another revision of that same record keeps its ID.

Use explicit `Document version: v1` metadata for a new document. Use `v2`, `v3`, and so on for substantial revisions to requirements, model, scope, structure, responsibilities, or governing rules; use a minor revision such as `v3.1` for a meaningful compatible refinement/correction that does not constitute a new major document generation. Canonical notation uses a dot: a request for `v3dot1` means `v3.1`. Use this simple major/minor convention unless the repository explicitly adopts another scheme. Compare numeric components, so `v3.10` follows `v3.9`. Inspect the current document and all its archives before selecting a later unused version; never reuse a version or infer it from a family ID, timestamp, or plugin version.

Typographical, formatting, and link-only corrections can retain the document version when meaning is unchanged. If meaning changes, create a versioned revision and archive its predecessor. For an existing unversioned document, preserve it as a `v1` baseline when first making a substantive revision, then publish the revision as `v2`; do not mass-rename or rewrite unrelated legacy documents.

Version metadata records revision, not acceptance. Mark drafts, accepted decisions, and unresolved questions according to project authority; a higher version never grants approval or resolves an authority conflict.

## Publish a revision

1. Identify the current owning document, its stable ID and path, version, governing status, and relevant links. Prepare the revision from accepted decisions; keep unsettled choices visibly provisional. Satisfy the project's approval requirements before replacing accepted authority.
2. Before overwriting the current content, preserve the complete predecessor in the project's archive. Default to `docs/archive/`, mirroring the functional path beneath `docs/` and appending `_<old-version>` to the filename stem. For a root document such as `systems.md`, use `docs/archive/root/systems_v2.md`. An archive destination must not already exist; resolve a collision without overwriting history.
3. Mark the archive historical, record its original version and replacement, and link to the current owner. Preserve its original content and decision evidence; a historical notice and rebased relative links may be added so the moved document remains usable. Do not edit historical rules to match the replacement or treat embedded old acceptance/status text as current authority.
4. Write the newer version in the **same current folder and stable filename**, preserving the logical ID. Record its version, predecessor archive link, and a concise change summary. Do not put the newer version in the archive, create an active `v2/` or `v3/` directory, or leave two current owners for the same document.
5. Include the new current content and predecessor archive together in the same scoped change. Keep normal index and authority links pointing to the current stable path; use archive links only for historical evidence. Consumers follow the canonical path to the current document rather than sorting versioned filenames. Update or rebase links affected by archiving.
6. Verify one current owner, the later unused version, preserved identity, the complete prior revision in the archive, working links, and correct current/historical status. Report the new version and archived predecessor.

For example, revising `SPEC_012` from `v3` to `v3.1` leaves the new content at `docs/specifications/SPEC_STORAGE_012_access-rules.md` with `Document version: v3.1`. The old content belongs at `docs/archive/specifications/SPEC_STORAGE_012_access-rules_v3.md`. The `012` sequence remains unchanged.

With an established `spec/` structure, the same revision keeps `spec/systems.md` current at `v3.1` and preserves its old `v3` at `spec/archive/systems_v3.md`. Keep that local structure instead of relocating the current map to the default directories.
