from pathlib import Path
import json
import re
import sys

root = Path(__file__).resolve().parents[1]
errors = []

required = [
    'README.md',
    'CHANGELOG.md',
    'AGENTS.md',
    'rules/rules.yaml',
    'audit/rubric.md',
    'audit/report-template.md',
    'audit/prompts/website-audit.md',
    'schemas/rules.schema.json',
    'spec/40-audit-scope.md',
    'decisions/0004-respect-audit-scope.md',
    'docs/project-context.md',
    'docs/project-charter.md',
    'docs/vision.md',
    'docs/non-goals.md',
    'docs/custom-gpt-release-process.md',
    'docs/roadmap.md',
    'docs/sprint-1.md',
]

for item in required:
    if not (root / item).exists():
        errors.append(f'Missing required file: {item}')

rules_text = (root / 'rules/rules.yaml').read_text(encoding='utf-8')
ids = re.findall(r'^  - id: (DL-\d{3})$', rules_text, re.M)

if len(ids) != len(set(ids)):
    errors.append('Duplicate rule IDs found')

if not ids:
    errors.append('No rule IDs found')

if 'DL-120' not in ids:
    errors.append('DL-120 is missing')

versions = {
    'rules': re.search(r'^version:\s*(\d+\.\d+\.\d+)', rules_text, re.M),
    'readme': re.search(r'Current version:\s*`(\d+\.\d+\.\d+)`', (root / 'README.md').read_text(encoding='utf-8')),
}

for key, match in versions.items():
    if not match:
        errors.append(f'Could not determine version from {key}')

resolved = {key: match.group(1) for key, match in versions.items() if match}
if len(set(resolved.values())) > 1:
    errors.append(f'Version mismatch: {resolved}')

try:
    json.loads((root / 'schemas/rules.schema.json').read_text(encoding='utf-8'))
except Exception as exc:
    errors.append(f'Invalid JSON schema: {exc}')

if errors:
    print('\n'.join(errors))
    sys.exit(1)

print(f'Validation passed: {len(ids)} rules found. Version {next(iter(resolved.values()))}.')
