# Code comments and specification reasoning

Version: v1

## Rule and scope

No comments in code. Keep business explanations, design rationale and non-obvious
implementation reasoning in the relevant specification documents. This includes
reasoning about implementation hazards; there is no exception for it. Do not use
inline comments, block comments, documentation comments, JSDoc or explanatory
docstrings as another home for that prose.

Apply this rule when authoring or changing source, tests, scripts, configuration
and code examples or templates through YMAS workflows. It governs this repository;
an adopting repository retains its own governing authority. During authorized
adoption, establish the rule in local agent guidance and identify any conflict
with existing requirements rather than silently weakening either rule. Plugin
installation alone does not change repository policy.

## Preserve the reasoning

Use clear names, explicit structure and meaningful tests to make implementation
readable. Put the explanation of required behavior, constraints, hazards, choices
and consequences in the existing owning SPEC, SPECARC or project-equivalent
specification. Reference affected symbols, paths and verification cases there
when useful; a comment pointing to a spec is still a code comment.

For this workflow package, the relevant workflow rule or skill contract owns
workflow behavior and reasoning. Do not create a product specification solely to
document this package's procedures. Follow existing documentation and versioning
rules, prefer one owner over duplicate prose, and keep observations or proposals
distinct from accepted requirements.

When an in-scope change removes an existing comment, preserve its useful meaning
in the appropriate specification before removal. Check it against current
authority and behavior; do not turn an obsolete assertion into an accepted rule.
Existing comments do not authorize unrelated repository-wide cleanup. Markdown
documentation is prose, not code comments to remove; code examples within it
follow the same rule as other code.

## Verification and conflicts

Before completing implementation or repair, review changed code and code examples
for comments and confirm that necessary explanations are captured in their
specification owners. Use language-aware inspection where available; comment-like
characters inside runtime strings or documentation prose are not sufficient
evidence of a violation. Record the scope and result with normal verification.

If a legally required notice or a tool directive encoded as a comment creates a
real conflict, stop the affected change and report its exact location, requirement
and consequence to the governing owner. Preserve the notice or directive while
the conflict is unresolved. Do not delete it blindly or silently treat it as an
exception. Continue independent work that does not depend on resolving the conflict.
