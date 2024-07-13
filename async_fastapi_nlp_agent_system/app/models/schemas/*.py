## app/models/schemas/*.py
from pydantic import BaseModel, Field
from typing import Optional, List, Union
from datetime import datetime

# New NLP related schemas
class SentimentAnalysisRequest(BaseModel):
    text: str = Field(..., example="I love sunny days but hate the rain.")

class SentimentAnalysisResponse(BaseModel):
    result: Union[List[dict], dict]

class EntityRecognitionRequest(BaseModel):
    text: str = Field(..., example="London is a big city in the United Kingdom.")

class EntityRecognitionResponse(BaseModel):
    entities: List[dict]

class LanguageTranslationRequest(BaseModel):
    text: str = Field(..., example="Hello, how are you?")
    target_language: str = Field(..., example="es")

class LanguageTranslationResponse(BaseModel):
    translated_text: str

# Existing schemas
class RoleBase(BaseModel):
    name: str = Field(..., example="Administrator")

class RoleCreate(RoleBase):
    pass

class Role(RoleBase):
    id: int
    class Config:
        orm_mode = True

class AgentBase(BaseModel):
    name: str = Field(..., example="John Doe")
    role_id: Optional[int] = Field(None, example=1)

class AgentCreate(AgentBase):
    pass

class Agent(AgentBase):
    id: int
    role: Optional[Role] = None
    class Config:
        orm_mode = True

class TaskBase(BaseModel):
    description: str = Field(..., example="Complete the project documentation.")

class TaskCreate(TaskBase):
    pass

class Task(TaskBase):
    id: int
    agent_id: Optional[int] = None
    class Config:
        orm_mode = True

class GroupBase(BaseModel):
    name: str = Field(..., example="Development Team")

class GroupCreate(GroupBase):
    pass

class Group(GroupBase):
    id: int
    tasks: List[Task] = []
    class Config:
        orm_mode = True

class InfluenceBase(BaseModel):
    name: str = Field(..., example="Positive")

class InfluenceCreate(InfluenceBase):
    pass

class Influence(InfluenceBase):
    id: int
    class Config:
        orm_mode = True

class NewsBase(BaseModel):
    title: str = Field(..., example="New Feature Release")
    content: str = Field(..., example="We are excited to announce the release of...")

class NewsCreate(NewsBase):
    pass

class News(NewsBase):
    id: int
    class Config:
        orm_mode = True

class RecommendationBase(BaseModel):
    title: str = Field(..., example="Recommended Practices for Security")
    content: str = Field(..., example="It is recommended to regularly update your passwords...")

class RecommendationCreate(RecommendationBase):
    pass

class Recommendation(RecommendationBase):
    id: int
    class Config:
        orm_mode = True

class TrainingBase(BaseModel):
    title: str = Field(..., example="Docker Basics")
    content: str = Field(..., example="Docker is a set of platform as a service products that use OS-level virtualization...")

class TrainingCreate(TrainingBase):
    pass

class Training(TrainingBase):
    id: int
    class Config:
        orm_mode = True

class FeedbackBase(BaseModel):
    content: str = Field(..., example="This new feature has significantly improved my workflow!")

class FeedbackCreate(FeedbackBase):
    pass

class Feedback(FeedbackBase):
    id: int
    class Config:
        orm_mode = True
