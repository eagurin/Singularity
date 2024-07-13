## app/schemas/ethics.py
from typing import List
from pydantic import BaseModel, Field

class EthicsCreate(BaseModel):
    principles: List[str] = Field(default=[], description="List of ethical principles to be applied.")

class Ethics(BaseModel):
    id: int = Field(..., description="The unique identifier of the applied ethics.")
    principles: List[str] = Field(default=[], description="List of applied ethical principles.")
