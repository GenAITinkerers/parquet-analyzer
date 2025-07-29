"""
Utility functions for anomaly detection module.
This module sets up following:
    1) the logging configuration.
"""

import logging
from parquet.config import get_config

CONFIG = get_config()


def setup_logger(name=__name__, level=logging.INFO) -> logging.Logger:
    logger = logging.getLogger(name)
    logger.setLevel(level)

    # Clear existing handlers
    if logger.hasHandlers():
        logger.handlers.clear()

    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(name)s -%(lineno)s - %(message)s')

    ch = logging.StreamHandler()
    ch.setLevel(level)
    ch.setFormatter(formatter)

    logger.addHandler(ch)
    return logger

# LOGGER = setup_logger(__name__, logging.INFO)

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




