## tests/api/test_nlp_features.py
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
    from app.main import create_app  # Import the FastAPI app creation function
    app = create_app()
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
async def test_perform_sentiment_analysis(client: AsyncClient):
    response = await client.post("/api/v1/nlp/sentiment_analysis", json={"text": "I love sunny days but hate the rain."})
    assert response.status_code == 200
    data = response.json()
    assert "result" in data
    assert isinstance(data["result"], (list, dict))

@pytest.mark.asyncio
async def test_perform_entity_recognition(client: AsyncClient):
    response = await client.post("/api/v1/nlp/entity_recognition", json={"text": "London is a big city in the United Kingdom."})
    assert response.status_code == 200
    data = response.json()
    assert "entities" in data
    assert isinstance(data["entities"], list)

@pytest.mark.asyncio
async def test_perform_language_translation(client: AsyncClient):
    response = await client.post("/api/v1/nlp/language_translation", json={"text": "Hello, how are you?", "target_language": "es"})
    assert response.status_code == 200
    data = response.json()
    assert "translated_text" in data
    assert isinstance(data["translated_text"], str)
