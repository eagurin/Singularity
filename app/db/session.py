## app/db/session.py

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from app.core.config import settings

# Create the SQLAlchemy engine for synchronous operations
engine = create_engine(
    settings.DATABASE_URL,
    connect_args={"check_same_thread": False} if "sqlite" in settings.DATABASE_URL else {}
)

# Create the SQLAlchemy engine for asynchronous operations
async_engine = create_async_engine(
    settings.DATABASE_URL_ASYNC,
    echo=True,
)

# Create a configured "Session" class for synchronous operations
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create a configured "Session" class for asynchronous operations
AsyncSessionLocal = sessionmaker(
    autocommit=False, autoflush=False, bind=async_engine, class_=AsyncSession
)

# Create a base class for our models to inherit from
Base = declarative_base()

# Dependency to get DB session for synchronous operations
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Dependency to get DB session for asynchronous operations
async def get_async_db() -> AsyncSession:
    async with AsyncSessionLocal() as session:
        yield session
