# Design Language Auditor GPT 1.0.1

This directory records the configuration published for Design Language Auditor GPT 1.0.1.

## Release metadata

| Field | Value |
| --- | --- |
| Design Language version | 1.0.1 |
| GPT version | 1.0.1 |
| Publication date | July 12, 2026 |
| Configuration captured | July 13, 2026 |
| Public GPT | [Design Language Auditor](https://chatgpt.com/g/g-6a52996c067481919f69cde33a25b22d-design-language-auditor) |
| Repository | [briandburge/design-language](https://github.com/briandburge/design-language) |

## Published configuration

- [`instructions.md`](instructions.md) contains the exact GPT instructions.
- [`conversation-starters.md`](conversation-starters.md) contains the published conversation starters.
- [`rendered-url-action.openapi.yaml`](rendered-url-action.openapi.yaml) contains the Rendered URL Reader Action schema.
- [`knowledge/`](knowledge/) contains the five uploaded knowledge files.

## External Action

The Rendered URL Reader Action sends the exact public URL being audited to `https://r.jina.ai`. Authentication is set to none. The configured privacy policy is https://jina.ai/legal/.

The Action is used only when normal retrieval is incomplete or a page depends on JavaScript. GPT instructions preserve the requested audit scope and prohibit bypassing access controls.

## Known limitation

Rendered URL Reader availability, rate limits, access controls, and page structure can affect retrieval completeness.
