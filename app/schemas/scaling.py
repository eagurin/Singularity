## app/schemas/scaling.py
from pydantic import BaseModel, Field

class ScalingCreate(BaseModel):
    strategy: str = Field(..., description="The scaling strategy to be applied.", example="AutoScaling")

class Scaling(BaseModel):
    id: int = Field(..., description="The unique identifier of the scaling strategy.")
    strategy: str = Field(..., description="The applied scaling strategy.", example="AutoScaling")
