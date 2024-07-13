## app/schemas/feedback.py
from pydantic import BaseModel, Field, validator

class FeedbackCreate(BaseModel):
    user: str = Field(..., description="The user who provided the feedback.", min_length=1)
    content: str = Field(..., description="The content of the feedback.", min_length=1)

    @validator('user', 'content')
    def not_empty(cls, v, field):
        if not v.strip():
            raise ValueError(f"{field.name} must not be empty")
        return v

class Feedback(BaseModel):
    user: str = Field(..., description="The user who provided the feedback.")
    content: str = Field(..., description="The content of the feedback.")

    @validator('user', 'content')
    def not_empty(cls, v, field):
        if not v.strip():
            raise ValueError(f"{field.name} must not be empty")
        return v
