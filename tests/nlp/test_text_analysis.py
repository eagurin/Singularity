## tests/nlp/test_text_analysis.py

import pytest
from fastapi.testclient import TestClient
from app.main import app
from app.services.text_analysis_service import TextAnalysisService

client = TestClient(app)

@pytest.fixture(scope="module")
def text_analysis_service() -> TextAnalysisService:
    """
    Fixture to provide a TextAnalysisService instance for the tests.
    """
    return TextAnalysisService()

def test_analyze_text(text_analysis_service: TextAnalysisService):
    """
    Test the text analysis functionality.
    """
    text = "This is a test text for analysis."
    result = text_analysis_service.analyze_text(text)
    assert result is not None
    assert "entities" in result
    assert "sentiment" in result

def test_analyze_text_endpoint():
    """
    Test the text analysis endpoint.
    """
    response = client.post('/api/v1/text-analysis/', json={'text': 'This is a test text for analysis.'})
    assert response.status_code == 200
    result = response.json()
    assert "entities" in result
    assert "sentiment" in result
