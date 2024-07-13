from fastapi import APIRouter, Depends, HTTPException
from typing import List
from sqlalchemy.orm import Session
from app.models.schemas.agent import AgentCreate, Agent
from app.services.agent_service import AgentService
from app.core.dependencies import get_db

router = APIRouter()

@router.post("/", response_model=Agent, status_code=201)
def create_agent(agent: AgentCreate, db: Session = Depends(get_db)):
    """
    Create a new agent and save it to the database.
    """
    agent_service = AgentService(db)
    return agent_service.create_agent(agent)

@router.get("/", response_model=List[Agent])
def read_agents(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """
    Retrieve agents from the database.
    """
    agent_service = AgentService(db)
    return agent_service.get_agents(skip=skip, limit=limit)

@router.get("/{agent_id}", response_model=Agent)
def read_agent(agent_id: int, db: Session = Depends(get_db)):
    """
    Retrieve a single agent by ID.
    """
    agent_service = AgentService(db)
    db_agent = agent_service.get_agent(agent_id)
    if db_agent is None:
        raise HTTPException(status_code=404, detail="Agent not found")
    return db_agent

@router.put("/{agent_id}", response_model=Agent)
def update_agent(agent_id: int, agent: AgentCreate, db: Session = Depends(get_db)):
    """
    Update an agent's information.
    """
    agent_service = AgentService(db)
    updated_agent = agent_service.update_agent(agent_id, agent)
    if updated_agent is None:
        raise HTTPException(status_code=404, detail="Agent not found")
    return updated_agent

@router.delete("/{agent_id}", response_model=Agent)
def delete_agent(agent_id: int, db: Session = Depends(get_db)):
    """
    Delete an agent from the database.
    """
    agent_service = AgentService(db)
    deleted_agent = agent_service.delete_agent(agent_id)
    if deleted_agent is None:
        raise HTTPException(status_code=404, detail="Agent not found")
    return deleted_agent
