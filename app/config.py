import os
from pathlib import Path
from pydantic import BaseSettings


BASE_DIR = Path(__file__).resolve().parent.parent
ENV_FILE = ".env"
ENV_PATH = os.path.join(BASE_DIR, ENV_FILE)


class Settings(BaseSettings):
    DATABASE_PORT: int
    POSTGRES_PASSWORD: str
    POSTGRES_USER: str
    POSTGRES_DB: str
    POSTGRES_HOST: str
    POSTGRES_HOSTNAME: str

    JWT_PUBLIC_KEY: str
    JWT_PRIVATE_KEY: str
    REFRESH_TOKEN_EXPIRES_IN: int
    ACCESS_TOKEN_EXPIRES_IN: int
    JWT_ALGORITHM: str

    CLIENT_ORIGIN: str

    class Config:
        env_file = ENV_PATH
        env_file_encoding = "utf-8"


settings = Settings()
