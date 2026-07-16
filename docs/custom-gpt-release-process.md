# Custom GPT release process

The Design Language Auditor Custom GPT must remain aligned with every DSL release.

## Required release review

Compare changes to:

- `rules/rules.yaml`
- `rules/terms.yaml`
- `spec/`
- `audit/`
- `examples/`
- `decisions/`
- GPT instructions
- conversation starters
- displayed DSL version

## Knowledge bundle

Regenerate and replace all five files for every release. Store the published files under `gpt/versions/<version>/knowledge/`:

- `dsl-rules.yaml`
- `dsl-specification.md`
- `dsl-audit-guide.md`
- `dsl-examples.md`
- `dsl-terms.yaml`

## Instructions and starters

Update GPT instructions whenever audit behavior, scope handling, scoring, report structure, rewrite behavior, or feedback behavior changes.

Review conversation starters for every new capability.

Store the exact published instructions, conversation starters, action schema, and release metadata under `gpt/versions/<version>/`.

## Release checklist

1. Update the displayed DSL version.
2. Replace all five knowledge files.
3. Replace instructions when behavior changed.
4. Review conversation starters.
5. Test document, website, navigation, AI-pattern, and rewrite workflows.
6. Confirm valid rule IDs.
7. Confirm the GPT does not rewrite during an audit.
8. Confirm the GPT reports its actual scope.
9. Store the exact published GPT configuration under `gpt/versions/<version>/`.
10. Publish the GPT update.
11. Record the GPT release in `CHANGELOG.md`.

## Release record

Record DSL version, GPT version, publication date, knowledge bundle version, instruction version, major changes, known limitations, and the Custom GPT URL.

## Custom GPT URL

https://chatgpt.com/g/g-6a52996c067481919f69cde33a25b22d-design-language-auditor


## Current public GPT

Design Language Auditor

https://chatgpt.com/g/g-6a52996c067481919f69cde33a25b22d-design-language-auditor
