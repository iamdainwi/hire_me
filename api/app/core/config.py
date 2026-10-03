from pathlib import Path

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict

# api/app/core/config.py → parents[2] = api/
ENV_FILE = Path(__file__).resolve().parents[2] / ".env"


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=ENV_FILE, extra="ignore")

    DATABASE_URL: str
    SECRET_KEY: str = Field(min_length=32)
    JWT_ALGORITHM: str
    ACCESS_TTL_MIN: int
    REFRESH_TTL_DAYS: int
    VERIFY_TTL_HOURS: int
    FRONTEND_URL: str


settings = Settings()  # pyright: ignore[reportCallIssue]
