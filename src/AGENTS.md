# src/AGENTS.md

## Scope

Rules for all code within the src/ directory.

## Additional constraints for src/

- Use the src layout: all importable code lives under src/horse_race_prob_engine/
- All modules must be importable without side effects
- Do not place scripts, notebooks, or data files inside src/
- Each subpackage (data, features, modeling, api, utils) has a single responsibility
- Keep __init__.py files minimal — only re-export what is explicitly needed
- Do not import between sibling subpackages except through clearly defined interfaces
- Type annotations are required on all public function signatures
- No hardcoded paths — use config objects loaded from configs/

## Subpackage responsibilities

- horse_race_prob_engine/config.py — load and validate YAML configs
- horse_race_prob_engine/schemas.py — Pydantic data models for races, runners, features
- horse_race_prob_engine/logging_config.py — configure logging for the library
- horse_race_prob_engine/utils/ — shared utilities (no domain logic)
- horse_race_prob_engine/data/ — ingestion and I/O only, no feature logic
- horse_race_prob_engine/features/ — feature engineering, strictly no I/O or modeling
- horse_race_prob_engine/modeling/ — model training, calibration, prediction
- horse_race_prob_engine/api/ — CLI or internal API surface only
