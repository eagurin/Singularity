## IMPORTS
import sys
sys.path.append('/data')
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from unittest import TestCase, main
from app.main import app
from app.core.config import settings
from app.models import Base

## SETUP
DATABASE_URL = settings.TEST_DATABASE_URL
engine = create_engine(DATABASE_URL)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def override_get_db():
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()

app.dependency_overrides[get_db] = override_get_db

client = TestClient(app)

## <SECTION_NAME>: TestSentimentAnalysisEndpoint
class TestSentimentAnalysisEndpoint(TestCase):
    @classmethod
    def setUpClass(cls):
        Base.metadata.create_all(bind=engine)

    @classmethod
    def tearDownClass(cls):
        Base.metadata.drop_all(bind=engine)

    def test_perform_sentiment_analysis_valid_request(self):
        """Test the sentiment analysis endpoint with a valid request"""
        request_data = {"text": "I love sunny days!"}
        response = client.post("/sentiment_analysis", json=request_data)
        self.assertEqual(response.status_code, 200)
        self.assertIn("sentiment", response.json())
        self.assertIn(response.json()["sentiment"], ["positive", "neutral", "negative"])

    def test_perform_sentiment_analysis_empty_text(self):
        """Test the sentiment analysis endpoint with an empty text"""
        request_data = {"text": ""}
        response = client.post("/sentiment_analysis", json=request_data)
        self.assertEqual(response.status_code, 422)

    def test_perform_sentiment_analysis_missing_text_field(self):
        """Test the sentiment analysis endpoint with a missing text field"""
        request_data = {}
        response = client.post("/sentiment_analysis", json=request_data)
        self.assertEqual(response.status_code, 422)

    def test_perform_sentiment_analysis_with_long_text(self):
        """Test the sentiment analysis endpoint with a very long text"""
        request_data = {"text": "a" * 10001}  # Assuming there's a limit of 10000 characters
        response = client.post("/sentiment_analysis", json=request_data)
        self.assertEqual(response.status_code, 422)

if __name__ == "__main__":
    main()
