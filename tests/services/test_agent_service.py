## tests/services/test_agent_service.py

import pytest
from sqlalchemy.orm import Session
from app.models.agent import Agent
from app.services.agent_service import AgentService
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

def test_create_agent(db: Session):
    """
    Test the creation of an agent.
    """
    agent_name = "test_agent"
    agent_model = "test_model"
    agent = AgentService.create_agent(db, agent_name, agent_model)
    assert agent.name == agent_name
    assert agent.model == agent_model

def test_get_agent(db: Session):
    """
    Test retrieving an agent by name.
    """
    agent_name = "test_agent"
    agent_model = "test_model"
    AgentService.create_agent(db, agent_name, agent_model)
    agent = AgentService.get_agent(db, agent_name)
    assert agent is not None
    assert agent.name == agent_name
    assert agent.model == agent_model

def test_delete_agent(db: Session):
    """
    Test deleting an agent by name.
    """
    agent_name = "test_agent"
    agent_model = "test_model"
    AgentService.create_agent(db, agent_name, agent_model)
    AgentService.delete_agent(db, agent_name)
    agent = AgentService.get_agent(db, agent_name)
    assert agent is None
