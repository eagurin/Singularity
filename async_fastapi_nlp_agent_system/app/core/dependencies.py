## app/core/dependencies.py
from typing import Generator
from sqlalchemy.orm import Session
from app.db.session import SessionLocal

def get_db() -> Generator[Session, None, None]:
    """
    Dependency to get a database session.
    Yields a SQLAlchemy SessionLocal instance that can be used to execute database operations.
    """
    db: Session = SessionLocal()
    try:
        yield db
    finally:
        db.close()
