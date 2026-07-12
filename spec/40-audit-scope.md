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
