## app/services/group_service.py

from app.models.group import Group
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from typing import List, Optional

class GroupService:
    @staticmethod
    async def create_group(db: AsyncSession, name: str, members: List[str]) -> Group:
        """
        Asynchronously create a new group and save it to the database.

        Args:
            db (AsyncSession): The database session.
            name (str): The name of the group.
            members (List[str]): The members of the group.

        Returns:
            Group: The created group.
        """
        group = Group(name=name, members=members)
        db.add(group)
        await db.commit()
        await db.refresh(group)
        return group

    @staticmethod
    async def get_group(db: AsyncSession, name: str) -> Optional[Group]:
        """
        Asynchronously retrieve a group by name from the database.

        Args:
            db (AsyncSession): The database session.
            name (str): The name of the group.

        Returns:
            Optional[Group]: The retrieved group or None if not found.
        """
        result = await db.execute(select(Group).filter(Group.name == name))
        group = result.scalars().first()
        return group

    @staticmethod
    async def delete_group(db: AsyncSession, name: str) -> None:
        """
        Asynchronously delete a group by name from the database.

        Args:
            db (AsyncSession): The database session.
            name (str): The name of the group to be deleted.
        """
        result = await db.execute(select(Group).filter(Group.name == name))
        group = result.scalars().first()
        if group:
            await db.delete(group)
            await db.commit()

    @staticmethod
    async def list_groups(db: AsyncSession) -> List[Group]:
        """
        Asynchronously list all groups from the database.

        Args:
            db (AsyncSession): The database session.

        Returns:
            List[Group]: A list of all groups.
        """
        result = await db.execute(select(Group))
        groups = result.scalars().all()
        return groups
