## tests/services/test_recommendation_service.py

import pytest
from sqlalchemy.orm import Session
from app.models.recommendation import Recommendation
from app.services.recommendation_service import RecommendationService
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

def test_create_recommendation(db: Session):
    """
    Test the creation of a recommendation.
    """
    recommendation_title = "test_recommendation"
    recommendation_content = "test_content"
    recommendation = RecommendationService.create_recommendation(db, recommendation_title, recommendation_content)
    assert recommendation.title == recommendation_title
    assert recommendation.content == recommendation_content

def test_get_recommendation(db: Session):
    """
    Test retrieving a recommendation by title.
    """
    recommendation_title = "test_recommendation"
    recommendation_content = "test_content"
    RecommendationService.create_recommendation(db, recommendation_title, recommendation_content)
    recommendation = RecommendationService.get_recommendation(db, recommendation_title)
    assert recommendation is not None
    assert recommendation.title == recommendation_title
    assert recommendation.content == recommendation_content

def test_delete_recommendation(db: Session):
    """
    Test deleting a recommendation by title.
    """
    recommendation_title = "test_recommendation"
    recommendation_content = "test_content"
    RecommendationService.create_recommendation(db, recommendation_title, recommendation_content)
    RecommendationService.delete_recommendation(db, recommendation_title)
    recommendation = RecommendationService.get_recommendation(db, recommendation_title)
    assert recommendation is None
