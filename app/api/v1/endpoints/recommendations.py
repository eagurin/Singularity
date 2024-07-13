## app/api/v1/endpoints/recommendations.py

from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List

from app.schemas.recommendation import RecommendationCreate, Recommendation
from app.services.recommendation_service import RecommendationService
from app.db.session import get_async_db

router = APIRouter()

@router.post('/', response_model=Recommendation, status_code=201)
async def create_recommendation(recommendation: RecommendationCreate, db: AsyncSession = Depends(get_async_db)):
    """
    Asynchronously create a new recommendation.
    """
    try:
        new_recommendation = await RecommendationService.create_recommendation(db=db, title=recommendation.title, content=recommendation.content)
        return new_recommendation
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error creating recommendation: {e}")

@router.get('/{title}', response_model=Recommendation)
async def get_recommendation(title: str, db: AsyncSession = Depends(get_async_db)):
    """
    Asynchronously get a recommendation by title.
    """
    try:
        recommendation = await RecommendationService.get_recommendation(db=db, title=title)
        if not recommendation:
            raise HTTPException(status_code=404, detail='Recommendation not found')
        return recommendation
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error retrieving recommendation: {e}")

@router.delete('/{title}', status_code=204)
async def delete_recommendation(title: str, db: AsyncSession = Depends(get_async_db)):
    """
    Asynchronously delete a recommendation by title.
    """
    try:
        await RecommendationService.delete_recommendation(db=db, title=title)
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error deleting recommendation: {e}")
