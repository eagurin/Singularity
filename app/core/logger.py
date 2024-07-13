import logging
from logging.handlers import RotatingFileHandler
from pathlib import Path

# Define default settings for logger
class LoggerSettings:
    LOG_DIR: str = "logs"
    LOG_FILE: str = "app.log"
    LOG_LEVEL: str = "DEBUG"
    MAX_BYTES: int = 10 * 1024 * 1024  # 10 MB
    BACKUP_COUNT: int = 5
    FORMAT: str = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'

# Ensure the logs directory exists
log_dir = Path(LoggerSettings.LOG_DIR)
log_dir.mkdir(exist_ok=True)

# Define log file path
log_file_path = log_dir / LoggerSettings.LOG_FILE

# Set up the logger
logger = logging.getLogger("NLP Service API")
level = logging.getLevelName(LoggerSettings.LOG_LEVEL)
logger.setLevel(level)

# Create handlers
console_handler = logging.StreamHandler()
file_handler = RotatingFileHandler(log_file_path, maxBytes=LoggerSettings.MAX_BYTES, backupCount=LoggerSettings.BACKUP_COUNT)

# Set level for handlers
console_handler.setLevel(logging.INFO)
file_handler.setLevel(level)

# Create formatters and add them to handlers
formatter = logging.Formatter(LoggerSettings.FORMAT)
console_handler.setFormatter(formatter)
file_handler.setFormatter(formatter)

# Add handlers to the logger
logger.addHandler(console_handler)
logger.addHandler(file_handler)

def setup_logger():
    """
    Function to set up the logger. This function can be called at the start of the application.
    """
    logger.info("Logger is set up.")

# Example usage
if __name__ == "__main__":
    setup_logger()
    logger.debug("This is a debug message")
    logger.info("This is an info message")
    logger.warning("This is a warning message")
    logger.error("This is an error message")
    logger.critical("This is a critical message")
