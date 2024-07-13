## app/api/v1/endpoints/entity_recognition.py
from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.core.dependencies import get_db
from app.models.schemas.nlp import (EntityRecognitionRequest,
                                    EntityRecognitionResponse)
from app.services.nlp_service import NLPService

router = APIRouter()


@router.post("/entity_recognition", response_model=EntityRecognitionResponse)
def perform_entity_recognition(
    request: EntityRecognitionRequest, db: Session = Depends(get_db)
):
    """
    Endpoint to perform entity recognition on the provided text.
    Utilizes the NLPService to recognize entities in the text and returns the recognized entities.

    Parameters:
    - request: EntityRecognitionRequest - A Pydantic model that contains the text for entity recognition.
    - db: Session - A SQLAlchemy database session dependency injected by FastAPI.

    Returns:
    - EntityRecognitionResponse: A Pydantic model that contains the recognized entities.
    """
    nlp_service = NLPService(db)
    return nlp_service.recognize_entities(request.text)
