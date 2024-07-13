## app/services/feedback_service.py

from app.models.feedback import Feedback
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from typing import Optional, List

class FeedbackService:
    @staticmethod
    async def create_feedback(db: AsyncSession, user: str, content: str) -> Feedback:
        """
        Asynchronously create a new feedback entry and save it to the database.

        Args:
            db (AsyncSession): The database session.
            user (str): The user who provided the feedback.
            content (str): The content of the feedback.

        Returns:
            Feedback: The created feedback entry.
        """
        feedback = Feedback(user=user, content=content)
        db.add(feedback)
        await db.commit()
        await db.refresh(feedback)
        return feedback

    @staticmethod
    async def get_feedback(db: AsyncSession, user: str) -> Optional[Feedback]:
        """
        Asynchronously retrieve feedback by user from the database.

        Args:
            db (AsyncSession): The database session.
            user (str): The user who provided the feedback.

        Returns:
            Optional[Feedback]: The retrieved feedback or None if not found.
        """
        result = await db.execute(select(Feedback).filter(Feedback.user == user))
        feedback = result.scalars().first()
        return feedback

    @staticmethod
    async def delete_feedback(db: AsyncSession, user: str) -> None:
        """
        Asynchronously delete feedback by user from the database.

        Args:
            db (AsyncSession): The database session.
            user (str): The user who provided the feedback.
        """
        result = await db.execute(select(Feedback).filter(Feedback.user == user))
        feedback = result.scalars().first()
        if feedback:
            await db.delete(feedback)
            await db.commit()

    @staticmethod
    async def list_feedbacks(db: AsyncSession) -> List[Feedback]:
        """
        Asynchronously list all feedback entries from the database.

        Args:
            db (AsyncSession): The database session.

        Returns:
            List[Feedback]: A list of all feedback entries.
        """
        result = await db.execute(select(Feedback))
        feedbacks = result.scalars().all()
        return feedbacks
