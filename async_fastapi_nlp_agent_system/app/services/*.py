## app/services/agent_service.py
import logging
from typing import List, Optional
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from app.models.database.agent import Agent as DBAgent
from app.models.schemas.agent import AgentCreate, Agent as SchemaAgent

class AgentService:
    def __init__(self, db: Session):
        self.db = db

    def create_agent(self, agent: AgentCreate) -> SchemaAgent:
        """
        Create a new agent and save it to the database.
        """
        db_agent = DBAgent(name=agent.name, role_id=agent.role_id)
        try:
            self.db.add(db_agent)
            self.db.commit()
            self.db.refresh(db_agent)
            return db_agent
        except SQLAlchemyError as e:
            self.db.rollback()
            logging.error(f"Failed to create agent: {e}")
            raise

    def get_agents(self, skip: int = 0, limit: int = 100) -> List[SchemaAgent]:
        """
        Retrieve agents from the database.
        """
        return self.db.query(DBAgent).offset(skip).limit(limit).all()

    def get_agent(self, agent_id: int) -> Optional[SchemaAgent]:
        """
        Retrieve a single agent by ID.
        """
        return self.db.query(DBAgent).filter(DBAgent.id == agent_id).first()

    def update_agent(self, agent_id: int, agent: AgentCreate) -> Optional[SchemaAgent]:
        """
        Update an agent's information.
        """
        db_agent = self.db.query(DBAgent).filter(DBAgent.id == agent_id).first()
        if db_agent is None:
            return None
        db_agent.name = agent.name
        db_agent.role_id = agent.role_id
        try:
            self.db.commit()
            self.db.refresh(db_agent)
            return db_agent
        except SQLAlchemyError as e:
            self.db.rollback()
            logging.error(f"Failed to update agent {agent_id}: {e}")
            raise

    def delete_agent(self, agent_id: int) -> Optional[SchemaAgent]:
        """
        Delete an agent from the database.
        """
        db_agent = self.db.query(DBAgent).filter(DBAgent.id == agent_id).first()
        if db_agent is None:
            return None
        try:
            self.db.delete(db_agent)
            self.db.commit()
            return db_agent
        except SQLAlchemyError as e:
            self.db.rollback()
            logging.error(f"Failed to delete agent {agent_id}: {e}")
            raise
