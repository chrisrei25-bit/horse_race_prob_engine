"""config.py — Load and validate project configuration from YAML files.

Phase 0: Module stub. Config loading logic to be implemented in Phase 1.
"""

from __future__ import annotations

import logging
from pathlib import Path
from typing import Any

logger = logging.getLogger(__name__)

_DEFAULT_CONFIG_PATH = Path("configs/base.yaml")


def load_config(config_path: Path = _DEFAULT_CONFIG_PATH) -> dict[str, Any]:
    """Load configuration from a YAML file.

    Args:
        config_path: Path to the YAML config file.

    Returns:
        Parsed configuration as a dictionary.

    Raises:
        FileNotFoundError: If the config file does not exist.
    """
    raise NotImplementedError("Config loading not yet implemented. Phase 1 task.")
