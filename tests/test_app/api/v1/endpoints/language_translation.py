## test_app/api/v1/endpoints/language_translation.py
"""
This module contains tests for the language_translation endpoint in the app/api/v1/endpoints/language_translation.py file.
"""

import unittest
from unittest.mock import patch
from fastapi.testclient import TestClient
from sqlalchemy.orm import Session
from app.main import app
from app.models.schemas.nlp import LanguageTranslationRequest

## SETUP
client = TestClient(app)

## <TEST_CASES>

## Test Language Translation Endpoint
class TestLanguageTranslationEndpoint(unittest.TestCase):
    @patch('app.api.v1.endpoints.language_translation.get_db')
    @patch('app.api.v1.endpoints.language_translation.NLPService')
    def test_perform_language_translation(self, mock_nlp_service, mock_get_db):
        """
        Test the /language_translation endpoint for successful translation.
        """
        # Setup mock objects
        mock_db_session = Session()
        mock_get_db.return_value = mock_db_session
        mock_nlp_service_instance = mock_nlp_service.return_value
        mock_nlp_service_instance.translate_text.return_value = "translated text"

        # Define test data
        test_request_data = {
            "text": "test text",
            "target_language": "fr"
        }

        # Perform test
        response = client.post("/language_translation", json=test_request_data)

        # Assertions
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"translated_text": "translated text"})
        mock_nlp_service_instance.translate_text.assert_called_once_with("test text", "fr")

    @patch('app.api.v1.endpoints.language_translation.get_db')
    @patch('app.api.v1.endpoints.language_translation.NLPService')
    def test_perform_language_translation_with_invalid_data(self, mock_nlp_service, mock_get_db):
        """
        Test the /language_translation endpoint with invalid request data.
        """
        # Setup mock objects
        mock_db_session = Session()
        mock_get_db.return_value = mock_db_session

        # Define test data with missing 'target_language'
        test_request_data = {
            "text": "test text"
        }

        # Perform test
        response = client.post("/language_translation", json=test_request_data)

        # Assertions
        self.assertNotEqual(response.status_code, 200)
        self.assertTrue("detail" in response.json())

    @patch('app.api.v1.endpoints.language_translation.get_db')
    @patch('app.api.v1.endpoints.language_translation.NLPService')
    def test_perform_language_translation_with_empty_text(self, mock_nlp_service, mock_get_db):
        """
        Test the /language_translation endpoint with empty 'text' field.
        """
        # Setup mock objects
        mock_db_session = Session()
        mock_get_db.return_value = mock_db_session

        # Define test data with empty 'text'
        test_request_data = {
            "text": "",
            "target_language": "fr"
        }

        # Perform test
        response = client.post("/language_translation", json=test_request_data)

        # Assertions
        self.assertNotEqual(response.status_code, 200)
        self.assertTrue("detail" in response.json())

## <RUN_TESTS>
if __name__ == '__main__':
    unittest.main()
