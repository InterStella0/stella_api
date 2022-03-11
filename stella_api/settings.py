from pydantic import BaseSettings

__all__ = ("settings",)


class Settings(BaseSettings):
    HOST: str = "localhost"
    PORT: int = 8200

    POSTGRES_HOST: str = "localhost"
    POSTGRES_PORT: int = 5656
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_DATABASE: str

    class Config:
        env_file = ".env"
        env_prefix = "STELLA_API_"
        case_sensitive = True


settings = Settings()
