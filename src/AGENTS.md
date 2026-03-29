# AGENTS.md

## Scope
This file governs everything under src/.

## Code rules
- Write production-oriented Python, not notebook-style code.
- Keep functions small and single-purpose.
- Avoid hidden side effects.
- Prefer pure functions unless state is required.
- Use explicit inputs and outputs.
- Avoid global mutable state.
- Do not bury business logic inside CLI code.
- Do not mix feature engineering with model training in the same file.
- Do not mix schema definitions with runtime prediction logic.

## Architecture rules
Preserve these boundaries:
- config.py for configuration loading and validation
- schemas.py for canonical data schema definitions
- logging_config.py for logging setup only
- utils/ for generic reusable helpers
- data/ for ingestion, mapping, preprocessing
- features/ for leakage-safe feature generation
- modeling/ for dataset building, training, prediction, calibration, evaluation, backtesting, explainability
- api/ for CLI and thin orchestration only

## Modeling rules
- Every feature must be justifiable as available before post time
- Every rolling feature must be backward-looking
- Every race-aware calculation must preserve race grouping
- Probability outputs must sum sensibly within a race
- Calibration must not be skipped once prediction code exists
- Do not present ranking scores as calibrated probabilities unless calibration is actually performed

## Dependency rules
- Prefer standard library where practical
- Prefer pydantic, pandas, numpy, scikit-learn, pyyaml, typer, pytest
- Do not add heavyweight frameworks unless explicitly requested
- Do not add deep learning libraries in early phases unless specifically requested

## Implementation discipline
When adding new code:
- update imports cleanly
- avoid dead code
- avoid commented-out blocks
- avoid TODO clutter
- do not leave fake stub returns except where explicitly marked and documented

## Documentation inside code
For any non-trivial function, document:
- purpose
- inputs
- outputs
- leakage or temporal assumptions if relevant
