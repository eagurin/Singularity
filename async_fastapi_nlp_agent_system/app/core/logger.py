## app/core/logger.py
import logging
from logging.handlers import RotatingFileHandler
import os
from fastapi.logger import logger as fastapi_logger

class LoggerConfig:
    """Logger configuration class."""
    LOG_LEVEL: str = os.getenv("LOG_LEVEL", "INFO").upper()
    LOG_TO_FILE: bool = os.getenv("LOG_TO_FILE", "False").lower() in ("true", "1", "t")
    LOG_FILE_PATH: str = os.getenv("LOG_FILE_PATH", "./logs/app.log")
    LOG_FILE_MAX_BYTES: int = int(os.getenv("LOG_FILE_MAX_BYTES", "10485760"))  # 10MB
    LOG_FILE_BACKUP_COUNT: int = int(os.getenv("LOG_FILE_BACKUP_COUNT", "5"))

def configure_logging():
    """
    Configures the logging.
    This function sets up logging to file if configured, and sets the log level.
    """
    log_level = getattr(logging, LoggerConfig.LOG_LEVEL)

    # Configure root logger
    logging.basicConfig(level=log_level)
    root_logger = logging.getLogger()

    if LoggerConfig.LOG_TO_FILE:
        # Ensure log directory exists
        os.makedirs(os.path.dirname(LoggerConfig.LOG_FILE_PATH), exist_ok=True)

        # Add rotating file handler
        file_handler = RotatingFileHandler(
            LoggerConfig.LOG_FILE_PATH,
            maxBytes=LoggerConfig.LOG_FILE_MAX_BYTES,
            backupCount=LoggerConfig.LOG_FILE_BACKUP_COUNT
        )
        file_handler.setLevel(log_level)
        formatter = logging.Formatter(
            "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
        )
        file_handler.setFormatter(formatter)
        root_logger.addHandler(file_handler)

    # Configure FastAPI logger to use the same configuration as the root logger
    fastapi_logger.handlers = root_logger.handlers
    fastapi_logger.setLevel(log_level)

# Call the configure_logging function to configure the logger at the module level
configure_logging()
