## tests/services/test_task_service.py

import pytest
from sqlalchemy.orm import Session
from app.models.task import Task
from app.services.task_service import TaskService
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

def test_create_task(db: Session):
    """
    Test the creation of a task.
    """
    task_name = "test_task"
    task_action = "test_action"
    task = TaskService.create_task(db, task_name, task_action)
    assert task.name == task_name
    assert task.action == task_action

def test_get_task(db: Session):
    """
    Test retrieving a task by name.
    """
    task_name = "test_task"
    task_action = "test_action"
    TaskService.create_task(db, task_name, task_action)
    task = TaskService.get_task(db, task_name)
    assert task is not None
    assert task.name == task_name
    assert task.action == task_action

def test_delete_task(db: Session):
    """
    Test deleting a task by name.
    """
    task_name = "test_task"
    task_action = "test_action"
    TaskService.create_task(db, task_name, task_action)
    TaskService.delete_task(db, task_name)
    task = TaskService.get_task(db, task_name)
    assert task is None
