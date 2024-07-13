## app/api/v1/endpoints/scaling.py

from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List

from app.schemas.scaling import ScalingCreate, Scaling
from app.services.scaling_service import ScalingService
from app.db.session import get_async_db

router = APIRouter()

@router.post('/', response_model=Scaling, status_code=201)
async def apply_scaling(scaling: ScalingCreate, db: AsyncSession = Depends(get_async_db)):
    """
    Asynchronously apply a scaling strategy.
    
    Args:
        scaling (ScalingCreate): The scaling strategy to be applied.
        db (AsyncSession): Dependency injection of the database session.

    Returns:
        Scaling: The applied scaling strategy.
    """
    try:
        new_scaling = await ScalingService.apply_scaling(db=db, strategy=scaling.strategy)
        return new_scaling
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error applying scaling strategy: {e}")
