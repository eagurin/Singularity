## app/core/config.py

from pydantic import BaseSettings, Field

class Settings(BaseSettings):
    PROJECT_NAME: str = Field(default="NLP Service API", env="PROJECT_NAME")
    VERSION: str = Field(default="1.0.0", env="VERSION")
    API_V1_STR: str = Field(default="/api/v1", env="API_V1_STR")
    DATABASE_URL: str = Field(default="sqlite:///./test.db", env="DATABASE_URL")
    SECRET_KEY: str = Field(default="supersecretkey", env="SECRET_KEY")
    ACCESS_TOKEN_EXPIRE_MINUTES: int = Field(default=30, env="ACCESS_TOKEN_EXPIRE_MINUTES")
    ALGORITHM: str = Field(default="HS256", env="ALGORITHM")
    KAFKA_BROKER_URL: str = Field(default="localhost:9092", env="KAFKA_BROKER_URL")
    REDIS_URL: str = Field(default="redis://localhost:6379/0", env="REDIS_URL")
    ELASTICSEARCH_URL: str = Field(default="http://localhost:9200", env="ELASTICSEARCH_URL")
    PROMETHEUS_URL: str = Field(default="http://localhost:9090", env="PROMETHEUS_URL")
    GRAFANA_URL: str = Field(default="http://localhost:3000", env="GRAFANA_URL")

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

settings = Settings()
