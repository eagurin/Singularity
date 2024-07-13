## app/services/role_service.py

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from typing import Optional, List
from app.models.role import Role

class RoleService:
    @staticmethod
    async def create_role(db: AsyncSession, name: str, description: str) -> Role:
        """
        Asynchronously create a new role and save it to the database.

        Args:
            db (AsyncSession): The database session.
            name (str): The name of the role.
            description (str): The description of the role.

        Returns:
            Role: The created role.
        """
        role = Role(name=name, description=description)
        db.add(role)
        await db.commit()
        await db.refresh(role)
        return role

    @staticmethod
    async def get_role(db: AsyncSession, name: str) -> Optional[Role]:
        """
        Asynchronously retrieve a role by name from the database.

        Args:
            db (AsyncSession): The database session.
            name (str): The name of the role.

        Returns:
            Optional[Role]: The retrieved role or None if not found.
        """
        result = await db.execute(select(Role).filter(Role.name == name))
        role = result.scalars().first()
        return role

    @staticmethod
    async def delete_role(db: AsyncSession, name: str) -> None:
        """
        Asynchronously delete a role by name from the database.

        Args:
            db (AsyncSession): The database session.
            name (str): The name of the role to be deleted.
        """
        result = await db.execute(select(Role).filter(Role.name == name))
        role = result.scalars().first()
        if role:
            await db.delete(role)
            await db.commit()

    @staticmethod
    async def list_roles(db: AsyncSession) -> List[Role]:
        """
        Asynchronously list all roles from the database.

        Args:
            db (AsyncSession): The database session.

        Returns:
            List[Role]: A list of all roles.
        """
        result = await db.execute(select(Role))
        roles = result.scalars().all()
        return roles
