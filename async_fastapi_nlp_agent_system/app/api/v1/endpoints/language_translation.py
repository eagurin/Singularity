## app/api/v1/endpoints/language_translation.py
from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.core.dependencies import get_db
from app.models.schemas.nlp import (LanguageTranslationRequest,
                                    LanguageTranslationResponse)
from app.services.nlp_service import NLPService

router = APIRouter()


@router.post(
    "/language_translation", response_model=LanguageTranslationResponse
)
def perform_language_translation(
    request: LanguageTranslationRequest, db: Session = Depends(get_db)
):
    """
    Endpoint to translate the provided text to the target language.
    Utilizes the NLPService to translate the text and returns the translated text.

    Parameters:
    - request: LanguageTranslationRequest - A Pydantic model that contains the text to be translated and the target language.
    - db: Session - A SQLAlchemy database session dependency injected by FastAPI.

    Returns:
    - LanguageTranslationResponse: A Pydantic model that contains the translated text.
    """
    nlp_service = NLPService(db)
    return nlp_service.translate_text(request.text, request.target_language)
