# OPS_TASK_009 — Specification handoff and document versioning

Status: Complete on task branch; unmerged
Document version: v1
Date: October 2, 2026
Branch: task/spec-systems-document-versioning

## Result

The documented workflow is **True Specification conversations and settled decisions → formal specification documents → integrated `systems.md` architecture map**. Conversations and decision records supply source material; accepted specifications define their subjects; the map integrates the entire current specification set. Individual architecture specifications remain specifications rather than replacing the whole-set map.

An existing `systems.md` may be inspected for architecture, dependencies, and impacts while writing specifications. It must not override newly settled decisions or generate requirements to preserve itself. Its absence does not block specification formalization. After the specifications are written, review the entire current set and create/update the integrated map, including specifications unaffected by the latest conversation. Material changes to boundaries, ownership, dependencies, interfaces, or architecture require map review and update in that specification cycle. An accurate map that needs no meaningful revision receives a reported review rather than a mechanical version bump.

Document IDs remain stable identities independent of versions such as `v1`, `v2`, `v3`, and `v3.1`. When `v3` becomes `v3.1`, keep the current document at its established canonical path with `Document version: v3.1`; preserve the complete `v3` predecessor in the project's archive with an old-version suffix, a historical notice, and a link to the current owner. This applies to both specification documents and `systems.md`. Substantial revisions use major versions; compatible meaningful refinements/corrections use minor versions. Meaning-preserving spelling, formatting, and link fixes need no version bump. Existing local archive/version conventions are retained.

Applied the new rule to this package's two substantively revised project documents: the documentation standard and specification workflow are `v2` at their existing paths, with their previously unversioned `v1` baselines preserved in explicitly historical archives. Skill contracts, reusable templates, README, and index remain package artifacts governed by plugin release rather than project-record version copies.

## Changed files

- [Specification-development skill](../../../skills/spec-driven-development/SKILL.md) — correct handoff order and selection for completed conversations, full-set map coverage, and versioning.
- [Specification workflow](../../workflows/specification_driven_development.md) — specify formalization before architecture integration, existing-map treatment, and required refresh conditions.
- [Systems map checklist](../../../skills/spec-driven-development/references/systems_map_checklist.md) — trace specifications, systems, relationships, overlaps, gaps, and coherence.
- [New systems.md template](../../../skills/spec-driven-development/assets/systems_map_template.md) — specification/version coverage and integrated architecture relationships.
- [True Specification template](../../../skills/spec-driven-development/assets/true_specification_template.md) — version metadata and downstream handoff.
- [Canonical Specification template](../../../skills/spec-driven-development/assets/canonical_specification_template.md) — version metadata and inclusion in the integrated map.
- [Detailed System Specification template](../../../skills/spec-driven-development/assets/detailed_system_specification_template.md) — accepted decision sources, version metadata, and map inclusion.
- [Project-bootstrap skill](../../../skills/project-bootstrap/SKILL.md) — consistent specification order, stable paths, and archival.
- [Documentation standard template](../../../skills/project-bootstrap/assets/documentation_standard_template.md) — specification/map roles and explicit document-versioning rules.
- [Documentation-consolidation skill](../../../skills/documentation-consolidation/SKILL.md) — preserve subject authority, map separation, and versioned predecessors.
- [New document-versioning procedure](../../workflows/document_versioning.md) — stable identities/paths, meaningful major/minor revisions, and complete predecessor archives.
- [Local documentation standard](../../OPS_WORKFLOW_001_documentation_standard.md) — adopt document versions independently of sequence IDs.
- [Historical documentation standard v1](../../archive/OPS_WORKFLOW_001_documentation_standard_v1.md) — preserved baseline.
- [Historical specification workflow v1](../../archive/workflows/specification_driven_development_v1.md) — preserved baseline with rebased links.
- [README](../../../README.md) — describe the corrected workflow and document versions.
- [INDEX](../../../INDEX.md) — route to versioning, the systems-map template, and this record.
- This task record — preserve the material workflow change and verification results.

## Verification and boundaries

Package validation passed for all six skill front-matter blocks, 36 Markdown files, 82 Markdown links, manifest/marketplace identity, and index routes. The existing link-containment regression check passed. Candidate-checkout and published-source installation checks passed fresh/repeated installation, removal/reinstallation, and installed-package validation; the published check also passed marketplace refresh. The host CLI reported `0.159.0-alpha.3`; these are observed host results, not claims about the pinned `0.159.1` CI matrix or other operating systems. No model session or user's Codex home was changed by the installation checks. These checks verify packaging and installed documents; model compliance during a live specification session remains unverified.

Compared both archived baselines against their branch-start Git contents after normalizing relative-link destinations: the entire original text and original link targets were preserved, with only explicit historical notices and required link rebasing. Reviewed the active workflow, skill, templates, bootstrap/consolidation guidance, and version rules against the requested order and `v3` → `v3.1` behavior. The final scoped whitespace check passed.

No unresolved ambiguity or conflicting active instruction was found. Historical archives retain the earlier workflow as historical evidence and explicitly disclaim current authority. Product acceptance and architecture decisions remain with the adopting project. The branch remains unmerged as requested; no plugin release or publication was performed.
