# OPS_TASK_011 - Template versioning portability

Status: Complete for the repair and local verification
Version: v1
Date: 2026-10-03
Task base: `58bdfc2e2e7db7cb4965674c613bb54dbbb2a0c8`
Scope: Adopter-facing document-versioning references, a bounded regression, and a verified task-base reference correction.

## Failure and repair

The documentation-standard template and five specification/map templates linked to `../../../docs/workflows/document_versioning.md`. That route resolves inside the package but escapes an adopting repository when the templates are copied into their recommended document locations. Five occurrences exist on main; the architecture-specification template adds the sixth in PR #9.

Replace these six references with self-contained guidance to follow this project's adopted document-versioning rules. Preserve the surrounding identity, version metadata, archive, acceptance, and specification requirements. Package-resident skill and reference links retain their existing routes.

During merge-readiness review, replace OPS_TASK_010's historical `2da6f33` base reference with the reachable PR #8 merge commit `402ec8991885e3a14768dc46c898c3d4167ef52b`. Git and the GitHub commit API both identify that commit as the parent of task commit `58bdfc2e2e7db7cb4965674c613bb54dbbb2a0c8`. The original reviewed head is outside the candidate's ancestry, but both baseline commits share tree `c6d3bf3915f624e2e2b3dbf91bdbf802b4902a7b`. This reference-only correction preserves the task's scope, file lists, and recorded outcomes.

## Verification

The regression in `scripts/test_validate_package.py` copies the six actual templates into a disposable adopter, covering seven output locations including both `docs/systems/systems.md` and an established root `systems.md`. It checks the versioning references without installing the package guide. A negative control against the task base rejected all seven locations; the repaired templates passed. The existing path-alias regression also passed.

Package validation and scoped whitespace checks passed. Windows Codex CLI `0.159.1` passed candidate checkout installation, repeated installation, and removal/reinstallation in a disposable Codex home. Published-source installation, repeated installation, marketplace refresh, and removal/reinstallation also passed for the existing six-skill release; that check does not establish publication of this repair.

These checks establish static template/versioning portability and package installation behavior. They are not a live adoption session, application acceptance, or cross-platform CI evidence.

## Remaining boundary

The True Specification template also contains a package-relative worksheet link, `../../true-spec-worksheet/assets/true_spec_worksheet_template.md`. That separate reference is outside this versioning repair and remains unchanged. The regression intentionally checks versioning references rather than claiming every materialized-template link is portable.

The repair uses its own branch based on PR #9's head, preserving the concurrent branch. Publication is a separate draft PR targeting `work/product-definition-architecture`; merging and deployment remain outside scope.
