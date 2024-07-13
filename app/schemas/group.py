## app/schemas/group.py

from pydantic import BaseModel, Field
from typing import List, Optional

class GroupCreate(BaseModel):
    name: str = Field(..., description="The name of the group.")
    members: List[str] = Field(default=[], description="The list of members in the group.")

class Group(BaseModel):
    name: str = Field(..., description="The name of the group.")
    members: List[str] = Field(default=[], description="The list of members in the group.")
    class Config:
        orm_mode = True
