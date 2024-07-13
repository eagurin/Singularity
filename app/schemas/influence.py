## app/schemas/influence.py

from pydantic import BaseModel, Field

class InfluenceCreate(BaseModel):
    name: str = Field(..., description="The name of the influence.", min_length=1)
    effect: str = Field(..., description="The effect of the influence.", min_length=1)

class Influence(BaseModel):
    name: str = Field(..., description="The name of the influence.")
    effect: str = Field(..., description="The effect of the influence.")
