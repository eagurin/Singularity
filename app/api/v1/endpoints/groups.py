## app/api/v1/endpoints/groups.py

from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List

from app.schemas.group import GroupCreate, Group
from app.services.group_service import GroupService
from app.db.session import get_async_db

router = APIRouter()

@router.post('/', response_model=Group, status_code=201)
async def create_group(group: GroupCreate, db: AsyncSession = Depends(get_async_db)):
    """
    Asynchronously create a new group.
    """
    try:
        new_group = await GroupService.create_group(db=db, name=group.name, members=group.members)
        return new_group
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error creating group: {e}")

@router.get('/{name}', response_model=Group)
async def get_group(name: str, db: AsyncSession = Depends(get_async_db)):
    """
    Asynchronously get a group by name.
    """
    try:
        group = await GroupService.get_group(db=db, name=name)
        if not group:
            raise HTTPException(status_code=404, detail='Group not found')
        return group
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error retrieving group: {e}")

@router.delete('/{name}', status_code=204)
async def delete_group(name: str, db: AsyncSession = Depends(get_async_db)):
    """
    Asynchronously delete a group by name.
    """
    try:
        await GroupService.delete_group(db=db, name=name)
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error deleting group: {e}")
