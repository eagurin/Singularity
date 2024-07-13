## app/schemas/news.py

from pydantic import BaseModel, Field

class NewsCreate(BaseModel):
    title: str = Field(..., description="The title of the news article.", min_length=1)
    content: str = Field(..., description="The content of the news article.", min_length=1)

class News(BaseModel):
    title: str = Field(..., description="The title of the news article.")
    content: str = Field(..., description="The content of the news article.")

    class Config:
        orm_mode = True
