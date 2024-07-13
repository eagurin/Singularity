## test_app/core/config.py
"""
This test module is designed to verify the correctness and robustness of the Settings class in the app/core/config.py file.
It uses Python's unittest framework to ensure that all configurations are loaded correctly, with a focus on default values,
environment variable overrides, and the structure of the Settings class itself.
"""

import unittest
from unittest.mock import patch
from app.core.config import Settings

## TestSettingsDefaultValues
class TestSettingsDefaultValues(unittest.TestCase):
    """Test case for default values of the Settings class."""

    def test_default_values(self):
        """Test that default values are correctly set."""
        settings = Settings()
        self.assertEqual(settings.PROJECT_NAME, "NLP Processing API")
        self.assertEqual(settings.PROJECT_VERSION, "1.0.0")
        self.assertEqual(settings.API_PORT, 8000)
        self.assertEqual(settings.DATABASE_URL, "sqlite:///./sql_app.db")
        self.assertEqual(settings.TEST_DATABASE_URL, "sqlite:///./test_sql_app.db")
        self.assertEqual(settings.SPACY_MODEL, "en_core_web_sm")
        self.assertEqual(settings.REDIS_URL, "redis://localhost:6379")
        self.assertEqual(settings.RABBITMQ_URL, "amqp://user:password@localhost")

## TestEnvironmentVariableOverrides
class TestEnvironmentVariableOverrides(unittest.TestCase):
    """Test case for environment variable overrides."""

    @patch.dict('os.environ', {
        "PROJECT_NAME": "Test NLP API",
        "PROJECT_VERSION": "2.0.0",
        "API_PORT": "9000",
        "DATABASE_URL": "postgresql:///prod_db",
        "TEST_DATABASE_URL": "postgresql:///test_db",
        "SPACY_MODEL": "en_core_web_lg",
        "REDIS_URL": "redis://prod:6379",
        "RABBITMQ_URL": "amqp://admin:admin@prod"
    })
    def test_environment_variable_overrides(self):
        """Test that environment variables correctly override default values."""
        settings = Settings(_env_file=None)
        self.assertEqual(settings.PROJECT_NAME, "Test NLP API")
        self.assertEqual(settings.PROJECT_VERSION, "2.0.0")
        self.assertEqual(settings.API_PORT, 9000)
        self.assertEqual(settings.DATABASE_URL, "postgresql:///prod_db")
        self.assertEqual(settings.TEST_DATABASE_URL, "postgresql:///test_db")
        self.assertEqual(settings.SPACY_MODEL, "en_core_web_lg")
        self.assertEqual(settings.REDIS_URL, "redis://prod:6379")
        self.assertEqual(settings.RABBITMQ_URL, "amqp://admin:admin@prod")

## TestConfigCaseSensitivity
class TestConfigCaseSensitivity(unittest.TestCase):
    """Test case for config case sensitivity."""

    def test_case_sensitivity(self):
        """Test that the case sensitivity setting is respected."""
        settings = Settings()
        self.assertTrue(settings.Config.case_sensitive)

if __name__ == '__main__':
    unittest.main()
