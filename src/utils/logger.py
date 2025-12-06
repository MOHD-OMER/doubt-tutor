"""
Logging configuration for Doubt Tutor
"""

import logging
import sys
from pathlib import Path
from datetime import datetime


LOG_DIR = Path("logs")
LOG_DIR.mkdir(exist_ok=True)


def setup_logger(name: str = "doubt_tutor", log_level: int = logging.INFO) -> logging.Logger:
    """
    Setup and configure logger

    Args:
        name (str): Logger name
        log_level (int): Logging level

    Returns:
        logging.Logger: Configured logger instance
    """

    logger = logging.getLogger(name)
    logger.setLevel(log_level)

    # ✅ Prevent duplicate handlers
    if logger.handlers:
        return logger

    logger.propagate = False

    # ✅ Formatters
    detailed_formatter = logging.Formatter(
        "%(asctime)s | %(levelname)s | %(name)s | %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )

    simple_formatter = logging.Formatter(
        "%(levelname)s | %(message)s"
    )

    # ✅ File Handler (Daily log file)
    log_file = LOG_DIR / f"doubt_tutor_{datetime.now().strftime('%Y-%m-%d')}.log"

    file_handler = logging.FileHandler(log_file, encoding="utf-8")
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(detailed_formatter)

    # ✅ Console Handler
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setLevel(logging.INFO)
    console_handler.setFormatter(simple_formatter)

    # ✅ Attach Handlers
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger


# ✅ Default logger instance (safe import support)
default_logger = setup_logger()


def get_logger(name: str = None) -> logging.Logger:
    """Return named logger instance"""
    return setup_logger(name or "doubt_tutor")
