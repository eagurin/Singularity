## app/api/v1/endpoints/feedback.py

from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List

from app.schemas.feedback import FeedbackCreate, Feedback
from app.services.feedback_service import FeedbackService
from app.db.session import get_async_db

router = APIRouter()

@router.post('/', response_model=Feedback, status_code=201)
async def create_feedback(feedback: FeedbackCreate, db: AsyncSession = Depends(get_async_db)):
    """
    Asynchronously create a new feedback entry.
    """
    try:
        new_feedback = await FeedbackService.create_feedback(db=db, user=feedback.user, content=feedback.content)
        return new_feedback
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error creating feedback: {e}")

@router.get('/{user}', response_model=List[Feedback])
async def get_feedback(user: str, db: AsyncSession = Depends(get_async_db)):
    """
    Asynchronously get feedback by user.
    """
    try:
        feedback = await FeedbackService.get_feedback(db=db, user=user)
        if not feedback:
            raise HTTPException(status_code=404, detail='Feedback not found')
        return feedback
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error retrieving feedback: {e}")

@router.delete('/{user}', status_code=204)
async def delete_feedback(user: str, db: AsyncSession = Depends(get_async_db)):
    """
    Asynchronously delete feedback by user.
    """
    try:
        await FeedbackService.delete_feedback(db=db, user=user)
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error deleting feedback: {e}")
