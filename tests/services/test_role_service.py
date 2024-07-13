## tests/services/test_role_service.py

import pytest
from sqlalchemy.orm import Session
from app.models.role import Role
from app.services.role_service import RoleService
from app.db.session import SessionLocal, Base, engine

# Create the database tables
Base.metadata.create_all(bind=engine)

@pytest.fixture(scope="module")
def db() -> Session:
    """
    Fixture to provide a database session for the tests.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def test_create_role(db: Session):
    """
    Test the creation of a role.
    """
    role_name = "test_role"
    role_description = "test_description"
    role = RoleService.create_role(db, role_name, role_description)
    assert role.name == role_name
    assert role.description == role_description

def test_get_role(db: Session):
    """
    Test retrieving a role by name.
    """
    role_name = "test_role"
    role_description = "test_description"
    RoleService.create_role(db, role_name, role_description)
    role = RoleService.get_role(db, role_name)
    assert role is not None
    assert role.name == role_name
    assert role.description == role_description

def test_delete_role(db: Session):
    """
    Test deleting a role by name.
    """
    role_name = "test_role"
    role_description = "test_description"
    RoleService.create_role(db, role_name, role_description)
    RoleService.delete_role(db, role_name)
    role = RoleService.get_role(db, role_name)
    assert role is None
