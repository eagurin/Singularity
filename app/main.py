## app/main.py

from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from app.api.v1.endpoints import (
    agents, roles, influences, stages, groups, tasks, news, recommendations, training, feedback, scaling, ethics
)
from app.core.config import settings
from app.core.logger import setup_logger
from app.db.session import SessionLocal
from app.middleware.error_handler import add_error_handlers

# Initialize the FastAPI app
app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.VERSION,
    openapi_url=f"{settings.API_V1_STR}/openapi.json"
)

# Include routers for different endpoints
app.include_router(agents.router, prefix='/api/v1/agents', tags=['agents'])
app.include_router(roles.router, prefix='/api/v1/roles', tags=['roles'])
app.include_router(influences.router, prefix='/api/v1/influences', tags=['influences'])
app.include_router(stages.router, prefix='/api/v1/stages', tags=['stages'])
app.include_router(groups.router, prefix='/api/v1/groups', tags=['groups'])
app.include_router(tasks.router, prefix='/api/v1/tasks', tags=['tasks'])
app.include_router(news.router, prefix='/api/v1/news', tags=['news'])
app.include_router(recommendations.router, prefix='/api/v1/recommendations', tags=['recommendations'])
app.include_router(training.router, prefix='/api/v1/training', tags=['training'])
app.include_router(feedback.router, prefix='/api/v1/feedback', tags=['feedback'])
app.include_router(scaling.router, prefix='/api/v1/scaling', tags=['scaling'])
app.include_router(ethics.router, prefix='/api/v1/ethics', tags=['ethics'])

# Setup logger
setup_logger()

# Add error handlers
add_error_handlers(app)

# Dependency to get DB session
def get_db() -> Session:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Root endpoint
@app.get("/", tags=["Root"])
async def read_root():
    return {"message": "Welcome to the NLP Service API"}

# Health check endpoint
@app.get("/health", tags=["Health"])
async def health_check():
    return {"status": "healthy"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
