# AGENTS.md

## Scope
This file governs everything under tests/.

## Testing rules
- Tests must validate behavior, not implementation trivia.
- Prefer deterministic tests.
- Avoid flaky time-based or network-based tests.
- Do not rely on external APIs.
- Do not rely on live racing data.
- Use small synthetic fixtures where possible.

## Priority coverage
When relevant code exists, prioritize tests for:
- schema validation
- missing-column handling
- backward-looking feature generation
- temporal split correctness
- race-level probability normalization
- prediction output shape
- calibration behavior
- leakage prevention

## Test design rules
- One test should verify one core behavior.
- Use clear names.
- Keep fixtures small and readable.
- Fail loudly on leakage or future-data usage.
- Prefer explicit assertions over snapshot noise.
