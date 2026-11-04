from typing import Generic, TypeVar, Optional, Any
from pydantic import BaseModel

T = TypeVar("T")

class MessageResponse(BaseModel):
    message: str
    status: int = 200

class HealthCheck(BaseModel):
    status: str
    service: str
    version: str
    database: str
