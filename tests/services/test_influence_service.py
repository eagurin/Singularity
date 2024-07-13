## tests/services/test_influence_service.py

import pytest
from sqlalchemy.orm import Session
from app.models.influence import Influence
from app.services.influence_service import InfluenceService
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

def test_create_influence(db: Session):
    """
    Test the creation of an influence.
    """
    influence_name = "test_influence"
    influence_effect = "test_effect"
    influence = InfluenceService.create_influence(db, influence_name, influence_effect)
    assert influence.name == influence_name
    assert influence.effect == influence_effect

def test_get_influence(db: Session):
    """
    Test retrieving an influence by name.
    """
    influence_name = "test_influence"
    influence_effect = "test_effect"
    InfluenceService.create_influence(db, influence_name, influence_effect)
    influence = InfluenceService.get_influence(db, influence_name)
    assert influence is not None
    assert influence.name == influence_name
    assert influence.effect == influence_effect

def test_delete_influence(db: Session):
    """
    Test deleting an influence by name.
    """
    influence_name = "test_influence"
    influence_effect = "test_effect"
    InfluenceService.create_influence(db, influence_name, influence_effect)
    InfluenceService.delete_influence(db, influence_name)
    influence = InfluenceService.get_influence(db, influence_name)
    assert influence is None
