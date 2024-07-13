## app/api/v1/endpoints/stages.py

from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List

from app.schemas.stage import StageCreate, Stage
from app.services.stage_service import StageService
from app.db.session import get_async_db

router = APIRouter()

@router.post('/', response_model=Stage, status_code=201)
async def create_stage(stage: StageCreate, db: AsyncSession = Depends(get_async_db)):
    """
    Asynchronously create a new stage.
    """
    try:
        new_stage = await StageService.create_stage(db=db, name=stage.name, description=stage.description)
        return new_stage
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error creating stage: {e}")

@router.get('/', response_model=List[Stage])
async def get_all_stages(db: AsyncSession = Depends(get_async_db)):
    """
    Asynchronously get all stages.
    """
    try:
        stages = await StageService.get_all_stages(db=db)
        return stages
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error retrieving stages: {e}")

@router.get('/{name}', response_model=Stage)
async def get_stage(name: str, db: AsyncSession = Depends(get_async_db)):
    """
    Asynchronously get a stage by name.
    """
    try:
        stage = await StageService.get_stage(db=db, name=name)
        if not stage:
            raise HTTPException(status_code=404, detail='Stage not found')
        return stage
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error retrieving stage: {e}")

@router.delete('/{name}', status_code=204)
async def delete_stage(name: str, db: AsyncSession = Depends(get_async_db)):
    """
    Asynchronously delete a stage by name.
    """
    try:
        await StageService.delete_stage(db=db, name=name)
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error deleting stage: {e}")
