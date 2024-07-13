from fastapi.testclient import TestClient
from app.main import app
from app.services.intent_classification_service import IntentClassificationService
import pytest

client = TestClient(app)

@pytest.fixture(scope="module")
def intent_classification_service() -> IntentClassificationService:
    """
    Fixture to provide an IntentClassificationService instance for the tests.
    """
    return IntentClassificationService()

def test_classify_intent(intent_classification_service: IntentClassificationService):
    """
    Test the intent classification functionality.
    """
    text = "Book a flight to New York"
    result = intent_classification_service.classify_intent(text)
    assert result is not None
    assert "intent" in result
    assert result["intent"] == "BookFlight"

def test_classify_intent_endpoint():
    """
    Test the intent classification endpoint.
    """
    response = client.post('/api/v1/intent-classification/', json={'text': 'Book a flight to New York'})
    assert response.status_code == 200
    result = response.json()
    assert "intent" in result
    assert result["intent"] == "BookFlight"
