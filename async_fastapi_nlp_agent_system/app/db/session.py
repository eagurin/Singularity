## app/db/session.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy.ext.declarative import declarative_base
from app.core.config import settings

# Create an engine instance
engine = create_engine(settings.DATABASE_URL, connect_args={"check_same_thread": False} if settings.DATABASE_URL.startswith("sqlite") else {})

# Create a SessionLocal class which will serve as a factory for new Session objects
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create a base class for declarative classes
Base = declarative_base()

def get_db() -> Session:
    """
    Dependency to get a database session.
    Yields a SQLAlchemy SessionLocal instance that can be used to execute database operations.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
