## app/models/ethics.py

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.db.base_class import Base

class Ethics(Base):
    id = Column(Integer, primary_key=True, index=True)
    principles = relationship("EthicalPrinciple", back_populates="ethics")

    def __repr__(self) -> str:
        """
        Return a string representation of the ethics instance.

        Returns:
            str: The string representation of the ethics instance.
        """
        return f"Ethics(id={self.id})"

class EthicalPrinciple(Base):
    id = Column(Integer, primary_key=True, index=True)
    principle = Column(String, index=True)
    ethics_id = Column(Integer, ForeignKey('ethics.id'))
    ethics = relationship("Ethics", back_populates="principles")

    def __repr__(self) -> str:
        """
        Return a string representation of the ethical principle instance.

        Returns:
            str: The string representation of the ethical principle instance.
        """
        return f"EthicalPrinciple(id={self.id}, principle={self.principle})"
