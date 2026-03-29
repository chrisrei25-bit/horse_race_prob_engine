# tests/AGENTS.md

## Scope

Rules for all code within the tests/ directory.

## Test constraints

- Tests must not import from outside src/horse_race_prob_engine/ except standard library and dev dependencies
- Do not test implementation details — test observable behavior and contracts
- Do not use random train/test splits in any test involving temporal data
- Do not hardcode expected values derived from post-race information
- Each test file should correspond to a module in src/horse_race_prob_engine/
- Use pytest fixtures for shared setup; do not use setUp/tearDown (unittest style)
- Tests must be runnable with: pytest tests/

## Phase 0 state

No tests exist yet. The tests/ directory is scaffolded only.
Tests will be added in Phase 1 alongside each implemented module.
