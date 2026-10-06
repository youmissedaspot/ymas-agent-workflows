> Status: Historical / superseded
> Current owner: [current workflow](../../workflows/behavioral_checks.md)

# Bounded behavioral checks

Version: v1.1
Previous version: [v1](behavioral_checks_v1.md)
Change summary: Add maintained-verification and feature-map drift cases without changing grader authority.

The fourteen [neutral cases](../../../scripts/behavior_cases.json) cover explicit, implicit and
negative routing, scope, settled decisions, whole-set conflicts, known blockers, selected
contracts, resume identity, concept ambiguity/freshness and project-owned acceptance, maintained verification and scoped feature-map drift. Run affected cases for changed
skills; broaden only for new failures, changed contracts or an explicitly requested baseline.

In disposable fixtures, present each prompt/context with the actual selected package
contracts available. Keep the task's selected model/effort/permissions unchanged. Record
the qualified contract path/hash/version and package source commit/tree or full digest.
Capture before/after filesystem state, relevant tool/action evidence and final artifacts
outside the public package. Do not copy private project evidence into reusable cases.
An observer should assign route/actions/decisions from those traces and inspect whether
authority and scope are preserved; self-declared action labels alone are insufficient.

`python scripts/grade_behavior.py observations.json` grades the declared observations.
The input has `kind` (`observed_replay` or `synthetic_grader_fixture`), `metadata` with
`package_source`, `package_version`, `model`, `effort`, `permissions`, `artifacts`, and
`observations` keyed by selected case IDs. Each observation has `route`, `actions`, `writes`
(fixture-relative paths), `decisions`, and `human_acceptance_claimed: false`.
Use the case's action labels; record actual scope/authority nuance in the review artifact.

For affected checks, include an explicit nonempty `case_ids` list and observations for
exactly those IDs; omitted selection means the complete baseline. Unknown/duplicate IDs
and missing selected outcomes fail. Cases may list valid supporting `routes`; these are
compositions under the execution loop, not claims that one bare skill name must win.

The grader does not run a model, inspect a filesystem, authenticate a trace or establish
semantic correctness. Its synthetic positive/negative tests establish only checker behavior.
Reported actual replays need independent trace/artifact inspection. They remain bounded
samples, with no claim of automatic host selection, compaction-loss rates or broad efficacy.
Installation tests establish installed files/discovery, not these behaviors. Preserve
failures and distinguish an unexecuted case from a pass. No savings target or telemetry
collector is included.
