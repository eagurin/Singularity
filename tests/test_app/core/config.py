## IMPORTS
import unittest
from unittest.mock import patch
from pydantic import ValidationError

## TEST SETTINGS
class TestSettings(unittest.TestCase):
    ## SETUP
    def setUp(self) -> None:
        self.default_values = {
            "PROJECT_NAME": "NLP Processing API",
            "PROJECT_VERSION": "1.0.0",
            "API_PORT": 8000,
            "DATABASE_URL": "sqlite:///./sql_app.db",
            "TEST_DATABASE_URL": "sqlite:///./test_sql_app.db",
            "SPACY_MODEL": "en_core_web_sm",
        }

    ## TEST_DEFAULT_VALUES
    def test_default_values(self):
        """Test that default values are correctly set."""
        with patch.dict('os.environ', {}, clear=True):
            from app.core.config import settings
            for attr, expected in self.default_values.items():
                with self.subTest(attr=attr):
                    self.assertEqual(getattr(settings, attr), expected)

    ## TEST_ENVIRONMENT_OVERRIDES
    def test_environment_overrides(self):
        """Test that environment variables override default values."""
        env_vars = {
            "PROJECT_NAME": "Test NLP API",
            "PROJECT_VERSION": "2.0.0",
            "API_PORT": "9000",
            "DATABASE_URL": "sqlite:///./test_db.db",
            "TEST_DATABASE_URL": "sqlite:///./real_test_db.db",
            "SPACY_MODEL": "en_core_web_lg",
        }
        with patch.dict('os.environ', env_vars):
            from app.core.config import settings
            for attr, expected in env_vars.items():
                with self.subTest(attr=attr):
                    self.assertEqual(str(getattr(settings, attr)), expected)

    ## TEST_INVALID_API_PORT
    def test_invalid_api_port(self):
        """Test that an invalid API_PORT raises a ValidationError."""
        with patch.dict('os.environ', {"API_PORT": "not_a_number"}):
            with self.assertRaises(ValidationError):
                from app.core.config import Settings
                Settings()

    ## TEST_INVALID_TYPE
    def test_invalid_type(self):
        """Test that assigning an invalid type to a field raises a ValidationError."""
        with patch.dict('os.environ', {"API_PORT": "[8000]"}):  # Using a list instead of an int
            with self.assertRaises(ValidationError):
                from app.core.config import Settings
                Settings()

    ## TEST_CASE_SENSITIVITY
    def test_case_sensitivity(self):
        """Test that environment variable names are case-sensitive."""
        with patch.dict('os.environ', {"api_port": "8001"}):
            from app.core.config import settings
            self.assertNotEqual(settings.API_PORT, 8001)
            self.assertEqual(settings.API_PORT, 8000)  # Default value

if __name__ == '__main__':
    unittest.main()
