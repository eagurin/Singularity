## app/db/session.py
from typing import Generator

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session, sessionmaker

# Assuming settings are defined in a separate module to avoid circular imports
from app.core.config import settings

# Create an engine instance
# The DATABASE_URL is expected to be provided by the settings module
engine = create_engine(
    settings.DATABASE_URL,
    connect_args=(
        {"check_same_thread": False}
        if "sqlite" in settings.DATABASE_URL
        else {}
    ),
)

# Create a SessionLocal class which will serve as a factory for new Session objects
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create a base class for declarative classes
Base = declarative_base()


def get_db() -> Generator[Session, None, None]:
    """
    Dependency to get a database session.
    Yields a SQLAlchemy SessionLocal instance that can be used to execute database operations.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
