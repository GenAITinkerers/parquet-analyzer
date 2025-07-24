"""
Utility functions for anomaly detection module.
This module sets up following:
    1) the logging configuration.
"""

import logging
# from parquet.config import get_config
from config import get_config

CONFIG = get_config()

def setup_logger():
    """Setup default logging, call at the start of program."""
    log_handler = logging.StreamHandler()
    logging.basicConfig(
        format="[{asctime},{msecs:03.0f}] {levelname} {name}.{lineno}| {message}",
        datefmt="%H:%M:%S",
        style="{",
        handlers=[log_handler],
    )
    print(f"Setting log level to {CONFIG.LOGLEVEL}")
    logging.getLogger("anomaly").setLevel(CONFIG.LOGLEVEL)
    print(f"Logger level set to {CONFIG.LOGLEVEL}")

LOGGER = logging.getLogger(__name__)
LOGGER.info("Logger setup complete.")
LOGGER.debug("This is a debug message.")

if __name__ == "__main__":
    from pathlib import Path
    print("current working directory:", Path.cwd())
    # If this module is run directly, set up the logger
    CONFIG = get_config()
    print("Config level:", CONFIG.LOGLEVEL)
    setup_logger()
    LOGGER = logging.getLogger(__name__)
    print("Logger name:", LOGGER.name)
    print("Logger level:", LOGGER.level)
    LOGGER.info("Logger setup complete.")
    LOGGER.debug("This is a debug message.")




