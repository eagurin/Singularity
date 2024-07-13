## app/schemas/agent.py

from pydantic import BaseModel, Field

class AgentCreate(BaseModel):
    name: str = Field(..., description="The name of the agent.")
    model: str = Field(..., description="The model associated with the agent.")

class Agent(BaseModel):
    name: str = Field(..., description="The name of the agent.")
    model: str = Field(..., description="The model associated with the agent.")
