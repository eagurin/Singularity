## app/services/ethics_service.py

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from typing import List, Optional
from app.models.ethics import Ethics, EthicalPrinciple

class EthicsService:
    @staticmethod
    async def apply_ethics(db: AsyncSession, principles: List[str]) -> Ethics:
        """
        Asynchronously apply ethics principles and save them to the database.

        Args:
            db (AsyncSession): The database session.
            principles (List[str]): The list of ethics principles to be applied.

        Returns:
            Ethics: The applied ethics principles.
        """
        ethics = Ethics()
        db.add(ethics)
        await db.commit()
        await db.refresh(ethics)

        for principle in principles:
            ethical_principle = EthicalPrinciple(principle=principle, ethics_id=ethics.id)
            db.add(ethical_principle)

        await db.commit()
        return ethics

    @staticmethod
    async def get_all_ethics(db: AsyncSession) -> List[Ethics]:
        """
        Asynchronously retrieve all applied ethics principles from the database.

        Args:
            db (AsyncSession): The database session.

        Returns:
            List[Ethics]: A list of all applied ethics principles.
        """
        result = await db.execute(select(Ethics))
        ethics_list = result.scalars().all()
        return ethics_list

    @staticmethod
    async def delete_ethics(db: AsyncSession, id: int) -> None:
        """
        Asynchronously delete applied ethics principles by id from the database.

        Args:
            db (AsyncSession): The database session.
            id (int): The id of the ethics principles to be deleted.
        """
        result = await db.execute(select(Ethics).filter(Ethics.id == id))
        ethics = result.scalars().first()
        if ethics:
            await db.delete(ethics)
            await db.commit()
