from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

# Importing NLP related schemas and services
from app.models.schemas.nlp import SentimentAnalysisRequest, SentimentAnalysisResponse, EntityRecognitionRequest, EntityRecognitionResponse, LanguageTranslationRequest, LanguageTranslationResponse
from app.services.nlp_service import NLPService

from app.core.dependencies import get_db

router = APIRouter()

@router.post("/sentiment_analysis", response_model=SentimentAnalysisResponse)
def perform_sentiment_analysis(request: SentimentAnalysisRequest, db: Session = Depends(get_db)):
    """
    Perform sentiment analysis on the provided text.
    """
    nlp_service = NLPService(db)
    return nlp_service.analyze_sentiment(request.text)

@router.post("/entity_recognition", response_model=EntityRecognitionResponse)
def perform_entity_recognition(request: EntityRecognitionRequest, db: Session = Depends(get_db)):
    """
    Perform entity recognition on the provided text.
    """
    nlp_service = NLPService(db)
    return nlp_service.recognize_entities(request.text)

@router.post("/language_translation", response_model=LanguageTranslationResponse)
def perform_language_translation(request: LanguageTranslationRequest, db: Session = Depends(get_db)):
    """
    Translate the provided text to the target language.
    """
    nlp_service = NLPService(db)
    return nlp_service.translate_text(request.text, request.target_language)
