# Bounded behavioral checks

Version: v1.5
Previous version: [v1.4](../archive/workflows/behavioral_checks_v1dot4.md)
Change summary: Exercise artifact delivery when the intended recipient cannot open the original surface.

The thirty-two [neutral cases](../../scripts/behavior_cases.json) cover explicit, implicit and
negative routing, scope, settled decisions, whole-set conflicts, known blockers, selected
contracts, resume identity, concept ambiguity/freshness and project-owned acceptance, maintained verification and scoped feature-map drift, Understanding Checks, adult/project explanations, prototype authority, immediate architectural discrepancies, alternatives, durable conversational decisions and optional documentation purposes. Run affected cases for changed
skills; broaden only for new failures, changed contracts or an explicitly requested baseline.

Four [handoff](task_context.md#delegation-and-return) cases cover returned work under
newer steering, an unreachable executor with an uncertain operation, configured
work without a produced deliverable, and a produced artifact the recipient cannot open.
Inspect the actual return, current source, status evidence, access and next owner.
Synthetic controls verify required/forbidden observations in
the grader; they do not prove live task delivery, recovery or future agent compliance.

The six audit cases use [neutral executable fixtures](../../scripts/audit_fixtures.py).
Materialize a selected case with `python scripts/audit_fixtures.py --case <case> --output <new-disposable-path>`;
the parent directory must exist and the output must be new. Run `python -B tools/check_lookup.py`
inside that fixture for its declared contract checks. Give a trial agent only the selected
skill, request and raw fixture files, excluding the generator and test oracle. See
[audit evaluation guidance](../../skills/audit-repair/references/audit_assessment.md#bounded-evaluation).
Fixture regressions establish their application's known-good, seeded-failure and preflight
behavior. They do not establish model audit accuracy; actual trials need the trace/artifact
inspection below, including false positives, missed defects, scope and evidence calibration.

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

For human-understanding cases, independently inspect the actual wording, source use and action order. Action labels alone cannot establish an adult tone, technical accuracy, readable prose or that an Understanding Check preceded implementation recommendations. Editorial quality is contextual judgment, not a banned-word or punctuation score.
