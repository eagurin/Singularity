## test_app/services/test_nlp_service.py
"""
This module contains tests for the NLPService class in the app/services/nlp_service.py file.
"""

import unittest
from unittest.mock import patch, MagicMock
from sqlalchemy.orm import Session
from app.services.nlp_service import NLPService
from app.models.schemas.nlp import SentimentAnalysisResponse, EntityRecognitionResponse, LanguageTranslationResponse

class TestNLPService(unittest.TestCase):
    ## SETUP
    def setUp(self) -> None:
        self.db: Session = MagicMock()  # Mocking the Session object
        self.nlp_service = NLPService(db=self.db)

    ## SENTIMENT ANALYSIS TESTS
    @patch("app.services.nlp_service.pipeline")
    def test_analyze_sentiment_success(self, mock_pipeline):
        mock_pipeline.return_value = MagicMock(return_value=[{"label": "POSITIVE", "score": 0.9997}])
        response = self.nlp_service.analyze_sentiment("This is a great day")
        self.assertIsInstance(response, SentimentAnalysisResponse)
        self.assertEqual(response.result[0]["label"], "POSITIVE")

    @patch("app.services.nlp_service.pipeline")
    def test_analyze_sentiment_pipeline_exception(self, mock_pipeline):
        mock_pipeline.side_effect = Exception("Pipeline error")
        with self.assertRaises(ValueError):
            self.nlp_service.analyze_sentiment("This will fail")

    ## ENTITY RECOGNITION TESTS
    @patch("app.services.nlp_service.pipeline")
    def test_recognize_entities_success(self, mock_pipeline):
        mock_pipeline.return_value = MagicMock(return_value=[{"entity_group": "PER", "score": 0.998, "word": "John Doe"}])
        response = self.nlp_service.recognize_entities("John Doe is a software engineer")
        self.assertIsInstance(response, EntityRecognitionResponse)
        self.assertEqual(response.entities[0]["word"], "John Doe")

    @patch("app.services.nlp_service.pipeline")
    def test_recognize_entities_pipeline_exception(self, mock_pipeline):
        mock_pipeline.side_effect = Exception("Pipeline error")
        with self.assertRaises(ValueError):
            self.nlp_service.recognize_entities("This will fail")

    ## LANGUAGE TRANSLATION TESTS
    @patch("app.services.nlp_service.pipeline")
    def test_translate_text_success(self, mock_pipeline):
        mock_pipeline.return_value = MagicMock(return_value=[{"translation_text": "Ceci est un test"}])
        response = self.nlp_service.translate_text("This is a test", "fr")
        self.assertIsInstance(response, LanguageTranslationResponse)
        self.assertEqual(response.translated_text, "Ceci est un test")

    @patch("app.services.nlp_service.pipeline")
    def test_translate_text_pipeline_exception(self, mock_pipeline):
        mock_pipeline.side_effect = Exception("Pipeline error")
        with self.assertRaises(ValueError):
            self.nlp_service.translate_text("This will fail", "fr")

    ## EDGE CASES AND FAILURE MODES
    @patch("app.services.nlp_service.pipeline")
    def test_translate_text_with_unsupported_language(self, mock_pipeline):
        mock_pipeline.side_effect = Exception("Unsupported language")
        with self.assertRaises(ValueError):
            self.nlp_service.translate_text("This will fail", "xx")

    @patch("app.services.nlp_service.pipeline")
    def test_analyze_sentiment_empty_text(self, mock_pipeline):
        with self.assertRaises(ValueError):
            self.nlp_service.analyze_sentiment("")

    @patch("app.services.nlp_service.pipeline")
    def test_recognize_entities_empty_text(self, mock_pipeline):
        with self.assertRaises(ValueError):
            self.nlp_service.recognize_entities("")

    @patch("app.services.nlp_service.pipeline")
    def test_translate_text_empty_text(self, mock_pipeline):
        with self.assertRaises(ValueError):
            self.nlp_service.translate_text("", "fr")

if __name__ == "__main__":
    unittest.main()
