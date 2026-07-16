<!-- Source: audit/rubric.md -->

# Audit rubric

## Severity

### Error

A clear violation that may reduce trust, accessibility, accuracy, or task completion.

### Warning

A meaningful inconsistency or pattern that weakens clarity, tone, or authorship.

### Recommendation

A refinement that may improve quality but depends on context.

## Scoring

Start at 100.

- Error: subtract 5 points per unique issue, up to 25 points per rule.
- Warning: subtract 2 points per unique issue, up to 10 points per rule.
- Recommendation: subtract 1 point per unique issue, up to 5 points per rule.

Do not award false precision. Scores are directional and should always be paired with findings.

## Human-authorship signal score

Use this optional score only for AI writing-pattern audits.

Rate the content from 0 to 10 in half-point increments based on editorial evidence:

- 9–10: Strong specificity, experience, evidence, constraints, and individual point of view with few formulaic patterns.
- 7–8.5: Credible and distinctive overall with several polished or repeatable AI-associated patterns.
- 5–6.5: Mixed evidence, with substantial generic fluency, abstraction, repetition, or formulaic structure.
- 0–4.5: Predominantly generic or templated language with little concrete authorship evidence.

Consider DL-011, DL-054, and DL-060 through DL-066. Repeated patterns weigh more than isolated findings. Concrete evidence, constraints, tradeoffs, uncertainty, and point of view are positive signals.

The score is not a probability, detection result, or estimate of how much content was written by a human. Always pair it with a short evidence-based interpretation.

## Categories

- Grammar and mechanics
- Editorial structure
- Voice and evidence
- Natural writing
- Accessibility
- Component language
- Cross-document consistency

---

<!-- Source: audit/report-template.md -->

# Design Language audit

## Audit scope

- Source:
- Scope:
- Pages reviewed:
- Navigation followed:

## Summary

- Version:
- Scope:
- Overall score:
- Highest-risk issue:
- Strongest area:

## Human-authorship signals

Include this section only for AI writing-pattern audits.

- Signal score: /10
- Interpretation:
- Sentences with relevant patterns:
- Strongest human-authorship evidence:
- Strongest formulaic pattern:

## Category scores

| Category | Score | Notes |
|---|---:|---|
| Grammar and mechanics |  |  |
| Editorial structure |  |  |
| Voice and evidence |  |  |
| Natural writing |  |  |
| Accessibility |  |  |
| Component language |  |  |
| Consistency |  |  |

## Findings

### [Rule ID] Rule title

- Severity:
- Plain-language rule:
- Location:
- Found:
- Why it matters:
- Suggested direction:

## Patterns

Summarize repeated issues across the content.

## Rule reference

List only the rules cited in this audit. Include each rule ID, title, and plain-language meaning.

Readable reference: https://github.com/briandburge/design-language/blob/main/docs/rule-reference.md

Do not link users to the raw YAML unless they explicitly request the machine-readable registry.

## Priorities

1. Fix errors.
2. Fix repeated warnings.
3. Review recommendations in context.

---

<!-- Source: audit/templates/quick-check.md -->

# Quick check

Use this for a lightweight review.

Check:

- sentence case
- em dashes
- marketing language
- filler transitions
- false contrast
- repeated summary sentences
- paragraph length
- button and link clarity

Return only the five highest-value findings with rule IDs.

---

<!-- Source: audit/prompts/ai-tells-audit.md -->

# AI writing patterns audit prompt

Audit the supplied content for patterns covered by DL-011, DL-054, and DL-060 through DL-066.

Use this audit mode whenever the user asks whether content appears human-written, AI-written, AI-generated, AI-assisted, model-driven, or contains indicators associated with AI writing. Apply it even when the request also includes a broader website or document audit.

Look for repeated patterns, not isolated words alone.

Do not treat every em dash, triad, transition, or marketing term as proof of AI authorship. The goal is editorial quality, not detection.

Report a directional human-authorship signal score from 0 to 10 in half-point increments. This score measures how strongly the writing demonstrates concrete experience, specificity, constraints, tradeoffs, uncertainty, evidence, and individual point of view. It is not a probability, detection result, or claim about who wrote the content.

Accompany the score with a short interpretation in this pattern:

> Overall, I would rate the page [score]/10 for human-authorship signals. [Brief evidence-based explanation of what reads as experience-driven and which limited passages contain formulaic patterns associated with AI-assisted polishing.]

Do not convert the score into a percentage of human-written or AI-written content. When useful, identify the approximate number of sentences that contain relevant patterns, but describe the patterns rather than attributing their origin.

Treat repeated em-dash use as a meaningful signal under DL-011. Treat one necessary em dash as an isolated punctuation finding, not authorship evidence.

Always include the `Human-authorship signals` section. Do not replace it with directional hints elsewhere in the response.

For each finding:

- cite the rule ID
- show the smallest useful excerpt
- explain the pattern
- state whether it is isolated or repeated
- suggest an editing direction without rewriting the full passage

---

<!-- Source: audit/prompts/consistency-audit.md -->

# Cross-document consistency audit prompt

Compare the supplied pages or documents against Design Language v1.0.0 and against each other.

Find differences in:

- capitalization
- terminology
- product and feature names
- heading patterns
- button verbs
- number and date formats
- voice and level of formality
- repeated descriptions of the same concept

Report the preferred canonical form and list every conflicting form found.

---

<!-- Source: audit/prompts/document-audit.md -->

# Document audit prompt

You are a Design Language auditor.

Use `rules/rules.yaml`, the documents in `spec/`, and `audit/rubric.md` as the authority.

Audit the supplied document against Design Language v1.0.0.

Requirements:

- Do not rewrite the document unless explicitly asked.
- Report findings by stable rule ID.
- Quote only the smallest useful excerpt.
- Assign each finding a severity.
- Distinguish a one-off issue from a repeated pattern.
- Respect documented exceptions and context.
- Give a directional compliance score using the rubric.
- Prioritize the findings that most affect clarity, trust, accessibility, and authorship.
- Do not flag a review term automatically. Explain why it is weak in context.

Return the audit using `audit/report-template.md`.

---

<!-- Source: audit/prompts/rewrite-after-audit.md -->

# Rewrite after audit prompt

First audit the content against Design Language v1.0.0. Then revise only the findings the user approves, or all errors and warnings when approval is not required.

Preserve:

- factual meaning
- author point of view
- domain terminology
- intentional rhythm
- uncertainty and tradeoffs

Do not introduce new claims, metrics, or examples.

After the revision, provide a compact change log by rule ID.

---

<!-- Source: audit/prompts/ui-copy-audit.md -->

# UI copy audit prompt

Audit the supplied interface copy against Design Language v1.0.0.

Pay special attention to:

- sentence case
- action clarity
- button length
- stable navigation labels
- persistent form labels
- actionable errors
- empty-state orientation
- accessibility and blame

Report findings by rule ID. Do not infer missing product behavior. Mark uncertainty clearly.

---

<!-- Source: audit/prompts/website-audit.md -->

# Website audit prompt

You are auditing website language against Design Language v1.0.1.

The supplied URL defines the default audit scope.

Unless the user explicitly requests broader coverage:

- audit only the supplied page
- do not search the public web for related pages
- do not discover pages through search engines
- do not follow internal links
- do not compare against unrelated websites

If the requested scope is ambiguous, ask one clarifying question before auditing.

Offer:

- Single page
- Follow navigation from this page
- Entire website

For a navigation crawl, follow only internal links directly reachable from the supplied page.

Review page titles, headings, navigation, body copy, links, calls to action, forms, errors, captions, and repeated terminology within the approved scope.

Requirements:

- Report findings by rule ID.
- Separate global patterns from page-specific issues.
- Identify inconsistent names for the same concept or destination.
- Note where visual hierarchy and language hierarchy disagree.
- Do not redesign the interface.
- Do not rewrite copy unless asked.
- State exactly which pages were reviewed.
- Use the standard audit report template.

---

<!-- Source: decisions/0001-sentence-case.md -->

# 0001: Use sentence case

## Status

Accepted

## Decision

Use sentence case across headings and interface copy.

## Rationale

Sentence case supports scanning, reduces visual noise, and fits a modern SaaS editorial aesthetic.

## Exceptions

Official proper nouns, acronyms, and brand marks retain their approved capitalization.

---

<!-- Source: decisions/0002-avoid-em-dashes.md -->

# 0002: Avoid em dashes in normal prose

## Status

Accepted

## Decision

Avoid em dashes in normal editorial and interface copy.

## Rationale

They are often overused in AI-assisted writing and can create an affected rhythm. Periods, commas, colons, and parentheses are usually clearer.

## Exceptions

Quoted material and faithful reproduction of source text.

---

<!-- Source: decisions/0003-audit-before-rewrite.md -->

# 0003: Separate audit from rewrite

## Status

Accepted

## Decision

Audits identify and prioritize issues. They do not rewrite content unless the user requests revision.

## Rationale

Separating evaluation from transformation preserves author intent and makes findings easier to review.

---

<!-- Source: decisions/0004-respect-audit-scope.md -->

# 0004: Respect audit scope

## Status

Accepted

## Decision

Audits evaluate only the user-requested scope.

## Rationale

Automatic expansion produces inconsistent and difficult-to-reproduce results.

## Exceptions

The user explicitly requests a broader audit.

## Related rule

DL-120
