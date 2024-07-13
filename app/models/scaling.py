## app/models/scaling.py

from sqlalchemy import Column, Integer, String
from app.db.base_class import Base

class Scaling(Base):
    id = Column(Integer, primary_key=True, index=True)
    strategy = Column(String, index=True)

    def __init__(self, strategy: str):
        """
        Initialize a Scaling instance.

        Args:
            strategy (str): The scaling strategy to be applied.
        """
        self.strategy = strategy

    def __repr__(self) -> str:
        """
        Return a string representation of the scaling strategy.

        Returns:
            str: The string representation of the scaling strategy.
        """
        return f"Scaling(id={self.id}, strategy={self.strategy})"
