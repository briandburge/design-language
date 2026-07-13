# Design Language rule reference

This page is the human-readable reference for Design Language v1.0.1. The canonical machine-readable registry remains `rules/rules.yaml`.

| Rule | Title | Category | Severity | Plain-language meaning |
|---|---|---|---|---|
| **DL-001** | Sentence case headings | capitalization | warning | Use sentence case for all editorial and interface headings. |
| **DL-002** | Sentence case UI labels | capitalization | warning | Use sentence case for buttons, navigation, labels, captions, and dialog titles. |
| **DL-003** | Respect proper nouns | capitalization | error | Preserve official capitalization for proper nouns, products, companies, and acronyms. |
| **DL-010** | Oxford comma | punctuation | recommendation | Use the Oxford comma in lists of three or more items. |
| **DL-011** | Avoid em dashes | punctuation | warning | Avoid em dashes in normal editorial copy. Prefer a period, comma, colon, or parentheses. |
| **DL-012** | Use curly quotes | punctuation | recommendation | Use curly quotation marks in published prose. |
| **DL-013** | Use en dashes for ranges | punctuation | recommendation | Use an en dash for numeric and date ranges. |
| **DL-014** | Limit exclamation marks | punctuation | warning | Use exclamation marks rarely and never repeat them. |
| **DL-020** | Number style | numbers | recommendation | Spell out one through nine in body copy. Use numerals for 10 and above. |
| **DL-021** | Numerals with units | numbers | warning | Use numerals with units, measurements, percentages, ages, and time. |
| **DL-022** | Unambiguous dates | dates | warning | Use a written month format for editorial dates. |
| **DL-030** | Parallel lists | lists | warning | Use parallel grammatical structure within a list. |
| **DL-031** | Focused lists | lists | recommendation | Regroup lists longer than seven items when possible. |
| **DL-032** | Descriptive links | links | warning | Use descriptive link text. Avoid generic labels such as Click here. |
| **DL-040** | Active voice | voice | recommendation | Prefer active voice when it makes ownership and action clearer. |
| **DL-041** | Evidence over adjectives | voice | warning | Replace promotional adjectives with facts, behavior, or outcomes. |
| **DL-042** | Concrete language | voice | warning | Prefer concrete nouns and active verbs over abstract corporate language. |
| **DL-043** | Contractions allowed | voice | recommendation | Use natural contractions in normal product and portfolio copy. |
| **DL-050** | One idea per paragraph | structure | warning | Keep each paragraph focused on one main idea. |
| **DL-051** | Paragraph length | structure | recommendation | Review paragraphs longer than four sentences. |
| **DL-052** | Sentence length | structure | recommendation | Review sentences longer than 28 words. |
| **DL-053** | Front-load meaning | structure | recommendation | Lead with the point, outcome, or decision. |
| **DL-054** | Remove repetition | structure | warning | Delete adjacent sentences that repeat the same idea. |
| **DL-060** | Avoid filler transitions | natural-writing | warning | Remove unnecessary transitions such as Additionally, Furthermore, Moreover, Importantly, and That said. |
| **DL-061** | Avoid false contrast | natural-writing | warning | Avoid the formula It is not about X. It is about Y unless the contrast is meaningful. |
| **DL-062** | Avoid empty triads | natural-writing | warning | Avoid generic three-part emphasis and repeated fragment sequences. |
| **DL-063** | Avoid generic openings | natural-writing | error | Avoid broad openings about a fast-paced world, changing technology, or the future of a topic. |
| **DL-064** | Avoid generic conclusions | natural-writing | warning | Avoid Ultimately, In conclusion, and repeated summary endings. |
| **DL-065** | Review inflated language | natural-writing | warning | Review leverage, unlock, harness, elevate, transformative, seamless, world-class, cutting-edge, journey, landscape, ecosystem, and solution. |
| **DL-066** | Preserve specificity | natural-writing | warning | Retain concrete details, constraints, tradeoffs, uncertainty, and author point of view. |
| **DL-070** | Plain language | readability | recommendation | Use the clearest familiar word that preserves meaning. |
| **DL-071** | Reading level | readability | recommendation | Target grade 8 to 10 for general web content. |
| **DL-072** | Inclusive language | accessibility | error | Avoid assumptions about identity, ability, family structure, location, or access. |
| **DL-073** | Meaningful alt text | accessibility | warning | Describe image purpose or information, not every visible detail. |
| **DL-080** | Descriptive headings | headings | warning | Use headings that predict the content below them. |
| **DL-081** | Heading depth | headings | recommendation | Limit heading hierarchy to three levels where practical. |
| **DL-090** | Verb-led buttons | buttons | warning | Use a verb-led label when the action is not obvious from context. |
| **DL-091** | Concise buttons | buttons | recommendation | Keep button labels to one to four words where practical. |
| **DL-092** | Stable navigation labels | navigation | error | Use the same label for the same destination throughout a product or site. |
| **DL-100** | Persistent form labels | forms | error | Do not use placeholder text as the only form label. |
| **DL-101** | Actionable errors | errors | error | Explain what happened and what the user can do next. |
| **DL-102** | No blame | errors | error | Do not blame the user in error messages. |
| **DL-103** | Orient then act | empty-states | warning | Explain the empty state and provide one clear next action. |
| **DL-110** | Role clarity | portfolio | warning | Clarify individual ownership, team contribution, and collaboration. |
| **DL-111** | Outcome integrity | portfolio | error | Use measured outcomes when available and observable outcomes when measurement is unavailable. |
| **DL-120** | Respect audit scope | audit | error | Evaluate only the requested scope unless the user explicitly expands it. |
