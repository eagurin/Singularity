## app/models/database/agent.py
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from .base import Base

class Agent(Base):
    __tablename__ = "agents"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    role_id = Column(Integer, ForeignKey("roles.id"))

    role = relationship("Role", back_populates="agents")

## app/models/database/role.py
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from .base import Base

class Role(Base):
    __tablename__ = "roles"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)

    agents = relationship("Agent", back_populates="role")

## app/models/database/influence.py
from sqlalchemy import Column, Integer, String
from .base import Base

class Influence(Base):
    __tablename__ = "influences"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)

## app/models/database/task.py
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from .base import Base

class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True)
    description = Column(String, index=True)
    agent_id = Column(Integer, ForeignKey("agents.id"))

    agent = relationship("Agent")

## app/models/database/group.py
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from .base import Base

class Group(Base):
    __tablename__ = "groups"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)

    tasks = relationship("Task", secondary="group_tasks")

## app/models/database/news.py
from sqlalchemy import Column, Integer, String, Text
from .base import Base

class News(Base):
    __tablename__ = "news"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    content = Column(Text)

## app/models/database/recommendation.py
from sqlalchemy import Column, Integer, String, Text
from .base import Base

class Recommendation(Base):
    __tablename__ = "recommendations"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    content = Column(Text)

## app/models/database/training.py
from sqlalchemy import Column, Integer, String, Text
from .base import Base

class Training(Base):
    __tablename__ = "training"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    content = Column(Text)

## app/models/database/feedback.py
from sqlalchemy import Column, Integer, String, Text
from .base import Base

class Feedback(Base):
    __tablename__ = "feedback"

    id = Column(Integer, primary_key=True, index=True)
    content = Column(Text)

## app/models/database/base.py
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
