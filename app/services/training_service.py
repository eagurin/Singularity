## app/services/training_service.py

from app.models.training import Training
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from typing import Optional, List

class TrainingService:
    @staticmethod
    async def create_training(db: AsyncSession, title: str, content: str) -> Training:
        """
        Asynchronously create a new training and save it to the database.

        Args:
            db (AsyncSession): The database session.
            title (str): The title of the training.
            content (str): The content of the training.

        Returns:
            Training: The created training.
        """
        training = Training(title=title, content=content)
        db.add(training)
        await db.commit()
        await db.refresh(training)
        return training

    @staticmethod
    async def get_training(db: AsyncSession, title: str) -> Optional[Training]:
        """
        Asynchronously retrieve a training by title from the database.

        Args:
            db (AsyncSession): The database session.
            title (str): The title of the training.

        Returns:
            Optional[Training]: The retrieved training or None if not found.
        """
        result = await db.execute(select(Training).filter(Training.title == title))
        training = result.scalars().first()
        return training

    @staticmethod
    async def delete_training(db: AsyncSession, title: str) -> None:
        """
        Asynchronously delete a training by title from the database.

        Args:
            db (AsyncSession): The database session.
            title (str): The title of the training to be deleted.
        """
        result = await db.execute(select(Training).filter(Training.title == title))
        training = result.scalars().first()
        if training:
            await db.delete(training)
            await db.commit()

    @staticmethod
    async def list_trainings(db: AsyncSession) -> List[Training]:
        """
        Asynchronously list all trainings from the database.

        Args:
            db (AsyncSession): The database session.

        Returns:
            List[Training]: A list of all trainings.
        """
        result = await db.execute(select(Training))
        trainings = result.scalars().all()
        return trainings
