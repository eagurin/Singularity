## tests/services/test_news_service.py

import pytest
from sqlalchemy.orm import Session
from app.models.news import News
from app.services.news_service import NewsService
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

def test_create_news(db: Session):
    """
    Test the creation of a news article.
    """
    news_title = "test_news"
    news_content = "test_content"
    news = NewsService.create_news(db, news_title, news_content)
    assert news.title == news_title
    assert news.content == news_content

def test_get_news(db: Session):
    """
    Test retrieving a news article by title.
    """
    news_title = "test_news"
    news_content = "test_content"
    NewsService.create_news(db, news_title, news_content)
    news = NewsService.get_news(db, news_title)
    assert news is not None
    assert news.title == news_title
    assert news.content == news_content

def test_delete_news(db: Session):
    """
    Test deleting a news article by title.
    """
    news_title = "test_news"
    news_content = "test_content"
    NewsService.create_news(db, news_title, news_content)
    NewsService.delete_news(db, news_title)
    news = NewsService.get_news(db, news_title)
    assert news is None
