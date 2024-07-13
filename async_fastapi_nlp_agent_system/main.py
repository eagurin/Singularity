from fastapi import FastAPI, Depends
from sqlalchemy.orm import sessionmaker
from app.api.v1.endpoints import agents, roles, influences, stages, groups, tasks, news, recommendations, training, feedback, sentiment_analysis, entity_recognition, language_translation, advanced_nlp_features
from app.core.config import settings
from app.db.session import SessionLocal, engine
from app.models.database.base import Base
from app.middleware.error_handler import setup_error_handlers

def create_app() -> FastAPI:
    app = FastAPI(title=settings.PROJECT_NAME, version=settings.PROJECT_VERSION)

    # Dependency
    def get_db() -> sessionmaker:
        db = SessionLocal(autocommit=False, autoflush=False, bind=engine)
        try:
            yield db
        finally:
            db.close()

    # Including routers
    app.include_router(agents.router, prefix="/api/v1/agents", tags=["agents"], dependencies=[Depends(get_db)])
    app.include_router(roles.router, prefix="/api/v1/roles", tags=["roles"], dependencies=[Depends(get_db)])
    app.include_router(influences.router, prefix="/api/v1/influences", tags=["influences"], dependencies=[Depends(get_db)])
    app.include_router(stages.router, prefix="/api/v1/stages", tags=["stages"], dependencies=[Depends(get_db)])
    app.include_router(groups.router, prefix="/api/v1/groups", tags=["groups"], dependencies=[Depends(get_db)])
    app.include_router(tasks.router, prefix="/api/v1/tasks", tags=["tasks"], dependencies=[Depends(get_db)])
    app.include_router(news.router, prefix="/api/v1/news", tags=["news"], dependencies=[Depends(get_db)])
    app.include_router(recommendations.router, prefix="/api/v1/recommendations", tags=["recommendations"], dependencies=[Depends(get_db)])
    app.include_router(training.router, prefix="/api/v1/training", tags=["training"], dependencies=[Depends(get_db)])
    app.include_router(feedback.router, prefix="/api/v1/feedback", tags=["feedback"], dependencies=[Depends(get_db)])
    app.include_router(sentiment_analysis.router, prefix="/api/v1/nlp", tags=["NLP"], dependencies=[Depends(get_db)])
    app.include_router(entity_recognition.router, prefix="/api/v1/nlp", tags=["NLP"], dependencies=[Depends(get_db)])
    app.include_router(language_translation.router, prefix="/api/v1/nlp", tags=["NLP"], dependencies=[Depends(get_db)])
    app.include_router(advanced_nlp_features.router, prefix="/api/v1/nlp", tags=["NLP"], dependencies=[Depends(get_db)])

    setup_error_handlers(app)

    @app.on_event("startup")
    async def startup_event():
        # Create database tables if they don't exist.
        Base.metadata.create_all(bind=engine)

    @app.on_event("shutdown")
    async def shutdown_event():
        # Logic for app shutdown, like closing database connections, can be added here.
        pass

    return app
