---
name: like-im-5
description: Explain technical, architectural, domain or project concepts in clear adult language for a competent reader unfamiliar with the subject. Use for explanation requests, including like-im-5; inspect relevant repository evidence when available. Explanation alone does not authorize implementation, adoption or documentation migration.
---

# Like I'm 5

Explain as one competent adult speaking to another who does not know this subject.
The informal name is not an instruction to use childish language or talk down to the
reader. Apply [human explanation and editorial judgment](../../docs/workflows/human_understanding.md).

Start with the underlying idea and why it exists. Use plain English and normal adult
vocabulary. Remove unnecessary jargon; define terms needed to preserve an important
distinction. Use concrete examples and explain the important consequence of getting the
concept wrong. Short analogies or anecdotes are optional aids, not a substitute for the
actual mechanism. Stay concise unless understanding requires more depth; adapt the form
to the question instead of imposing a report template.

For example, buying equipment may require removing payment, transferring ownership and
recording the accounting entry. A transaction makes those changes behave as one operation:
either all succeed or none do. Otherwise a buyer could lose the payment without receiving
the equipment. The formal term for this all-or-nothing behavior is atomicity. Do not imply
that atomicity alone also establishes concurrency isolation or every other database guarantee.

When the question concerns a repository, read its instructions and index, then the
smallest relevant specifications, accepted decisions, implementation and tests. Inspect
history when it explains a material design choice. Use existing system/Feature Maps for
navigation, checking their provenance and original sources. Explain this project's actual
model where evidence establishes it. Distinguish accepted requirements from what code
currently does, and established facts from inference or uncertainty. If sources conflict,
explain the conflict and its consequence under the repository's authority. If behavior
is missing or unverified, say so; generic examples cannot fill that gap.

Cite specifications, code, decisions, tests or history where a reference materially
improves trust or traceability. Explain naturally before asking the reader to decode
technical detail. Preserve consistent domain terms and meaningful qualifications.

Return the explanation in conversation by default. Do not change files, settle missing
product rules or begin implementation merely to explain them. A separately requested
write or development action follows the repository's relevant workflow and authorization.
