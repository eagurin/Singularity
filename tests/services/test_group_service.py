## tests/services/test_group_service.py

import pytest
from sqlalchemy.orm import Session
from app.models.group import Group
from app.services.group_service import GroupService
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

def test_create_group(db: Session):
    """
    Test the creation of a group.
    """
    group_name = "test_group"
    group_members = ["member1", "member2"]
    group = GroupService.create_group(db, group_name, group_members)
    assert group.name == group_name
    assert group.members == group_members

def test_get_group(db: Session):
    """
    Test retrieving a group by name.
    """
    group_name = "test_group"
    group_members = ["member1", "member2"]
    GroupService.create_group(db, group_name, group_members)
    group = GroupService.get_group(db, group_name)
    assert group is not None
    assert group.name == group_name
    assert group.members == group_members

def test_delete_group(db: Session):
    """
    Test deleting a group by name.
    """
    group_name = "test_group"
    group_members = ["member1", "member2"]
    GroupService.create_group(db, group_name, group_members)
    GroupService.delete_group(db, group_name)
    group = GroupService.get_group(db, group_name)
    assert group is None
