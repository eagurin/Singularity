## app/schemas/role.py

from pydantic import BaseModel, Field

class RoleCreate(BaseModel):
    name: str = Field(..., description="The name of the role.", min_length=1)
    description: str = Field(..., description="The description of the role.", min_length=1)

class Role(BaseModel):
    name: str = Field(..., description="The name of the role.")
    description: str = Field(..., description="The description of the role.")
