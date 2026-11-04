from typing import Optional, List
from pydantic import BaseModel, ConfigDict
from datetime import datetime

class UserBase(BaseModel):
    email: str
    name: str
    phone: Optional[str] = None
    department: Optional[str] = None
    grade: Optional[str] = None
    student_id: Optional[str] = None
    account_type: Optional[str] = "Student Account"
    role: Optional[str] = "student"
    avatar: Optional[str] = None
    interests: List[str] = []

class UserCreate(UserBase):
    pass

class UserUpdate(BaseModel):
    name: Optional[str] = None
    phone: Optional[str] = None
    department: Optional[str] = None
    grade: Optional[str] = None
    avatar: Optional[str] = None
    interests: Optional[List[str]] = None

class UserRead(UserBase):
    id: str
    created_at: datetime
    updated_at: datetime
    saved_event_ids: List[str] = []

    model_config = ConfigDict(from_attributes=True)
