## app/api/v1/endpoints/advanced_nlp_features.py
from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.core.dependencies import get_db
from app.models.schemas.nlp import (AdvancedNLPFeaturesRequest,
                                    AdvancedNLPFeaturesResponse,
                                    EntityRecognitionRequest,
                                    EntityRecognitionResponse,
                                    LanguageTranslationRequest,
                                    LanguageTranslationResponse,
                                    SentimentAnalysisRequest,
                                    SentimentAnalysisResponse)
from app.services.nlp_service import NLPService

router = APIRouter()


@router.post(
    "/advanced_nlp_features", response_model=AdvancedNLPFeaturesResponse
)
def perform_advanced_nlp_features(
    request: AdvancedNLPFeaturesRequest, db: Session = Depends(get_db)
):
    """
    Endpoint to perform advanced NLP features on the provided text.
    This includes sentiment analysis, entity recognition, and language translation as a combined service.

    Parameters:
    - request: AdvancedNLPFeaturesRequest - A Pydantic model that contains the text to be analyzed, and the target language for translation.
    - db: Session - A SQLAlchemy database session dependency injected by FastAPI.

    Returns:
    - AdvancedNLPFeaturesResponse: A Pydantic model that contains the results of the sentiment analysis, entity recognition, and language translation.
    """
    nlp_service = NLPService(db)

    # Perform sentiment analysis
    sentiment_result = nlp_service.analyze_sentiment(request.text)

    # Perform entity recognition
    entity_result = nlp_service.recognize_entities(request.text)

    # Perform language translation if a target language is specified and not empty
    translation_result = None
    if request.target_language and request.target_language.strip():
        translation_result = nlp_service.translate_text(
            request.text, request.target_language
        )

    return AdvancedNLPFeaturesResponse(
        sentiment_analysis=sentiment_result.result,
        entity_recognition=entity_result.entities,
        language_translation=(
            translation_result.translated_text if translation_result else None
        ),
    )
