## app/services/task_service.py

from app.models.task import Task
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from typing import Optional, List

class TaskService:
    @staticmethod
    async def create_task(db: AsyncSession, name: str, action: str) -> Task:
        """
        Asynchronously create a new task and save it to the database.

        Args:
            db (AsyncSession): The database session.
            name (str): The name of the task.
            action (str): The action associated with the task.

        Returns:
            Task: The created task.
        """
        task = Task(name=name, action=action)
        db.add(task)
        await db.commit()
        await db.refresh(task)
        return task

    @staticmethod
    async def get_task(db: AsyncSession, name: str) -> Optional[Task]:
        """
        Asynchronously retrieve a task by name from the database.

        Args:
            db (AsyncSession): The database session.
            name (str): The name of the task.

        Returns:
            Optional[Task]: The retrieved task or None if not found.
        """
        result = await db.execute(select(Task).filter(Task.name == name))
        task = result.scalars().first()
        return task

    @staticmethod
    async def delete_task(db: AsyncSession, name: str) -> None:
        """
        Asynchronously delete a task by name from the database.

        Args:
            db (AsyncSession): The database session.
            name (str): The name of the task to be deleted.
        """
        result = await db.execute(select(Task).filter(Task.name == name))
        task = result.scalars().first()
        if task:
            await db.delete(task)
            await db.commit()

    @staticmethod
    async def list_tasks(db: AsyncSession) -> List[Task]:
        """
        Asynchronously list all tasks from the database.

        Args:
            db (AsyncSession): The database session.

        Returns:
            List[Task]: A list of all tasks.
        """
        result = await db.execute(select(Task))
        tasks = result.scalars().all()
        return tasks
