## app/services/recommendation_service.py

from app.models.recommendation import Recommendation
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from typing import Optional, List

class RecommendationService:
    @staticmethod
    async def create_recommendation(db: AsyncSession, title: str, content: str) -> Recommendation:
        """
        Asynchronously create a new recommendation and save it to the database.

        Args:
            db (AsyncSession): The database session.
            title (str): The title of the recommendation.
            content (str): The content of the recommendation.

        Returns:
            Recommendation: The created recommendation.
        """
        recommendation = Recommendation(title=title, content=content)
        db.add(recommendation)
        await db.commit()
        await db.refresh(recommendation)
        return recommendation

    @staticmethod
    async def get_recommendation(db: AsyncSession, title: str) -> Optional[Recommendation]:
        """
        Asynchronously retrieve a recommendation by title from the database.

        Args:
            db (AsyncSession): The database session.
            title (str): The title of the recommendation.

        Returns:
            Optional[Recommendation]: The retrieved recommendation or None if not found.
        """
        result = await db.execute(select(Recommendation).filter(Recommendation.title == title))
        recommendation = result.scalars().first()
        return recommendation

    @staticmethod
    async def delete_recommendation(db: AsyncSession, title: str) -> None:
        """
        Asynchronously delete a recommendation by title from the database.

        Args:
            db (AsyncSession): The database session.
            title (str): The title of the recommendation to be deleted.
        """
        result = await db.execute(select(Recommendation).filter(Recommendation.title == title))
        recommendation = result.scalars().first()
        if recommendation:
            await db.delete(recommendation)
            await db.commit()

    @staticmethod
    async def list_recommendations(db: AsyncSession) -> List[Recommendation]:
        """
        Asynchronously list all recommendations from the database.

        Args:
            db (AsyncSession): The database session.

        Returns:
            List[Recommendation]: A list of all recommendations.
        """
        result = await db.execute(select(Recommendation))
        recommendations = result.scalars().all()
        return recommendations
