# app/core/config.py
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    ALLOWED_ORIGINS: list = ["*"]  # Update with your allowed origins for production

    class Config:
        env_file = ".env"

settings = Settings()
