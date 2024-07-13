## app/api/v1/endpoints/ethics.py

from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List

from app.schemas.ethics import EthicsCreate, Ethics
from app.services.ethics_service import EthicsService
from app.db.session import get_async_db

router = APIRouter()

@router.post('/', response_model=Ethics, status_code=201)
async def apply_ethics(ethics: EthicsCreate, db: AsyncSession = Depends(get_async_db)):
    """
    Asynchronously apply ethics principles.
    
    Args:
        ethics (EthicsCreate): The ethics principles to be applied.
        db (AsyncSession): Dependency injection of the database session.

    Returns:
        Ethics: The applied ethics principles.
    """
    try:
        new_ethics = await EthicsService.apply_ethics(db=db, principles=ethics.principles)
        return new_ethics
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error applying ethics principles: {e}")

@router.get('/', response_model=List[Ethics])
async def get_all_ethics(db: AsyncSession = Depends(get_async_db)):
    """
    Asynchronously get all applied ethics principles.
    
    Args:
        db (AsyncSession): Dependency injection of the database session.

    Returns:
        List[Ethics]: A list of all applied ethics principles.
    """
    try:
        ethics_list = await EthicsService.get_all_ethics(db=db)
        return ethics_list
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error retrieving ethics principles: {e}")

@router.delete('/{id}', status_code=204)
async def delete_ethics(id: int, db: AsyncSession = Depends(get_async_db)):
    """
    Asynchronously delete applied ethics principles by id.
    
    Args:
        id (int): The id of the ethics principles to be deleted.
        db (AsyncSession): Dependency injection of the database session.
    """
    try:
        await EthicsService.delete_ethics(db=db, id=id)
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error deleting ethics principles: {e}")
