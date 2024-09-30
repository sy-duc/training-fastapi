from pydantic_settings import BaseSettings, SettingsConfigDict
import os

class Settings(BaseSettings):
    PROJECT_NAME: str
    SECRET_KEY: str
    DATABASE_URL: str
    ACCESS_TOKEN_EXPIRE_SECONDS: int = 60 * 60 * 24 * 7  # Token expired after 7 days
    ALGORITHM: str

    model_config = SettingsConfigDict(
        env_file = ".env",  # Define the file containing environment variables
        env_ignore_empty = True, # Ignore environment variables with empty values
        extra = "ignore", # Ignore additional fields not defined in the Settings class
    ) 

# Initialize settings
settings = Settings()
