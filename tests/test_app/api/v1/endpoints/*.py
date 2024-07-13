"""
## IMPORTS
"""
import pytest

# Attempt to import TestClient from fastapi.testclient, handling the potential ImportError
try:
    from fastapi.testclient import TestClient
except ImportError as e:
    raise ImportError("It seems like 'fastapi' is not installed. Please ensure to install 'fastapi' to run tests.") from e

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.main import app
from app.core.config import settings
from app.database.base import Base

"""
## SETUP
"""
@pytest.fixture(scope="module")
def test_client():
    """
    Setup of the test client.
    """
    # Setup of the test client with handling for potential configuration issues
    try:
        engine = create_engine(settings.SQLALCHEMY_DATABASE_URI)
    except AttributeError as e:
        raise AttributeError("Database URI is not configured properly in settings.") from e

    TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    Base.metadata.create_all(bind=engine)
    _db = TestingSessionLocal()
    try:
        client = TestClient(app)
        yield client
    finally:
        _db.close()
        Base.metadata.drop_all(bind=engine)

"""
## CREATE_AGENT
"""
def test_create_agent(test_client):
    """
    Test creating a new agent.
    """
    response = test_client.post(
        "/",
        json={"name": "Test Agent", "status": "active"}
    )
    assert response.status_code == 201
    assert response.json()["name"] == "Test Agent"
    assert response.json()["status"] == "active"

"""
## READ_AGENTS
"""
def test_read_agents(test_client):
    """
    Test reading list of agents.
    """
    response = test_client.get("/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

"""
## READ_AGENT
"""
def test_read_agent_not_found(test_client):
    """
    Test reading a non-existing agent.
    """
    response = test_client.get("/999")
    assert response.status_code == 404

def test_read_agent(test_client):
    """
    Test reading an existing agent.
    """
    # First, create an agent to read
    create_response = test_client.post(
        "/",
        json={"name": "Existing Agent", "status": "active"}
    )
    agent_id = create_response.json()["id"]
    read_response = test_client.get(f"/{agent_id}")
    assert read_response.status_code == 200
    assert read_response.json()["name"] == "Existing Agent"

"""
## UPDATE_AGENT
"""
def test_update_agent_not_found(test_client):
    """
    Test updating a non-existing agent.
    """
    response = test_client.put(
        "/999",
        json={"name": "Non-existing Agent", "status": "inactive"}
    )
    assert response.status_code == 404

def test_update_agent(test_client):
    """
    Test updating an existing agent.
    """
    # First, create an agent to update
    create_response = test_client.post(
        "/",
        json={"name": "Agent to Update", "status": "active"}
    )
    agent_id = create_response.json()["id"]
    update_response = test_client.put(
        f"/{agent_id}",
        json={"name": "Updated Agent", "status": "inactive"}
    )
    assert update_response.status_code == 200
    assert update_response.json()["name"] == "Updated Agent"
    assert update_response.json()["status"] == "inactive"

"""
## DELETE_AGENT
"""
def test_delete_agent_not_found(test_client):
    """
    Test deleting a non-existing agent.
    """
    response = test_client.delete("/999")
    assert response.status_code == 404

def test_delete_agent(test_client):
    """
    Test deleting an existing agent.
    """
    # First, create an agent to delete
    create_response = test_client.post(
        "/",
        json={"name": "Agent to Delete", "status": "active"}
    )
    agent_id = create_response.json()["id"]
    delete_response = test_client.delete(f"/{agent_id}")
    assert delete_response.status_code == 200
    assert delete_response.json()["name"] == "Agent to Delete"
