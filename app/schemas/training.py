## app/schemas/training.py

from pydantic import BaseModel, Field, validator

class TrainingCreate(BaseModel):
    title: str = Field(..., description="The title of the training.", min_length=1)
    content: str = Field(..., description="The content of the training.", min_length=1)

    # Validator to ensure title and content are not empty
    @validator('title', 'content')
    def not_empty(cls, v, field):
        if not v.strip():
            raise ValueError(f"{field.name} must not be empty")
        return v

class Training(BaseModel):
    title: str = Field(..., description="The title of the training.")
    content: str = Field(..., description="The content of the training.")

    # Validator to ensure title and content are not empty
    @validator('title', 'content')
    def not_empty(cls, v, field):
        if not v.strip():
            raise ValueError(f"{field.name} must not be empty")
        return v
