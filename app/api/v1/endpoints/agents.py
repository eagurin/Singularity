## app/api/v1/endpoints/agents.py

from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from typing import List

from app.schemas.agent import AgentCreate, Agent
from app.services.agent_service import AgentService
from app.db.session import get_db

router = APIRouter()

@router.post('/', response_model=Agent, status_code=201)
async def create_agent(agent: AgentCreate, db: Session = Depends(get_db)):
    """
    Create a new agent.
    """
    return await AgentService.create_agent(db, agent.name, agent.model)

@router.get('/{name}', response_model=Agent)
async def get_agent(name: str, db: Session = Depends(get_db)):
    """
    Get an agent by name.
    """
    agent = await AgentService.get_agent(db, name)
    if not agent:
        raise HTTPException(status_code=404, detail='Agent not found')
    return agent

@router.delete('/{name}', status_code=204)
async def delete_agent(name: str, db: Session = Depends(get_db)):
    """
    Delete an agent by name.
    """
    await AgentService.delete_agent(db, name)
