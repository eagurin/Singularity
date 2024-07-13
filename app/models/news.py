## app/models/news.py

from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.orm import relationship
from app.db.base_class import Base

class News(Base):
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    content = Column(Text)

    def update_content(self, new_content: str) -> None:
        """
        Update the content of the news article.

        Args:
            new_content (str): The new content to be updated.
        """
        self.content = new_content

    def get_summary(self) -> str:
        """
        Get a summary of the news article.

        Returns:
            str: The summary of the news article.
        """
        return self.content[:100] + '...' if len(self.content) > 100 else self.content

    def __repr__(self) -> str:
        """
        Return a string representation of the news article.

        Returns:
            str: The string representation of the news article.
        """
        return f"News(id={self.id}, title={self.title}, content={self.content})"
