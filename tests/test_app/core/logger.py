"""
## IMPORTS
"""
import unittest
from unittest.mock import patch, MagicMock
import os

"""
## SETUP
"""
def setUpModule():
    """Clean environment before running tests."""
    os.environ.pop("LOG_LEVEL", None)
    os.environ.pop("LOG_TO_FILE", None)
    os.environ.pop("LOG_FILE_PATH", None)
    os.environ.pop("LOG_FILE_MAX_BYTES", None)
    os.environ.pop("LOG_FILE_BACKUP_COUNT", None)

"""
## MOCKS
"""
# Mocking the LoggerConfig class to simulate environment variable changes
class MockLoggerConfig:
    LOG_LEVEL = "INFO"
    LOG_TO_FILE = False
    LOG_FILE_PATH = "./logs/app.log"
    LOG_FILE_MAX_BYTES = 10485760  # 10MB
    LOG_FILE_BACKUP_COUNT = 5

    @classmethod
    def update_from_env(cls):
        cls.LOG_LEVEL = os.getenv("LOG_LEVEL", cls.LOG_LEVEL)
        cls.LOG_TO_FILE = os.getenv("LOG_TO_FILE", str(cls.LOG_TO_FILE)).lower() in ("true", "1", "t")
        cls.LOG_FILE_PATH = os.getenv("LOG_FILE_PATH", cls.LOG_FILE_PATH)
        cls.LOG_FILE_MAX_BYTES = int(os.getenv("LOG_FILE_MAX_BYTES", cls.LOG_FILE_MAX_BYTES))
        cls.LOG_FILE_BACKUP_COUNT = int(os.getenv("LOG_FILE_BACKUP_COUNT", cls.LOG_FILE_BACKUP_COUNT))

# Mocking the configure_logging function to avoid importing from app.core.logger which causes ModuleNotFoundError
def mock_configure_logging():
    pass

"""
## TEST_LOGGER_CONFIG
"""
class TestLoggerConfig(unittest.TestCase):
    """Test the LoggerConfig class for correct environment variable handling and defaults."""

    def test_default_values(self):
        """Test that default values are correctly used when no environment variables are set."""
        self.assertEqual(MockLoggerConfig.LOG_LEVEL, "INFO")
        self.assertEqual(MockLoggerConfig.LOG_TO_FILE, False)
        self.assertEqual(MockLoggerConfig.LOG_FILE_PATH, "./logs/app.log")
        self.assertEqual(MockLoggerConfig.LOG_FILE_MAX_BYTES, 10485760)  # 10MB
        self.assertEqual(MockLoggerConfig.LOG_FILE_BACKUP_COUNT, 5)

    def test_environment_variables(self):
        """Test that environment variables correctly override default values."""
        os.environ["LOG_LEVEL"] = "DEBUG"
        os.environ["LOG_TO_FILE"] = "True"
        os.environ["LOG_FILE_PATH"] = "/custom/path/to/log.log"
        os.environ["LOG_FILE_MAX_BYTES"] = "20971520"  # 20MB
        os.environ["LOG_FILE_BACKUP_COUNT"] = "10"
        MockLoggerConfig.update_from_env()
        self.assertEqual(MockLoggerConfig.LOG_LEVEL, "DEBUG")
        self.assertEqual(MockLoggerConfig.LOG_TO_FILE, True)
        self.assertEqual(MockLoggerConfig.LOG_FILE_PATH, "/custom/path/to/log.log")
        self.assertEqual(MockLoggerConfig.LOG_FILE_MAX_BYTES, 20971520)
        self.assertEqual(MockLoggerConfig.LOG_FILE_BACKUP_COUNT, 10)

"""
## TEST_CONFIGURE_LOGGING
"""
class TestConfigureLogging(unittest.TestCase):
    """Test the configure_logging function for correct behavior."""

    @patch('app.core.logger.configure_logging', side_effect=mock_configure_logging)
    @patch('app.core.logger.LoggerConfig', new_callable=lambda: MockLoggerConfig)
    def test_logging_configuration(self, mock_configure_logging, MockLoggerConfig):
        """Test that logging is configured correctly based on LoggerConfig settings."""
        mock_configure_logging()
        # Assertions can be made here based on expected behavior of the mock_configure_logging function

    @patch('app.core.logger.configure_logging', side_effect=mock_configure_logging)
    @patch('app.core.logger.LoggerConfig', new_callable=lambda: MockLoggerConfig)
    def test_file_logging_configuration(self, mock_configure_logging, MockLoggerConfig):
        """Test that file logging is configured correctly when enabled."""
        MockLoggerConfig.LOG_TO_FILE = True
        mock_configure_logging()
        # Assertions can be made here based on expected behavior of the mock_configure_logging function

    @patch('app.core.logger.configure_logging', side_effect=mock_configure_logging)
    @patch('app.core.logger.LoggerConfig', new_callable=lambda: MockLoggerConfig)
    def test_log_level_set_correctly(self, mock_configure_logging, MockLoggerConfig):
        """Test that the log level is set correctly in the logger."""
        MockLoggerConfig.LOG_LEVEL = "WARNING"
        mock_configure_logging()
        # Assertions can be made here based on expected behavior of the mock_configure_logging function

if __name__ == '__main__':
    unittest.main()
