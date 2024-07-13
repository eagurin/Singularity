## app/services/scaling_service.py

from app.models.scaling import Scaling
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from typing import List, Optional

class ScalingService:
    @staticmethod
    async def apply_scaling(db: AsyncSession, strategy: str) -> Scaling:
        """
        Asynchronously apply a scaling strategy and save it to the database.

        Args:
            db (AsyncSession): The database session.
            strategy (str): The scaling strategy to be applied.

        Returns:
            Scaling: The applied scaling strategy.
        """
        scaling = Scaling(strategy=strategy)
        db.add(scaling)
        await db.commit()
        await db.refresh(scaling)
        return scaling

    @staticmethod
    async def get_scaling(db: AsyncSession, strategy: str) -> Optional[Scaling]:
        """
        Asynchronously retrieve a scaling strategy by its strategy name from the database.

        Args:
            db (AsyncSession): The database session.
            strategy (str): The name of the scaling strategy.

        Returns:
            Optional[Scaling]: The retrieved scaling strategy or None if not found.
        """
        result = await db.execute(select(Scaling).filter(Scaling.strategy == strategy))
        scaling = result.scalars().first()
        return scaling

    @staticmethod
    async def delete_scaling(db: AsyncSession, strategy: str) -> None:
        """
        Asynchronously delete a scaling strategy by its strategy name from the database.

        Args:
            db (AsyncSession): The database session.
            strategy (str): The name of the scaling strategy to be deleted.
        """
        result = await db.execute(select(Scaling).filter(Scaling.strategy == strategy))
        scaling = result.scalars().first()
        if scaling:
            await db.delete(scaling)
            await db.commit()

    @staticmethod
    async def list_scalings(db: AsyncSession) -> List[Scaling]:
        """
        Asynchronously list all scaling strategies from the database.

        Args:
            db (AsyncSession): The database session.

        Returns:
            List[Scaling]: A list of all scaling strategies.
        """
        result = await db.execute(select(Scaling))
        scalings = result.scalars().all()
        return scalings
