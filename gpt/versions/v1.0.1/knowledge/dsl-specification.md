<!-- Source: spec/00-principles.md -->

# Principles

## Language is interface

Words are part of the product. They influence understanding, confidence, and trust.

## Clarity before cleverness

Write to communicate, not to impress. Rewrite anything that exists mainly to sound intelligent.

## Systems over style

Consistency creates recognition. Reusable patterns matter more than ornamental prose.

## Evidence over adjectives

Prefer observable facts, behavior, and outcomes. Avoid telling readers how impressive something is.

## Reduce noise

Every unnecessary word competes with the important ones. Delete before adding.

## Write for scanning

Readers search before they read. Make hierarchy visible and front-load useful information.

## AI should amplify authorship

AI should help express intent. It should not replace specificity with generic fluency.

---

<!-- Source: spec/01-capitalization.md -->

# Capitalization

## Intent

Create a consistent, modern SaaS-style hierarchy across editorial and interface content.

## Specification

Use sentence case for page titles, headings, navigation, buttons, form labels, cards, dialogs, captions, and notifications.

Capitalize proper nouns and official product names according to their source conventions.

## Preferred

- Design operations at scale
- View case study
- Email address
- Game Center

## Avoid

- Design Operations at Scale
- View Case Study
- Email Address
- Game center

## Exceptions

Brand marks, legal names, acronyms, and quoted source material may retain official capitalization.

---

<!-- Source: spec/02-punctuation.md -->

# Punctuation

## Commas

Use the Oxford comma in a series of three or more items.

## Dashes

Use hyphens for compound modifiers and en dashes for ranges. Avoid em dashes in normal editorial copy. Prefer a period, comma, colon, or parentheses.

## Quotes

Use curly quotation marks in published copy. Use straight quotes in source code and machine-readable files.

## Ellipses

Use a single ellipsis character only when text intentionally trails off or material is omitted. Do not use three periods as decoration.

## Exclamation marks

Use rarely. One is enough.

## Colons

Use a colon to introduce a list, explanation, or consequence when the preceding clause is complete.

---

<!-- Source: spec/03-numbers-dates.md -->

# Numbers and dates

## Numbers

Spell out one through nine in body copy. Use numerals for 10 and above.

Always use numerals with units, measurements, ages, percentages, time, and interface constraints.

## Percentages

Use the percent symbol with numerals: `37%`.

## Dates

Use `July 11, 2026` in US-facing editorial content. Avoid ambiguous numeric dates such as `7/11/26`.

## Ranges

Use an en dash for ranges: `2022–2026` and `10–15 minutes`.

---

<!-- Source: spec/04-lists-links.md -->

# Lists and links

## Lists

Use parallel grammatical structure. Begin each item with the same type of word or phrase.

Use sentence punctuation when list items are complete sentences. Omit terminal punctuation for short fragments.

Keep lists focused. Seven items is a useful maximum before regrouping.

## Links

Use descriptive link text that explains the destination or action.

Preferred: `Read the case study`

Avoid: `Click here`

---

<!-- Source: spec/10-voice.md -->

# Voice

## Core traits

- calm
- direct
- grounded
- specific
- professional without sounding corporate

## Behavior

Use active voice where it improves clarity. Use contractions in normal product and portfolio copy.

Prefer concrete nouns and active verbs. Avoid inflated claims, ceremonial language, and self-congratulation.

## Evidence over adjectives

Preferred: `Reduced onboarding time by 37%.`

Avoid: `Created an innovative, transformative onboarding experience.`

---

<!-- Source: spec/11-editorial-structure.md -->

# Editorial structure

## Front-load meaning

Lead with the point, outcome, or decision. Add context afterward.

## Paragraphs

Use one main idea per paragraph. Aim for two to three sentences. Use four as a practical maximum unless the content requires continuity.

## Sentences

Aim for 12 to 18 words on average. Review sentences longer than 28 words.

## Headings

Use descriptive headings that help readers predict the content below them.

## Repetition

Remove sentences that repeat or summarize the sentence immediately before them without adding meaning.

---

<!-- Source: spec/12-readability-accessibility.md -->

# Readability and accessibility

## Plain language

Use familiar words when they are equally precise. Explain specialist terms when the audience may not know them.

## Reading level

Target approximately grade 8 to 10 for general web content. Technical specifications may exceed this when precision requires it.

## Inclusive language

Avoid assumptions about identity, ability, family structure, location, or access.

## Alt text

Describe the information or purpose of an image, not every visible detail. Omit decorative images from the accessibility tree when the platform supports it.

## Instructions

Do not rely on color, position, or visual appearance alone. Name the control or action.

---

<!-- Source: spec/20-natural-writing.md -->

# Natural writing

## Intent

Reduce patterns commonly associated with generic AI-generated or over-produced marketing copy.

## Avoid formulaic contrast

Avoid `It is not about X. It is about Y.` unless the contrast reveals a real distinction.

## Avoid empty triads

Avoid repetitive three-part emphasis such as `Simple. Powerful. Effortless.` Use a specific claim instead.

## Avoid filler transitions

Delete transitions such as `Additionally`, `Furthermore`, `Moreover`, `Importantly`, and `That said` when the relationship is already clear.

## Avoid generic openings

Do not open with phrases such as `In today's fast-paced world` or `As technology continues to evolve`.

## Avoid generic endings

Do not end sections with `Ultimately`, `In conclusion`, or a summary that repeats the paragraph.

## Avoid inflated verbs and nouns

Review words such as `leverage`, `unlock`, `harness`, `elevate`, `transform`, `journey`, `landscape`, `ecosystem`, and `solution`.

These words are not always forbidden. They require specific meaning.

## Vary rhythm without performing

Avoid a sequence of one-line fragments or repeated sentence openings unless the rhythm serves a clear purpose.

## Preserve human specificity

Keep concrete details, uncertainty, constraints, tradeoffs, and point of view. Generic fluency is not a substitute for authorship.

---

<!-- Source: spec/30-headings.md -->

# Headings

## Purpose

Headings describe structure and help readers scan.

## Specification

- Use sentence case.
- Keep headings concise and descriptive.
- Use nouns or active phrases.
- Avoid punctuation unless the heading is a question.
- Limit hierarchy to three levels where practical.

## Preferred

- What changed
- Measuring adoption
- How the system works

## Avoid

- Overview
- More information
- Measuring Adoption
- What Changed!

---

<!-- Source: spec/31-buttons-navigation.md -->

# Buttons and navigation

## Buttons

Use sentence case. Start with a verb when the action is not already obvious.

Aim for one to four words.

Preferred:

- Save changes
- View project
- Download PDF

Avoid:

- Click here
- Submit form
- LEARN MORE

## Navigation

Use short, stable nouns. Do not change labels between pages when the destination is the same.

---

<!-- Source: spec/32-forms-errors-empty-states.md -->

# Forms, errors, and empty states

## Form labels

Use direct nouns or noun phrases. Do not use placeholder text as the only label.

## Help text

Explain format or consequence before the user makes an error.

## Errors

State what happened and what the user can do next. Do not blame the user.

Preferred: `We could not save your changes. Check your connection and try again.`

Avoid: `Invalid request.`

## Empty states

Orient the user, explain why the space is empty when useful, and provide one clear next action.

---

<!-- Source: spec/33-case-studies-portfolios.md -->

# Case studies and portfolios

## Structure

Use this default sequence:

1. Context
2. Challenge
3. Approach
4. Outcome
5. Reflection

## Evidence

Lead with decisions, constraints, collaboration, and outcomes. Avoid broad claims about passion, innovation, or leadership without evidence.

## Role clarity

State what you owned, what the team owned, and where collaboration shaped the result.

## Outcomes

Use measurable outcomes when available. When measurement is unavailable, describe observable changes without inventing precision.

---

<!-- Source: spec/40-audit-scope.md -->

# Audit scope

## Intent

Ensure audits are predictable, reproducible, and limited to the user's requested scope.

## Specification

A supplied source defines the default audit scope.

Unless the user explicitly requests broader coverage:

- Audit only the supplied source.
- Do not expand the scope automatically.
- Do not search for additional related content.
- Report exactly what was reviewed.

When the requested scope is ambiguous, ask one clarifying question before beginning.

## Website audits

Supported scopes:

- Single page
- Navigation crawl
- Site section
- Entire website

A navigation crawl may follow only internal links that are directly reachable from the supplied page.

An entire-site audit requires explicit user approval.

## Audit report

Every website audit must report:

- Source
- Scope
- Pages reviewed
- Navigation followed

## Rationale

Audit quality depends on predictable scope.

Expanding the scope without user intent reduces reproducibility and introduces unrelated findings.

## Good

- Audit only the supplied page when the user provides one URL.
- List each page reviewed during a navigation crawl.
- Ask which scope the user wants when the request is ambiguous.

## Avoid

- Searching the public web for related pages.
- Following unrelated search results.
- Claiming an entire site was reviewed when only a sample was inspected.

## Exceptions

The user explicitly requests broader coverage.

## AI notes

Do not search the public web for additional pages unless the user explicitly requests a broader review.

State exactly which pages were reviewed.

## Related rules

- DL-120
