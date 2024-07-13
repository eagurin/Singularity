## tests/services/test_training_service.py

import pytest
from sqlalchemy.orm import Session
from app.models.training import Training
from app.services.training_service import TrainingService
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

def test_create_training(db: Session):
    """
    Test the creation of a training.
    """
    training_title = "test_training"
    training_content = "test_content"
    training = TrainingService.create_training(db, training_title, training_content)
    assert training.title == training_title
    assert training.content == training_content

def test_get_training(db: Session):
    """
    Test retrieving a training by title.
    """
    training_title = "test_training"
    training_content = "test_content"
    TrainingService.create_training(db, training_title, training_content)
    training = TrainingService.get_training(db, training_title)
    assert training is not None
    assert training.title == training_title
    assert training.content == training_content

def test_delete_training(db: Session):
    """
    Test deleting a training by title.
    """
    training_title = "test_training"
    training_content = "test_content"
    TrainingService.create_training(db, training_title, training_content)
    TrainingService.delete_training(db, training_title)
    training = TrainingService.get_training(db, training_title)
    assert training is None
