# Repository instructions

This repository contains Design Language, a portable editorial and interface language system for human and AI-assisted workflows.

## Canonical sources

- `rules/rules.yaml` defines canonical rules.
- `spec/` explains rationale, examples, and exceptions.
- `audit/` defines audit behavior, scoring, and report format.
- `decisions/` records accepted decisions.
- `docs/` preserves project context, roadmap, and active sprint plans.

## Working principles

- Preserve stable rule IDs.
- Do not duplicate canonical rules in adapters.
- Use sentence case for headings.
- Avoid em dashes in normal prose.
- Separate audit from rewrite.
- Respect the user-defined audit scope.
- Update the changelog when behavior changes.
- Run `python scripts/validate.py` before committing.

## Git workflow

- Work on feature branches.
- Do not commit directly to `main`.
- Show the diff and validation results before committing.
- Do not push or merge without explicit approval.

## Required reading before substantial work

- `docs/project-charter.md`
- `docs/vision.md`
- `docs/non-goals.md`
- `docs/roadmap.md`
- `docs/sprint-1.md`
- `docs/custom-gpt-release-process.md`

Do not optimize short-term work in a way that undermines the 2.0 vision.

## Custom GPT release discipline

Every DSL version update must include a Custom GPT impact review and regeneration of all five knowledge files.
