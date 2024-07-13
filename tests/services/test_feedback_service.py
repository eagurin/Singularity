## tests/services/test_feedback_service.py

import pytest
from sqlalchemy.orm import Session
from app.models.feedback import Feedback
from app.services.feedback_service import FeedbackService
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

def test_create_feedback(db: Session):
    """
    Test the creation of a feedback entry.
    """
    feedback_user = "test_user"
    feedback_content = "test_content"
    feedback = FeedbackService.create_feedback(db, feedback_user, feedback_content)
    assert feedback.user == feedback_user
    assert feedback.content == feedback_content

def test_get_feedback(db: Session):
    """
    Test retrieving a feedback entry by user.
    """
    feedback_user = "test_user"
    feedback_content = "test_content"
    FeedbackService.create_feedback(db, feedback_user, feedback_content)
    feedback = FeedbackService.get_feedback(db, feedback_user)
    assert feedback is not None
    assert feedback.user == feedback_user
    assert feedback.content == feedback_content

def test_delete_feedback(db: Session):
    """
    Test deleting a feedback entry by user.
    """
    feedback_user = "test_user"
    feedback_content = "test_content"
    FeedbackService.create_feedback(db, feedback_user, feedback_content)
    FeedbackService.delete_feedback(db, feedback_user)
    feedback = FeedbackService.get_feedback(db, feedback_user)
    assert feedback is None
