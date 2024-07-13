## tests/api/test_agents.py
import pytest
from httpx import AsyncClient
from fastapi import FastAPI
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker
from app.models.database.agent import Agent as DBAgent
from app.core.config import settings

DATABASE_URL = settings.TEST_DATABASE_URL

# Setup test database and overrides
engine = create_async_engine(DATABASE_URL, echo=True)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine, class_=AsyncSession)

@pytest.fixture
async def async_app() -> FastAPI:
    from app.main import app  # Import the FastAPI app
    async with engine.begin() as conn:
        # Create test tables
        await conn.run_sync(DBAgent.metadata.create_all)
    try:
        yield app
    finally:
        async with engine.begin() as conn:
            # Drop test tables
            await conn.run_sync(DBAgent.metadata.drop_all)

@pytest.fixture
async def session() -> AsyncSession:
    async with TestingSessionLocal() as session:
        yield session

@pytest.fixture
async def client(async_app: FastAPI, session: AsyncSession) -> AsyncClient:
    async with AsyncClient(app=async_app, base_url="http://test") as client:
        yield client

@pytest.fixture(autouse=True)
async def transactional_db(session: AsyncSession):
    async with session.begin():
        yield session
        await session.rollback()

@pytest.mark.asyncio
async def test_create_agent(client: AsyncClient):
    response = await client.post("/api/v1/agents/", json={"name": "Test Agent", "role_id": 1})
    assert response.status_code == 201
    data = response.json()
    assert data["name"] == "Test Agent"
    assert "id" in data

@pytest.mark.asyncio
async def test_read_agent(client: AsyncClient, session: AsyncSession):
    # Pre-insert an agent into the test database
    test_agent = DBAgent(name="Read Agent", role_id=2)
    session.add(test_agent)
    await session.commit()

    response = await client.get(f"/api/v1/agents/{test_agent.id}")
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "Read Agent"
    assert data["id"] == test_agent.id

@pytest.mark.asyncio
async def test_update_agent(client: AsyncClient, session: AsyncSession):
    # Pre-insert an agent to update
    test_agent = DBAgent(name="Update Agent", role_id=3)
    session.add(test_agent)
    await session.commit()

    response = await client.put(f"/api/v1/agents/{test_agent.id}", json={"name": "Updated Agent", "role_id": 3})
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "Updated Agent"
    assert data["id"] == test_agent.id

@pytest.mark.asyncio
async def test_delete_agent(client: AsyncClient, session: AsyncSession):
    # Pre-insert an agent to delete
    test_agent = DBAgent(name="Delete Agent", role_id=4)
    session.add(test_agent)
    await session.commit()

    response = await client.delete(f"/api/v1/agents/{test_agent.id}")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == test_agent.id

    # Verify the agent is deleted
    db_agent = await session.get(DBAgent, test_agent.id)
    assert db_agent is None
