# Verification at changed boundaries

Version: v1

Choose evidence that can falsify the changed contract. Preserve required project checks;
green totals establish only asserted behavior. Broad reruns become useful when a shared
boundary changes, source changes, failures appear or consequential gaps remain. A narrow
independent review asks a concrete new question, rather than repeating the whole audit.

For shared return/state contracts, derive affected callers from implementation references
and actual adapters/producers, including indirect or shorthand paths. Before claiming
coverage, use a compact lifecycle matrix where consequential:

| Caller / source reference | Completed | Pending/yield | Halt/no progress | Resume same identity | Restart/reopen | Evidence / limit |
| --- | --- | --- | --- | --- | --- | --- |
| Actual caller | Verified / unsupported / unresolved | Same | Same | Same | Same | Exact source, command, artifact |

Use the real entry/preflight → admission → yield → re-entry boundary. Verify durable
identity, one effect and repeated-completion behavior when required by the contract;
exercise actual reopen/restart for persistence risk. Mark inapplicable edges with a
contract reason. An unsupported or unresolved edge is not a passing test. Review all
materially changed callers before declaring the shared contract verified.

Before building a costly fixture, check dependencies, command/runtime availability,
disposable path ownership and governed authority/state prerequisites. Reuse valid fixtures
where possible without weakening production guards or importing domain-specific rules
into this package. Graphs and static references support discovery; they cannot prove
runtime invariants. If an optional tool is unavailable, report its limits and use an
authorized source-based fallback; a denied/known-stop action has no fallback route.

For a failed unit retain expected/observed, artifact/source, valid reproduction yes/no,
cause class (fixture, environment, implementation, authority or unknown), repair/source
change, failed same-unit count and stop/reassessment reason. Aggregate failed assertions
are not repair-attempt counts. Stop a known blocker immediately; the three-failure ceiling
is a maximum before reassessing the unit, not a quota or permission to continue.

Report source/test/review identity through the [source receipt](source_receipts.md).
Distinguish fixture checks, actual runtime/browser evidence and any project-owned human
acceptance. Do not invent a product acceptance committee or waive an adopter requirement.
