## app/api/v1/endpoints/influences.py

from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List

from app.schemas.influence import InfluenceCreate, Influence
from app.services.influence_service import InfluenceService
from app.db.session import get_async_db

router = APIRouter()

@router.post('/', response_model=Influence, status_code=201)
async def create_influence(influence: InfluenceCreate, db: AsyncSession = Depends(get_async_db)):
    """
    Asynchronously create a new influence.
    """
    try:
        new_influence = await InfluenceService.create_influence(db=db, name=influence.name, effect=influence.effect)
        return new_influence
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error creating influence: {e}")

@router.get('/', response_model=List[Influence])
async def get_all_influences(db: AsyncSession = Depends(get_async_db)):
    """
    Asynchronously get all influences.
    """
    try:
        influences = await InfluenceService.get_all_influences(db=db)
        return influences
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error retrieving influences: {e}")

@router.get('/{name}', response_model=Influence)
async def get_influence(name: str, db: AsyncSession = Depends(get_async_db)):
    """
    Asynchronously get an influence by name.
    """
    try:
        influence = await InfluenceService.get_influence(db=db, name=name)
        if not influence:
            raise HTTPException(status_code=404, detail='Influence not found')
        return influence
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error retrieving influence: {e}")

@router.delete('/{name}', status_code=204)
async def delete_influence(name: str, db: AsyncSession = Depends(get_async_db)):
    """
    Asynchronously delete an influence by name.
    """
    try:
        await InfluenceService.delete_influence(db=db, name=name)
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error deleting influence: {e}")
