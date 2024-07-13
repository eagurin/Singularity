## app/schemas/recommendation.py

from pydantic import BaseModel, Field

class RecommendationCreate(BaseModel):
    title: str = Field(..., description="The title of the recommendation.", min_length=1)
    content: str = Field(..., description="The content of the recommendation.", min_length=1)

class Recommendation(BaseModel):
    title: str = Field(..., description="The title of the recommendation.")
    content: str = Field(..., description="The content of the recommendation.")
