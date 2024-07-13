## app/api/v1/endpoints/news.py

from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List

from app.schemas.news import NewsCreate, News
from app.services.news_service import NewsService
from app.db.session import get_async_db

router = APIRouter()

@router.post('/', response_model=News, status_code=201)
async def create_news(news: NewsCreate, db: AsyncSession = Depends(get_async_db)):
    """
    Asynchronously create a new news article.
    """
    try:
        new_news = await NewsService.create_news(db=db, title=news.title, content=news.content)
        return new_news
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error creating news: {e}")

@router.get('/{title}', response_model=News)
async def get_news(title: str, db: AsyncSession = Depends(get_async_db)):
    """
    Asynchronously get a news article by title.
    """
    try:
        news = await NewsService.get_news(db=db, title=title)
        if not news:
            raise HTTPException(status_code=404, detail='News not found')
        return news
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error retrieving news: {e}")

@router.delete('/{title}', status_code=204)
async def delete_news(title: str, db: AsyncSession = Depends(get_async_db)):
    """
    Asynchronously delete a news article by title.
    """
    try:
        await NewsService.delete_news(db=db, title=title)
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error deleting news: {e}")
