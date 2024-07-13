## app/services/agent_service.py

from app.models.agent import Agent
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from typing import Optional, List

class AgentService:
    @staticmethod
    async def create_agent(db: AsyncSession, name: str, model: str) -> Agent:
        """
        Asynchronously create a new agent and save it to the database.

        Args:
            db (AsyncSession): The database session.
            name (str): The name of the agent.
            model (str): The model associated with the agent.

        Returns:
            Agent: The created agent.
        """
        agent = Agent(name=name, model=model)
        db.add(agent)
        await db.commit()
        await db.refresh(agent)
        return agent

    @staticmethod
    async def get_agent(db: AsyncSession, name: str) -> Optional[Agent]:
        """
        Asynchronously retrieve an agent by name from the database.

        Args:
            db (AsyncSession): The database session.
            name (str): The name of the agent.

        Returns:
            Optional[Agent]: The retrieved agent or None if not found.
        """
        result = await db.execute(select(Agent).filter(Agent.name == name))
        agent = result.scalars().first()
        return agent

    @staticmethod
    async def delete_agent(db: AsyncSession, name: str) -> None:
        """
        Asynchronously delete an agent by name from the database.

        Args:
            db (AsyncSession): The database session.
            name (str): The name of the agent to be deleted.
        """
        result = await db.execute(select(Agent).filter(Agent.name == name))
        agent = result.scalars().first()
        if agent:
            await db.delete(agent)
            await db.commit()

    @staticmethod
    async def list_agents(db: AsyncSession) -> List[Agent]:
        """
        Asynchronously list all agents from the database.

        Args:
            db (AsyncSession): The database session.

        Returns:
            List[Agent]: A list of all agents.
        """
        result = await db.execute(select(Agent))
        agents = result.scalars().all()
        return agents
