# Human understanding and readable documentation

Version: v1

**Teach for human understanding. Trace for evidence.** Help the owner understand what
exists, why it behaves that way, what governs it, and what remains uncertain. Reuse the
repository's specifications, decisions, implementation and evidence; explanations do
not create another authority layer. Adapt depth and form to the question and reader.

## Understanding Check

Before substantial specification, architecture or implementation work, demonstrate your
understanding in a short plain-English restatement. Include the requested problem or
change, affected behavior, governing authority, important constraints, and genuinely
unresolved questions or contradictions. Inspect the relevant sources first; say when
authority or evidence is unavailable. Do this before proposing implementation, except
for trivial work whose implementation is explicitly authorized.

The check catches misunderstanding before it becomes a specification or code. It is a
concise explanation, not a mandatory report template, new document, permission request
or repeated ceremony at each step. Use the current request and evidence; refresh it when
material steering or a discovered conflict changes your understanding. Continue settled
authorized work without waiting for an acknowledgment. Consequential unresolved choices
stop only their dependent work under the project's existing authority rules.

For example: "You want an expired reservation to stop blocking new reservations. That
affects allocation and recovery after restart. The accepted allocation specification
governs ownership; the persistence specification governs restart behavior. We need to
preserve existing reservations. Those sources disagree about when expiry releases the
allocation, so that rule needs its owner's decision before dependent design."

## Explain the idea and its consequences

Explain naturally in plain English. Give the reader a useful mental model: the underlying
idea, why it exists, cause and consequence, and important distinctions. Introduce
implementation details when they answer the question. Use normal adult vocabulary;
define necessary jargon where it appears. A concrete example often clarifies more than
an analogy. Use a short analogy or anecdote only when it helps, and keep its limits clear.

Preserve distinctions that affect correctness. For example, a transaction's all-or-nothing
behavior does not by itself establish isolation from concurrent transactions. Simpler
language must not erase that difference or imply guarantees the system does not provide.
Explain the important consequence of getting the concept wrong when it matters.

In a repository, inspect the actual owning specifications and relevant code, tests,
decisions or history. An adopted Feature Map or systems map can locate sources; inspect
the originals before relying on their claims. Separate required behavior from observed
implementation, fact from inference, and current authority from historical evidence.
Name contradictions and uncertainty plainly. Do not invent missing project behavior or
present a generic example as the project's established design.

Cite sources where they materially improve trust, explain a decision, expose a conflict
or let the owner inspect evidence. Use useful paths or clauses rather than a citation on
every sentence. Let the explanation read as connected prose; no mandatory WHAT/HOW/WHY
headings or fixed number of sections is required. For the dedicated explanation route,
use [like-im-5](../../skills/like-im-5/SKILL.md).

## Editorial judgment

Prefer concrete claims, specific nouns and verbs, direct wording, useful detail and
consistent domain terminology. Vary sentence length naturally. State uncertainty with
its reason or evidence limit; remove hedging that adds no information. Read the result
as something one competent adult would write for another.

Revise recurring patterns that obstruct meaning: canned introductions, unnecessary
recap conclusions, repeated points, obligatory groups of three, fake contrasts,
habitual balancing clauses, generic signposting, inflated abstractions and vague nouns
when the actual thing can be named. "Several factors affect recovery" is less useful
than naming the conditions that change it. Stock phrases such as "At its core" or
"This highlights" deserve removal when they contribute nothing.

Use headings, bolding, lists and punctuation when they help the reader navigate or
compare information. Excessive formatting, ornamental punctuation and uniform sentence
rhythm can make a document harder to read. Ordinary paragraphs often serve explanation
better than an outline built around Markdown. Structured specifications and comparison
tables still need structure where it conveys their contracts clearly.

Judge clarity, precision, frequency and context. No individual word or punctuation mark
is inherently forbidden. Do not build a banned-word checker, punctuation score or an
AI-authorship detector. Editorial review must preserve facts, technical distinctions,
accepted qualifications, history and evidence while improving how they are expressed.

## Ordinary documentation purposes

When useful, distinguish what a reader needs from an ordinary document:

| Purpose | Reader's need |
| --- | --- |
| Tutorial | Learn through a guided example with an appropriate starting point |
| How-to | Complete a specific task with prerequisites and observable results |
| Reference | Look up an exact contract, option, term or constraint |
| Explanation | Understand a concept, cause, consequence or design choice |

These purposes can reveal missing context or an awkward mixture of instructions and
rationale. They are optional editorial aids, not required folders, new record families
or a migration instruction. Keep an existing useful owner. Canonical specifications
have their own authority and purpose; do not force SPEC/SPECARC or other governing
documents into these categories. Organization and clearer prose cannot amend their rules.
