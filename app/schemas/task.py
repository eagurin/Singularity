## app/schemas/task.py
from pydantic import BaseModel, Field

class TaskCreate(BaseModel):
    name: str = Field(..., description="The name of the task.", min_length=1)
    action: str = Field(..., description="The action associated with the task.", min_length=1)

class Task(BaseModel):
    name: str = Field(..., description="The name of the task.")
    action: str = Field(..., description="The action associated with the task.")
