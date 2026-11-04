from typing import List, Union
from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import AnyHttpUrl, field_validator
import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent.parent

class Settings(BaseSettings):
    PROJECT_NAME: str = "CampusConnect API"
    VERSION: str = "1.0.0"
    API_V1_STR: str = "/api"
    ENVIRONMENT: str = "development"
    DEBUG: bool = True
    
    # Database
    DATABASE_URL: str = f"sqlite:///{BASE_DIR}/campusconnect.db"
    
    # CORS
    BACKEND_CORS_ORIGINS: List[str] = [
        "http://localhost",
        "http://localhost:8000",
        "http://127.0.0.1:8000",
        "http://localhost:3000",
        "http://localhost:5173",
        "http://localhost:5500",
        "*"
    ]
    
    # Default User Simulation
    DEFAULT_USER_EMAIL: str = "anwitha@campus.edu"
    DEFAULT_USER_NAME: str = "Anwitha Guntupalli"
    DEFAULT_ORGANIZER_ID: str = "tech-club"
    
    # Static files directory for frontend
    FRONTEND_DIR: Path = BASE_DIR.parent / "campusconnect-ui"
    
    model_config = SettingsConfigDict(
        case_sensitive=True,
        env_file=".env",
        extra="allow"
    )

settings = Settings()
