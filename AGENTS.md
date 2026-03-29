# AGENTS.md

## Purpose

This repository is for a production-grade horse race probability engine.

The system goal is to estimate calibrated pre-race win probabilities for each horse in a race.

This is not a toy predictor, not a gambling gimmick, and not a simulation-first project.

## Mandatory operating rules

- Obey the user's prompt exactly.

- Obey more deeply nested AGENTS.md files when working inside their scope.

- Do not invent requirements that are not explicitly stated.

- Do not silently change architecture.

- Do not introduce placeholder logic disguised as finished code.

- Do not claim any formula is "official" unless that is explicitly documented in the repo.

- Do not hardcode a fake universal handicapping formula.

- Do not use future information in historical features.

- Do not use random train/test splits for temporal racing data.

- Do not use post-race information as pre-race features.

- Do not use final odds in pre-race prediction code unless a separate value-analysis path explicitly allows it.

- Keep the project modular, typed where reasonable, and testable.

- Prefer correctness over cleverness.

- Prefer transparency over black-box complexity.

- Prefer small, composable files over monolithic scripts.

## Project scope

The core system should eventually include:

- schema standardization

- data ingestion and mapping

- leakage-safe feature engineering

- race-level modeling

- probability calibration

- walk-forward backtesting

- explainability

- CLI access

- tests

## Out of scope unless explicitly requested

- web UI

- mobile app

- browser automation

- unrelated simulators

- betting exchange execution

- cloud deployment

- infra-as-code

- real-money wagering automation

## Development standards

- Python 3.11+

- Use src/ layout

- Use configuration files rather than hardcoded constants where practical

- Use logging, not print, in library code

- Keep I/O separated from feature logic and modeling logic

- Add docstrings to non-trivial public functions

- Minimize dependencies

- Every added dependency must be justified by clear use

## Data and modeling constraints

- All time-dependent features must be strictly backward-looking

- Every race must be handled as a group context, not as independent rows only

- Win probabilities must be normalized at the race level

- Calibration is a first-class requirement, not an optional extra

- Distinguish clearly between:

  1. most likely winner

    2. fair probability

      3. betting value

      - If BHA-style logic is added, treat it as an approximation feature layer, not an official rating engine

      ## Execution rules

      Before finishing any coding task that changes files:

      - run the relevant tests

      - run lint/type/format checks if configured

      - verify imports

      - verify no obvious leakage was introduced

      - verify changed files remain within architectural boundaries

      ## Response rules

      When reporting completion:

      - state exactly what changed

      - state what was not changed

      - state any assumptions

      - state any unresolved risks

      - do not exaggerate confidence
      
