"""
Application configuration.
All values are loaded from environment variables or the .env file.
Never hardcode secrets — use settings.ANTHROPIC_API_KEY etc. everywhere.
"""
from functools import lru_cache
from typing import List

from pydantic import field_validator
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
        extra="ignore",
    )

    # Application
    APP_ENV: str = "development"
    APP_NAME: str = "ResearchIQ"
    APP_VERSION: str = "0.1.0"
    DEBUG: bool = True
    LOG_LEVEL: str = "INFO"
    SECRET_KEY: str = "change-me"

    # API
    API_HOST: str = "0.0.0.0"
    API_PORT: int = 8000
    API_PREFIX: str = "/api/v1"
    ALLOWED_ORIGINS: List[str] = [
        "http://localhost:3000",
        "http://localhost:5173",
    ]

    @field_validator("ALLOWED_ORIGINS", mode="before")
    @classmethod
    def parse_cors_origins(cls, v):
        if isinstance(v, str):
            return [o.strip() for o in v.split(",")]
        return v

    # PostgreSQL
    POSTGRES_HOST: str = "localhost"
    POSTGRES_PORT: int = 5432
    POSTGRES_DB: str = "researchiq"
    POSTGRES_USER: str = "researchiq"
    POSTGRES_PASSWORD: str = "researchiq_dev_password"
    DATABASE_URL: str = (
        "postgresql+asyncpg://researchiq:researchiq_dev_password@localhost:5432/researchiq"
    )

    # Redis
    REDIS_URL: str = "redis://localhost:6379/0"
    CELERY_BROKER_URL: str = "redis://localhost:6379/0"
    CELERY_RESULT_BACKEND: str = "redis://localhost:6379/1"

    # Qdrant
    QDRANT_HOST: str = "localhost"
    QDRANT_PORT: int = 6333
    QDRANT_COLLECTION_PAPERS: str = "papers"
    QDRANT_COLLECTION_PATENTS: str = "patents"

    # LLM Providers
    ANTHROPIC_API_KEY: str = ""
    OPENAI_API_KEY: str = ""
    LANGCHAIN_TRACING_V2: bool = False
    LANGSMITH_API_KEY: str = ""

    # External Data APIs
    SEMANTIC_SCHOLAR_API_KEY: str = ""
    NCBI_API_KEY: str = ""
    SERPAPI_KEY: str = ""
    CROSSREF_EMAIL: str = "dev@researchiq.ai"

    # Auth
    JWT_SECRET_KEY: str = "change-me"
    JWT_ALGORITHM: str = "HS256"
    JWT_ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    JWT_REFRESH_TOKEN_EXPIRE_DAYS: int = 7

    # Feature Flags
    MOCK_INGESTION: bool = True
    MOCK_LLM: bool = False
    ENABLE_FUNDING_MODULE: bool = False

    @property
    def is_development(self) -> bool:
        return self.APP_ENV == "development"

    @property
    def is_production(self) -> bool:
        return self.APP_ENV == "production"

    @property
    def is_test(self) -> bool:
        return self.APP_ENV == "test"


@lru_cache
def get_settings() -> Settings:
    """Cached settings singleton — loaded once per process."""
    return Settings()


settings = get_settings()
