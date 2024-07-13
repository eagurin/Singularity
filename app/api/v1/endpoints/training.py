## app/api/v1/endpoints/training.py

from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List

from app.schemas.training import TrainingCreate, Training
from app.services.training_service import TrainingService
from app.db.session import get_async_db

router = APIRouter()

@router.post('/', response_model=Training, status_code=201)
async def create_training(training: TrainingCreate, db: AsyncSession = Depends(get_async_db)):
    """
    Asynchronously create a new training.
    """
    try:
        new_training = await TrainingService.create_training(db=db, title=training.title, content=training.content)
        return new_training
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error creating training: {e}")

@router.get('/{title}', response_model=Training)
async def get_training(title: str, db: AsyncSession = Depends(get_async_db)):
    """
    Asynchronously get a training by title.
    """
    try:
        training = await TrainingService.get_training(db=db, title=title)
        if not training:
            raise HTTPException(status_code=404, detail='Training not found')
        return training
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error retrieving training: {e}")

@router.delete('/{title}', status_code=204)
async def delete_training(title: str, db: AsyncSession = Depends(get_async_db)):
    """
    Asynchronously delete a training by title.
    """
    try:
        await TrainingService.delete_training(db=db, title=title)
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error deleting training: {e}")
