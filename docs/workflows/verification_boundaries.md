# Verification boundaries and maintained harnesses

Version: v2
Previous version: [v1](../archive/workflows/verification_boundaries_v1.md)
Change summary: Add maintained verification tooling and bounded capability-to-scenario integration.

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

## Promote repeated verification into maintained tools

A **Verification Harness** is the repository's maintained executable tooling for
repeatable verification and controlled state. Reuse tests, fixture builders and existing
development tools before adding another interface. Promote a procedure when repeated
nontrivial setup, state handling, inspection or evidence capture causes rediscovery,
inconsistent results or throwaway scripts. A one-off trivial check need not become a
framework. Keep the smallest tool that can falsify the governing contract.

Inspect accepted requirements and actual entrypoints first. Define the scenario's known
state, prerequisites, expected observations, evidence, owned resources and cleanup. Seed
valid states without disabling production guards. Make clocks, randomness, persistence
and external inputs controlled where relevant; report unresolved nondeterminism.

| Capability where applicable | Maintained interface should establish |
| --- | --- |
| Environment health | Required runtime/dependencies, governed state and actionable preflight failures |
| Seed/reset | A known scenario state inside an explicitly approved target |
| Exercise | Actual user/system entrypoint and required lifecycle/failure edges |
| Inspect/snapshot | Observable state and source/scenario identity without hidden mutation |
| Logs/evidence | Useful JSON where appropriate, command, exit status, observations and artifact references |
| Screenshot | Actual UI evidence when the contract requires it; label fixture images separately |
| Performance | Workload, environment, measurement method and governing threshold where required |
| Cleanup | Only resources owned by this run; preserve uncertain operation identity before retrying |

These are capabilities to select, not mandatory command names or a universal API. A small
repository-owned verification/control CLI is useful when it materially improves
reproducibility; composable scripts or existing test runners may already suffice. Avoid a
general application CLI. Describe inputs, defaults, target boundaries, effects, output,
exit behavior and corrective action for errors. A failed preflight or unavailable tool is
a blocker/limit, never a passing behavior check. Build the useful control surface when
authorized rather than repeatedly compensating with ad hoc instructions.

Mutation requires the task's existing authorization, isolation and approved target scope.
Preview/dry-run destructive operations where practical; explain limits when preview is
unavailable. Preview must expose intended effects without performing them. Do not infer
permission from a map, tool descriptor, successful preflight or machine-readable output.
Do not broaden access, weaken guards or reroute denied actions. Cleanup is also a mutation
and must verify resource ownership and resolved bounds. Stop a known blocker immediately.

Use a [Feature Map](feature_maps.md) when recurring capability navigation warrants one.
Link each scenario to accepted clauses, the maintained executable and required evidence.
The harness's own positive/negative tests establish tool behavior; run the actual scenario
to establish application behavior. Static maps, graph edges, self-reported success and
schema conformance cannot prove runtime invariants. Retain scope, evidence, verdict and
limits through the existing receipt; independent/adversarial review and project-owned
acceptance remain required wherever the governing workflow requires them.

Update the affected tool/scenario when feature behavior, entrypoints, prerequisites,
controllability or dependencies change. Check declared raw source hashes and inspect
affected callers; repair the smallest failed unit and preserve correct neighbors. Keep
the same-unit failure count and three-failed-attempt planning escalation above. No blind
daily regeneration, new acceptance gate or scheduled maintenance is introduced.
