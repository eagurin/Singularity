## app/services/influence_service.py

from app.models.influence import Influence
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from typing import Optional, List

class InfluenceService:
    @staticmethod
    async def create_influence(db: AsyncSession, name: str, effect: str) -> Influence:
        """
        Asynchronously create a new influence and save it to the database.

        Args:
            db (AsyncSession): The database session.
            name (str): The name of the influence.
            effect (str): The effect of the influence.

        Returns:
            Influence: The created influence.
        """
        influence = Influence(name=name, effect=effect)
        db.add(influence)
        await db.commit()
        await db.refresh(influence)
        return influence

    @staticmethod
    async def get_influence(db: AsyncSession, name: str) -> Optional[Influence]:
        """
        Asynchronously retrieve an influence by name from the database.

        Args:
            db (AsyncSession): The database session.
            name (str): The name of the influence.

        Returns:
            Optional[Influence]: The retrieved influence or None if not found.
        """
        result = await db.execute(select(Influence).filter(Influence.name == name))
        influence = result.scalars().first()
        return influence

    @staticmethod
    async def delete_influence(db: AsyncSession, name: str) -> None:
        """
        Asynchronously delete an influence by name from the database.

        Args:
            db (AsyncSession): The database session.
            name (str): The name of the influence to be deleted.
        """
        result = await db.execute(select(Influence).filter(Influence.name == name))
        influence = result.scalars().first()
        if influence:
            await db.delete(influence)
            await db.commit()

    @staticmethod
    async def get_all_influences(db: AsyncSession) -> List[Influence]:
        """
        Asynchronously list all influences from the database.

        Args:
            db (AsyncSession): The database session.

        Returns:
            List[Influence]: A list of all influences.
        """
        result = await db.execute(select(Influence))
        influences = result.scalars().all()
        return influences
