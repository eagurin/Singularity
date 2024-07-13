## app/services/news_service.py

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from typing import List, Optional
from app.models.news import News

class NewsService:
    @staticmethod
    async def create_news(db: AsyncSession, title: str, content: str) -> News:
        """
        Asynchronously create a new news article and save it to the database.

        Args:
            db (AsyncSession): The database session.
            title (str): The title of the news article.
            content (str): The content of the news article.

        Returns:
            News: The created news article.
        """
        news = News(title=title, content=content)
        db.add(news)
        await db.commit()
        await db.refresh(news)
        return news

    @staticmethod
    async def get_news(db: AsyncSession, title: str) -> Optional[News]:
        """
        Asynchronously retrieve a news article by title from the database.

        Args:
            db (AsyncSession): The database session.
            title (str): The title of the news article.

        Returns:
            Optional[News]: The retrieved news article or None if not found.
        """
        result = await db.execute(select(News).filter(News.title == title))
        news = result.scalars().first()
        return news

    @staticmethod
    async def delete_news(db: AsyncSession, title: str) -> None:
        """
        Asynchronously delete a news article by title from the database.

        Args:
            db (AsyncSession): The database session.
            title (str): The title of the news article to be deleted.
        """
        result = await db.execute(select(News).filter(News.title == title))
        news = result.scalars().first()
        if news:
            await db.delete(news)
            await db.commit()

    @staticmethod
    async def list_news(db: AsyncSession) -> List[News]:
        """
        Asynchronously list all news articles from the database.

        Args:
            db (AsyncSession): The database session.

        Returns:
            List[News]: A list of all news articles.
        """
        result = await db.execute(select(News))
        news_list = result.scalars().all()
        return news_list
