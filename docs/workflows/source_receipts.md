# Source and integration receipts

Version: v1

Use one detailed evidence receipt for a consequential candidate under the repository's
established integration process. An existing equivalent receipt is sufficient. This
procedure grants no publication, merge, deployment, or automatic retry authority.

Record exact repository/ref, source commit and tree, tested and reviewed source,
commands/outcomes/artifacts, finding dispositions, evidence limits and source-specific
authorization for the intended action. Keep partial installed/source comparisons labeled
partial. A package version alone cannot identify installed bytes. For a release candidate,
record the full tracked-file inventory from `scripts/check_receipt.py inventory --repo .`:
raw SHA256 per path, aggregate digest, source commit/tree and manifest version. Compare
every inventory path with installed bytes in read-only inspection; report extra runtime
files separately and missing/different paths explicitly. Do not refresh a cache to prove
the source of its previous contents. Line-ending differences count as different bytes.

Receipt states are **draft**, **ready**, **blocked**, **superseded**, and **integrated**.
A new finding, denied action, changed source/base or stale review makes readiness require
reassessment. Record the reason and replacement receipt when superseded; old approval
does not transfer. A known denial stops the affected action immediately. Do not reroute
it through another tool, worker or integration path. Three failed repair attempts are
a maximum before reassessment, never permission to retry a denied action.

Immediately before an authorized integration, reconcile the live candidate against the
receipt. Where supported, stale approvals/checks should become visibly obsolete through
the repository's normal controls. A read-only check is a snapshot, not a lock or an
enforcement engine; another actor can still change the candidate after it passes.

`python scripts/check_receipt.py check receipt.json --repo . --candidate HEAD` checks the
following shape (placeholders must be replaced; this is an incomplete draft):

```json
{
  "state": "draft",
  "source": {"commit": "<full hash>", "tree": "<full hash>"},
  "tested": {"source": {"commit": "<full hash>", "tree": "<full hash>"}, "artifact": "<test receipt>"},
  "reviewed": {"source": {"commit": "<full hash>", "tree": "<full hash>"}, "artifact": "<review report>"},
  "authorization": {"status": "not_requested", "action": "integrate", "source": {"commit": "<full hash>", "tree": "<full hash>"}, "evidence": "<actual instruction>"},
  "findings": [{"id": "<finding>", "blocking": true, "status": "open", "evidence": "<disposition evidence>"}],
  "checks": [{"command": "<command>", "outcome": "passed", "artifact": "<result>"}]
}
```

Ready requires all source identities to match, resolved blocking findings, passing checks
and actual source-specific integration authorization. The checker validates recorded
claims and Git identities; it cannot authenticate permission, execute the tests or grade
review quality. No action follows from a passing check.

After integration, retain candidate identity plus `integration` with `candidate` (the
source object), actual `commit`, `tree` and `artifact`; set state `integrated` only with
confirmed evidence. Check with `--integrated <actual-ref>`. This conservative checker
requires the integrated tree to equal the tested/reviewed tree. If merge/rebase/squash
changes it, create evidence for that resulting source and link the predecessor receipt;
do not declare differing bytes equivalent from a merge message.

The owning coordinator then records the material integration delta in current state and
the next action/dependency, linking both to this one detailed receipt. Preserve historical
pre-integration task claims. Reconcile live Git/operation status at resume; the highest
state/next ID alone is insufficient when a later integration has not been closed out.
Create only records needed for an actual transition; do not generate a task/state/next
triad mechanically. A blocked or superseded candidate remains visibly so in closeout.
