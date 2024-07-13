## app/core/config.py
from pydantic import BaseSettings, Field

class Settings(BaseSettings):
    PROJECT_NAME: str = Field(default="NLP Processing API", env="PROJECT_NAME")
    PROJECT_VERSION: str = Field(default="1.0.0", env="PROJECT_VERSION")
    API_PORT: int = Field(default=8000, env="API_PORT")
    DATABASE_URL: str = Field(default="sqlite:///./sql_app.db", env="DATABASE_URL")
    TEST_DATABASE_URL: str = Field(default="sqlite:///./test_sql_app.db", env="TEST_DATABASE_URL")
    SPACY_MODEL: str = Field(default="en_core_web_sm", env="SPACY_MODEL")

    class Config:
        env_file = ".env"
        case_sensitive = True

settings = Settings()
