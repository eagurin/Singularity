## app/models/schemas/agent.py
from pydantic import BaseModel, Field
from typing import Optional, List
from .role import Role

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

## app/models/schemas/role.py
class RoleBase(BaseModel):
    name: str = Field(..., example="Administrator")

class RoleCreate(RoleBase):
    pass

class Role(RoleBase):
    id: int
    class Config:
        orm_mode = True

## app/models/schemas/influence.py
class InfluenceBase(BaseModel):
    name: str = Field(..., example="Positive")

class InfluenceCreate(InfluenceBase):
    pass

class Influence(InfluenceBase):
    id: int
    class Config:
        orm_mode = True

## app/models/schemas/task.py
class TaskBase(BaseModel):
    description: str = Field(..., example="Complete the project documentation.")

class TaskCreate(TaskBase):
    pass

class Task(TaskBase):
    id: int
    agent_id: Optional[int] = None
    class Config:
        orm_mode = True

## app/models/schemas/group.py
from .task import Task

class GroupBase(BaseModel):
    name: str = Field(..., example="Development Team")

class GroupCreate(GroupBase):
    pass

class Group(GroupBase):
    id: int
    tasks: List[Task] = []
    class Config:
        orm_mode = True

## app/models/schemas/news.py
class NewsBase(BaseModel):
    title: str = Field(..., example="New Feature Release")
    content: str = Field(..., example="We are excited to announce the release of...")

class NewsCreate(NewsBase):
    pass

class News(NewsBase):
    id: int
    class Config:
        orm_mode = True

## app/models/schemas/recommendation.py
class RecommendationBase(BaseModel):
    title: str = Field(..., example="Recommended Practices for Security")
    content: str = Field(..., example="It is recommended to regularly update your passwords...")

class RecommendationCreate(RecommendationBase):
    pass

class Recommendation(RecommendationBase):
    id: int
    class Config:
        orm_mode = True

## app/models/schemas/training.py
class TrainingBase(BaseModel):
    title: str = Field(..., example="Docker Basics")
    content: str = Field(..., example="Docker is a set of platform as a service products that use OS-level virtualization...")

class TrainingCreate(TrainingBase):
    pass

class Training(TrainingBase):
    id: int
    class Config:
        orm_mode = True

## app/models/schemas/feedback.py
class FeedbackBase(BaseModel):
    content: str = Field(..., example="This new feature has significantly improved my workflow!")

class FeedbackCreate(FeedbackBase):
    pass

class Feedback(FeedbackBase):
    id: int
    class Config:
        orm_mode = True
