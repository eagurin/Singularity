## app/models/training.py

from sqlalchemy import Column, Integer, String, Text
from app.db.base_class import Base

class Training(Base):
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    content = Column(Text)

    def update_content(self, new_content: str) -> None:
        """
        Update the content of the training.

        Args:
            new_content (str): The new content to be updated.
        """
        self.content = new_content

    def get_summary(self) -> str:
        """
        Get a summary of the training.

        Returns:
            str: The summary of the training.
        """
        return self.content[:100] + '...' if len(self.content) > 100 else self.content

    def __repr__(self) -> str:
        """
        Return a string representation of the training.

        Returns:
            str: The string representation of the training.
        """
        return f"Training(id={self.id}, title={self.title}, content={self.content})"
