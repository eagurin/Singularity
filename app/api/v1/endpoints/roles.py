## app/api/v1/endpoints/roles.py

from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from sqlalchemy.exc import NoResultFound

from app.schemas.role import RoleCreate, Role
from app.services.role_service import RoleService
from app.db.session import get_db

router = APIRouter()

@router.post('/', response_model=Role, status_code=201)
async def create_role(role: RoleCreate, db: Session = Depends(get_db)):
    """
    Asynchronously create a new role.
    """
    try:
        role_created = await RoleService.create_role(db, role.name, role.description)
        return role_created
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Role could not be created. Error: {str(e)}")

@router.get('/{name}', response_model=Role)
async def get_role(name: str, db: Session = Depends(get_db)):
    """
    Asynchronously get a role by name.
    """
    try:
        role = await RoleService.get_role(db, name)
        return role
    except NoResultFound:
        raise HTTPException(status_code=404, detail='Role not found')

@router.delete('/{name}', status_code=204)
async def delete_role(name: str, db: Session = Depends(get_db)):
    """
    Asynchronously delete a role by name.
    """
    role_exists = await RoleService.get_role(db, name)
    if not role_exists:
        raise HTTPException(status_code=404, detail="Role not found")
    await RoleService.delete_role(db, name)
    return {"detail": "Role deleted successfully."}
