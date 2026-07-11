import logging
import os


def setup_logger():
    # Create logs folder if it does not exist
    os.makedirs("logs", exist_ok=True)

    # Create logger
    logger = logging.getLogger("trading_bot")
    logger.setLevel(logging.INFO)

    # Prevent duplicate logs
    if logger.handlers:
        return logger

    # Create file handler
    file_handler = logging.FileHandler(
        "logs/trading.log"
    )

    # Define log format
    formatter = logging.Formatter(
        "%(asctime)s - %(levelname)s - %(message)s"
    )

    file_handler.setFormatter(formatter)

    # Add handler to logger
    logger.addHandler(file_handler)

    return logger
    