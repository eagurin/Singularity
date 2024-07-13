from fastapi.testclient import TestClient
from app.main import app
from app.services.entity_recognition_service import EntityRecognitionService
import pytest

client = TestClient(app)

@pytest.fixture(scope="module")
def entity_recognition_service() -> EntityRecognitionService:
    """
    Fixture to provide an EntityRecognitionService instance for the tests.
    """
    return EntityRecognitionService()

def test_recognize_entities(entity_recognition_service: EntityRecognitionService):
    """
    Test the entity recognition functionality.
    """
    text = "Barack Obama was the 44th President of the United States."
    result = entity_recognition_service.recognize_entities(text)
    assert result is not None
    assert "entities" in result
    assert any(entity["entity"] == "PERSON" and entity["text"] == "Barack Obama" for entity in result["entities"])

def test_recognize_entities_endpoint():
    """
    Test the entity recognition endpoint.
    """
    response = client.post('/api/v1/entity-recognition/', json={'text': 'Barack Obama was the 44th President of the United States.'})
    assert response.status_code == 200
    result = response.json()
    assert "entities" in result
    assert any(entity["entity"] == "PERSON" and entity["text"] == "Barack Obama" for entity in result["entities"])
