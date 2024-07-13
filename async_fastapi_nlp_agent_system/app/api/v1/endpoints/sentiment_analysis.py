from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.core.dependencies import get_db
from app.models.schemas.nlp import (SentimentAnalysisRequest,
                                    SentimentAnalysisResponse)
from app.services.nlp_service import NLPService

router = APIRouter()


@router.post("/sentiment_analysis", response_model=SentimentAnalysisResponse)
def perform_sentiment_analysis(
    request: SentimentAnalysisRequest, db: Session = Depends(get_db)
):
    """
    Endpoint to perform sentiment analysis on the provided text.
    Utilizes the NLPService to analyze the sentiment of the text and returns the analysis result.

    Parameters:
    - request: SentimentAnalysisRequest - A Pydantic model that contains the text to be analyzed.
    - db: Session - A SQLAlchemy database session dependency injected by FastAPI.

    Returns:
    - SentimentAnalysisResponse: A Pydantic model that contains the result of the sentiment analysis.
    """
    nlp_service = NLPService(db)
    return nlp_service.analyze_sentiment(request.text)
