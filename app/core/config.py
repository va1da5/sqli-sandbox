from pydantic import BaseSettings


class Settings(BaseSettings):
    PROJECT_NAME: str = "SQLi Sandbox"
    SQLALCHEMY_DATABASE_URI: str
    SQLALCHEMY_ECHO: bool = False
    SQLALCHEMY_TRACK_MODIFICATIONS: bool = False
    SIMULATE_NETWORK_LATENCY: bool = False

    class Config:
        env_file = ".env"
        case_sensitive = True


settings = Settings()
