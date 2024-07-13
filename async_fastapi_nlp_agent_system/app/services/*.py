## app/services/nlp_service.py
import logging
from typing import List, Optional
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from app.models.schemas.nlp import SentimentAnalysisRequest, SentimentAnalysisResponse, EntityRecognitionRequest, EntityRecognitionResponse, LanguageTranslationRequest, LanguageTranslationResponse
from transformers import pipeline, PipelineException

class NLPService:
    def __init__(self, db: Session):
        self.db = db  # Placeholder for future database interactions

    def analyze_sentiment(self, text: str) -> SentimentAnalysisResponse:
        """
        Analyze the sentiment of the provided text.
        """
        try:
            sentiment_pipeline = pipeline("sentiment-analysis")
            result = sentiment_pipeline(text)
            return SentimentAnalysisResponse(result=result)
        except PipelineException as e:
            logging.error(f"Sentiment analysis pipeline error: {e}")
            raise ValueError("Failed to analyze sentiment due to a pipeline error.")
        except Exception as e:
            logging.error(f"Unexpected error during sentiment analysis: {e}")
            raise ValueError("Failed to analyze sentiment due to an unexpected error.")

    def recognize_entities(self, text: str) -> EntityRecognitionResponse:
        """
        Recognize entities in the provided text.
        """
        try:
            ner_pipeline = pipeline("ner", grouped_entities=True)
            entities = ner_pipeline(text)
            return EntityRecognitionResponse(entities=entities)
        except PipelineException as e:
            logging.error(f"Entity recognition pipeline error: {e}")
            raise ValueError("Failed to recognize entities due to a pipeline error.")
        except Exception as e:
            logging.error(f"Unexpected error during entity recognition: {e}")
            raise ValueError("Failed to recognize entities due to an unexpected error.")

    def translate_text(self, text: str, target_language: str, source_language: str = "en") -> LanguageTranslationResponse:
        """
        Translate the provided text from the source language to the target language.
        Assumes the source language is English ('en') if not specified.
        """
        try:
            translation_pipeline = pipeline("translation", model=f"Helsinki-NLP/opus-mt-{source_language}-{target_language}")
            translated_text = translation_pipeline(text, max_length=40)[0]['translation_text']
            return LanguageTranslationResponse(translated_text=translated_text)
        except PipelineException as e:
            logging.error(f"Translation pipeline error: {e}")
            raise ValueError("Failed to translate text due to a pipeline error.")
        except Exception as e:
            logging.error(f"Unexpected error during text translation: {e}")
            raise ValueError("Failed to translate text due to an unexpected error.")
