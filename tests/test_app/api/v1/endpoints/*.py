## IMPORTS
import sys
sys.path.append('/data')
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from unittest import TestCase, main
from app.main import app
from app.core.config import settings
from app.database.base_class import Base

## SETUP
# Configure the test database and session
TEST_DATABASE_URL = "sqlite:///./test_db.db"
engine = create_engine(TEST_DATABASE_URL, connect_args={"check_same_thread": False})
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create a TestClient using the FastAPI app
client = TestClient(app)

def override_get_db():
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()

app.dependency_overrides[get_db] = override_get_db

## PREPARE DATABASE
Base.metadata.create_all(bind=engine)

## TEST CASES
class TestNLPAPI(TestCase):
    ## SENTIMENT_ANALYSIS
    def test_perform_sentiment_analysis(self):
        request_data = {"text": "I love sunny days!"}
        response = client.post("/sentiment_analysis", json=request_data)
        self.assertEqual(response.status_code, 200)
        self.assertIn("sentiment", response.json())
        self.assertIn(response.json()["sentiment"], ["positive", "neutral", "negative"])

    ## ENTITY_RECOGNITION
    def test_perform_entity_recognition(self):
        request_data = {"text": "Google was founded in September 1998 by Larry Page and Sergey Brin."}
        response = client.post("/entity_recognition", json=request_data)
        self.assertEqual(response.status_code, 200)
        self.assertIn("entities", response.json())
        self.assertIsInstance(response.json()["entities"], list)
        self.assertGreater(len(response.json()["entities"]), 0)  # Expecting at least one entity

    ## LANGUAGE_TRANSLATION
    def test_perform_language_translation(self):
        request_data = {"text": "Hello, world!", "target_language": "es"}
        response = client.post("/language_translation", json=request_data)
        self.assertEqual(response.status_code, 200)
        self.assertIn("translated_text", response.json())
        self.assertNotEqual(response.json()["translated_text"], "")

    ## EDGE_CASES
    def test_sentiment_analysis_empty_text(self):
        request_data = {"text": ""}
        response = client.post("/sentiment_analysis", json=request_data)
        self.assertNotEqual(response.status_code, 200)

    def test_entity_recognition_empty_text(self):
        request_data = {"text": ""}
        response = client.post("/entity_recognition", json=request_data)
        self.assertNotEqual(response.status_code, 200)

    def test_language_translation_empty_text(self):
        request_data = {"text": "", "target_language": "es"}
        response = client.post("/language_translation", json=request_data)
        self.assertNotEqual(response.status_code, 200)

    def test_language_translation_unsupported_language(self):
        request_data = {"text": "Hello, world!", "target_language": "xx"}
        response = client.post("/language_translation", json=request_data)
        self.assertNotEqual(response.status_code, 200)

## CLEANUP
def tearDownModule():
    Base.metadata.drop_all(bind=engine)

if __name__ == "__main__":
    main()
