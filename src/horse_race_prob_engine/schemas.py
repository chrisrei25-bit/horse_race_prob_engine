"""schemas.py — Pydantic data models for races, runners, and features.

Phase 0: Minimal stubs. Full schemas to be defined in Phase 1 alongside data ingestion.

Design constraints:
- All fields must reflect what is knowable BEFORE a race starts.
- Do not include post-race fields (finish position, winning time) in pre-race schemas.
- Post-race schemas are separate and only used in backtesting / label pipelines.
"""

from __future__ import annotations

from pydantic import BaseModel


class RunnerSchema(BaseModel):
    """Minimal pre-race runner stub. To be extended in Phase 1."""

    horse_id: str
    race_id: str
    horse_name: str


class RaceSchema(BaseModel):
    """Minimal race stub. To be extended in Phase 1."""

    race_id: str
    runners: list[RunnerSchema]
