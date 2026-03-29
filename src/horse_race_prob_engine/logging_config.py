"""logging_config.py — Configure logging for the horse_race_prob_engine library.

Call setup_logging() once at application entry point.
Library code should only use logging.getLogger(__name__) and never call setup_logging().
"""

from __future__ import annotations

import logging
import os


def setup_logging(level: str | None = None) -> None:
    """Configure root logger for the project.

    Args:
        level: Log level string (DEBUG, INFO, WARNING, ERROR).
               Defaults to LOG_LEVEL env var, or INFO if not set.
    """
    resolved_level = level or os.getenv("LOG_LEVEL", "INFO")
    numeric_level = getattr(logging, resolved_level.upper(), logging.INFO)

    logging.basicConfig(
        level=numeric_level,
        format="%(asctime)s | %(levelname)-8s | %(name)s | %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )
    logging.getLogger(__name__).debug("Logging configured at level: %s", resolved_level)
