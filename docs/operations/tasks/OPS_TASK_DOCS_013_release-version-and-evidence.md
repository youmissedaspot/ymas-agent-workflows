# OPS_TASK_013 - Release version and evidence

Status: Release candidate prepared; integration, tag and authenticated discovery pending.
Version: v1
Predecessor: [source evidence and verification](OPS_TASK_DOCS_012_source-evidence-and-verification.md)
Source checkpoint: `2165f1d42d62e1cf7ffb241c6608f3ce1de434e2`
Branch: `work/reusable-workflow-release-0.4.1`

## Change

Prepare compatible patch version `0.4.1` for the reusable source-evidence, diagnostics
and verification improvements. Published main and the prior checkpoint both used
`0.4.0` despite different supporting bytes. The unpinned marketplace follows main,
so its distributable version must be part of the final integration candidate.

Add `0.4.1` to the installation smoke's versioned eight-skill contract while retaining
the older published-version contracts. Update current installation/version guidance
and preserve earlier dated verification as evidence for its original source only.
No skill contract, behavioral case, governing authority or acceptance rule changes.
The original checkpoint and its task record remain intact.

## Verification and release boundary

The coordinator records the final commit/tree, full tracked raw-byte inventory,
regressions, package/schema/links, ID diagnostics, neutrality checks, independent
source review and disposable installation/platform CI in one detailed release receipt.
Earlier evidence does not automatically transfer to this new versioned source.

Fresh authenticated discovery must show the candidate's available plugin skills in
the intended client. The earlier unauthenticated CLI attempt obtained no response;
installed/enabled bookkeeping alone cannot satisfy this gate. No authentication,
credential transfer or user-runtime update is performed by this preparation step.

Keep integration and tagging blocked until required release checks pass. Tag the
verified resulting release commit; a manifest version or tag alone is not proof.
Only after material integration should current state/next deltas link to the detailed
receipt. No pre-integration current-state/next record is manufactured here.

Automatic routing, real compaction recovery, desktop discovery and usage savings
remain unproved. The package stays instruction-only and project-neutral.
