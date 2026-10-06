# OPS_TASK_016 - Template portability and release preparation

Status: Repair verified locally; combined distribution pending final-source gates
Version: v1.1
Previous version: [v1](../../archive/operations/tasks/OPS_TASK_DOCS_016_template-portability-and-release-preparation_v1.md)
Change summary: Record the published-install validation boundary repair.
Date: 2026-10-06
Scope: The inherited True Specification worksheet reference, its materialization
regression, and preparation of the already authorized combined candidate.

## Finding and repair

Independent review of human-understanding checkpoint
`39051ba461228f154112308ad10e6c6a4f890dc4` found that the True Specification
template's package-relative worksheet link breaks when copied to an adopting
repository's `docs/sot/` location. The earlier
[versioning repair](OPS_TASK_DOCS_011_template-versioning-portability.md) explicitly
deferred that separate link; its versioning-only test did not cover it.

The [template](../../../skills/spec-driven-development/assets/true_specification_template.md)
now directs the agent to the project's worksheet or the available
`true-spec-worksheet` skill, and to link the actual project-owned worksheet when
recording decisions. This keeps decision traceability without assuming that the
adopting repository contains the installed package's directory structure.

The [regression](../../../scripts/test_validate_package.py) checks every retained
Markdown link across the seven existing materialized template locations. Its new
control accepts a real project-owned worksheet, proves that path checking ran,
and rejects the old package path while the valid worksheet still exists.
Both affected checks failed against the original template; all six link tests
passed after the repair. These are deterministic portability checks, not a model
replay or an actual adoption session. No neighboring workflow or Feature Map
behavior changes.

## Published installation validation boundary

The required public-route installation check exposed a second bounded defect:
`smoke_install.py` imported the candidate validator and redirected it to published
`0.4.0`, whose package predates Feature Map assets. This imposed the newer
candidate's asset requirements on the preserved older release.

The smoke check now runs each installed package's own versioned validator and
propagates its failures. Candidate byte comparison and versioned skill-set checks
remain in place; the candidate validator and Feature Map requirements are
unchanged. A deterministic subprocess control verifies the installed validator
runs, rejects a missing required asset, and passes once that asset exists. The
original public-route failure is retained as red evidence. Fresh actual checkout
and public-route results must be recorded for the final source; a stub-validator
control alone does not establish installation compatibility or discovery.

## Combined source and publication boundaries

Candidate `0.5.0` combines PR13's `0.4.1` preparation, verification/Feature Map
addition `69bb414e5ae2ca10ed617d7f358d4e4b98627470`, and the
[human-understanding work](OPS_TASK_DOCS_015_human-understanding.md), followed by
this repair. The owner authorized publication, merge after required gates, and a
verified version tag. PR12 remains a historical checkpoint and is not a separate
merge candidate. Existing release and verification branches remain preserved.

The unpublished human-understanding checkpoint contained a private commit email.
It remains preserved locally with its original evidence. The release branch
recreates that change with the verified public GitHub identity and the exact same
Git tree `f7b8e864fa3f96a26d0cf4f427dc4e030c728e8f` before applying this repair.
This is a new commit identity, not a claim that the original checkpoint is an
ancestor of the publication branch. Final-source receipts must bind the new
candidate's exact commit, tree and tracked bytes.

Final package validation, installation checks, CI and independent repair review
belong in that source receipt. Authenticated discovery in a fresh client remains
a release gate. An earlier isolated session received HTTP 401; installation and
supplied-contract replays do not establish discovery. Publication authorization
does not authorize initiating interactive sign-in, copying credentials or changing
credential storage, and does not clear this gate. Keep the combined PR draft and
unmerged, and create no release tag until all required gates pass.
