# Audit coverage, findings and reconciliation

Use only the parts needed by the requested audit or authorized repair. Governing
project requirements control expected behavior; audit reports are evidence unless the
project explicitly gives them a different role. Keep the explanation readable and the
work proportional. No fixed report template, audit team or new authority register is required.

## Whole-project coverage

A request to audit the whole project establishes that target. After relevant inspection,
briefly state the current source, governing requirements, requested risks and practical
inspection limits. Use existing indexes, systems maps or [Feature Maps](../../../docs/workflows/feature_maps.md)
to locate material systems, entrypoints, shared boundaries and their original sources;
an incomplete map is not evidence of complete coverage.

Tailor inspection to the request, architecture and consequence of failure. Applicable
lenses may include specification consistency, correctness, security and information
boundaries, authoritative state/ownership, persistence and recovery, concurrency and
retry behavior, migrations, UI interaction, performance or installability. A domain
profile can suggest questions, but cannot supply product requirements. For example,
restart/replay matters to a persistent service; a static document package may instead
need copied-template and installation checks. Do not mandate game, MMO or distributed
architecture for unrelated projects.

Trace consequential expectations to implementation and verification. Select negative,
boundary, restart/retry and cross-system scenarios where their governing contracts and
risks warrant them. Inspect the actual runtime/browser when the claim depends on those
behaviors; use the existing [verification boundaries](../../../docs/workflows/verification_boundaries.md)
for valid fixtures, caller lifecycles and maintained tools. Static inspection can establish
a finding without reproducing it, but cannot establish unobserved runtime acceptance.

Retain a compact coverage account when useful: area/contract, inspected source or scenario,
result and limit. Mark unchecked or partly checked areas plainly. A high test count,
unchanged hash or absence of findings is not proof that the whole project is correct.
Prioritize consequential findings; do not turn the audit into an unrelated repair campaign.

## Findings and evidence

For a material finding, retain the governing expectation, affected boundary, expected and
observed behavior, consequence, exact source/runtime identity, supporting evidence and
limits. Reuse the repository's finding IDs and severity scheme where available.

State severity separately from confidence. A reproduced defect and a statically established
defect can both be serious; a speculative serious consequence remains a hypothesis until
supported. Identify what was reproduced, established by source, inferred or not verified.
Do not inflate severity from an auditor's label or reduce a known consequence merely
because a permitted runtime is unavailable. Separate fixture/environment problems and
specification/authority gaps from product defects; a failed preflight is not application
behavior. Preserve unresolved questions without inventing a rule or reopening settled choices.

## Compare audit reports

When comparison is requested, retain each report's source identity, scope and evidence.
Reconcile findings against the current source and governing requirements. Use a small
crosswalk where it helps: original IDs, duplicate/complementary/conflicting/stale claims,
current evidence, disposition and reason. Similar wording alone does not prove duplication;
different wording may describe the same failed unit.

Apply precedence explicitly supplied by the user or project to conflicting recommendations
within its scope. Do not infer precedence from model/vendor, recency, confidence of tone or
majority vote. Precedence does not make an unsupported defect true or permit an audit to
override settled specifications. For example, Report A may be the selected comparison
baseline while its claim that an accepted storage mechanism must be replaced is rejected
for lack of governing support. Retain valid complementary findings from Report B.

If authoritative sources conflict without a settled precedence, surface the conflict and
stop only dependent work. Label claims tied to old source as historical; revalidate before
carrying them into the current verdict. Do not silently transfer old tests or reviews to
new source. Use [source receipts](../../../docs/workflows/source_receipts.md) for consequential
review evidence and the existing independent/adversarial review rules where applicable;
comparison does not require a model competition or repeated whole-project audit.

## Reproduction, regression and closure

For an authorized confirmed repair, retain the original failing conditions and expected
observation. Reuse or add the smallest maintained regression that can falsify that contract,
covering the relevant failure boundary rather than only the successful path. Exercise the
original failing source in an authorized disposable fixture, or use a valid negative control,
to establish that the regression detects the defect. Do not weaken production guards or
execute an unsafe reproduction to obtain red evidence.

Rerun the original reproduction and regression on the repaired source, plus required
affected-boundary checks. A passing unrelated suite, changed code or self-reported tool
success does not close the original failure. If faithful reproduction or maintained
regression protection is infeasible, state the reason and evidence limits; leave the
unverified behavior open under the project's bug/acceptance process. A manual scenario
may be the meaningful regression when automation cannot establish the behavior.

Preserve correct neighbors and use the existing same-unit failure count, architecture
discrepancy trigger and [verification boundaries](../../../docs/workflows/verification_boundaries.md).
Record closure and remaining limits in the existing bug/task/evidence owner; do not create
parallel records or universal full-suite requirements.

## Bounded evaluation

The neutral fixtures in [audit_fixtures.py](../../../scripts/audit_fixtures.py) provide raw
requirements, lookup code, valid/invalid input, a maintained behavior check and sample
reports. Materialize only the selected case in an authorized disposable path. Give a
trial agent the actual selected skill and that case's prompt/raw files, excluding the
generator, test oracle and intended verdict. Preserve source identity, actual output,
commands and filesystem effects for independent inspection.

The fixture tests establish seeded application/checker behavior; the outcome grader's
positive/negative controls establish grading behavior. Neither executes a model or proves
audit accuracy. Actual supplied-contract trials must be labeled and inspected separately
under [behavioral checks](../../../docs/workflows/behavioral_checks.md). Include known-good
controls and assess false positives, missed defects, evidence calibration and scope as
well as found defects. Stale evidence must not become a current finding without revalidation.
