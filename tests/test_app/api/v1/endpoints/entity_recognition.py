## test_app/api/v1/endpoints/entity_recognition.py
"""
This module contains tests for the entity_recognition endpoint in the app/api/v1/endpoints/entity_recognition.py file.
"""

import unittest
from unittest.mock import patch, MagicMock
from fastapi.testclient import TestClient
from sqlalchemy.orm import Session
from app.main import app
from app.models.schemas.nlp import EntityRecognitionRequest

## SETUP
def get_test_db_override():
    """
    This function returns a mocked DB session for dependency override during tests.
    """
    db = MagicMock(spec=Session)
    return db

app.dependency_overrides[get_db] = get_test_db_override

client = TestClient(app)

## TEST CASES

## Test_EntityRecognitionEndpoint
class TestEntityRecognitionEndpoint(unittest.TestCase):
    """
    This class contains tests for the entity_recognition endpoint.
    """

    ## Test_SuccessfulEntityRecognition
    @patch('app.api.v1.endpoints.entity_recognition.NLPService')
    def test_successful_entity_recognition(self, mock_nlp_service):
        """
        Test the entity_recognition endpoint for a successful entity recognition.
        """
        # Arrange
        test_request_payload = {"text": "Test text for entity recognition."}
        expected_response_payload = {
            "entities": [
                {"text": "Test", "type": "TestType"}
            ]
        }
        mock_nlp_service.return_value.recognize_entities.return_value = expected_response_payload

        # Act
        response = client.post("/entity_recognition", json=test_request_payload)

        # Assert
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), expected_response_payload)

    ## Test_EmptyTextEntityRecognition
    def test_empty_text_entity_recognition(self):
        """
        Test the entity_recognition endpoint with an empty text to ensure it handles empty inputs gracefully.
        """
        # Arrange
        test_request_payload = {"text": ""}
        expected_status_code = 422  # Unprocessable Entity

        # Act
        response = client.post("/entity_recognition", json=test_request_payload)

        # Assert
        self.assertEqual(response.status_code, expected_status_code)

    ## Test_InvalidInputEntityRecognition
    def test_invalid_input_entity_recognition(self):
        """
        Test the entity_recognition endpoint with invalid input to ensure it handles invalid inputs gracefully.
        """
        # Arrange
        test_request_payload = {"invalid_field": "This should fail."}
        expected_status_code = 422  # Unprocessable Entity

        # Act
        response = client.post("/entity_recognition", json=test_request_payload)

        # Assert
        self.assertEqual(response.status_code, expected_status_code)

    ## Test_DatabaseDependencyInjection
    @patch('app.api.v1.endpoints.entity_recognition.get_db', side_effect=get_test_db_override)
    def test_database_dependency_injection(self, mock_get_db):
        """
        Test to ensure that the database dependency is correctly injected into the endpoint.
        """
        # Arrange
        test_request_payload = {"text": "Test text for dependency injection."}
        # No need for an expected response payload as we are testing dependency injection

        # Act
        client.post("/entity_recognition", json=test_request_payload)

        # Assert
        mock_get_db.assert_called_once()

if __name__ == '__main__':
    unittest.main()
