from typing import Optional, List
from pydantic import BaseModel, ConfigDict
from datetime import datetime

class NotificationRead(BaseModel):
    id: str
    user_id: str
    title: str
    subtitle: Optional[str] = None
    message: str
    category: str
    event_id: Optional[str] = None
    date: Optional[str] = None
    time_slot: Optional[str] = None
    venue: Optional[str] = None
    unread: bool
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)

class NotificationListResponse(BaseModel):
    notifications: List[NotificationRead]
    unread_count: int
    total: int

class BroadcastCreate(BaseModel):
    title: str
    subtitle: Optional[str] = None
    message: str
    category: str = "Announcement"
    event_id: Optional[str] = None
    date: Optional[str] = None
    time_slot: Optional[str] = None
    venue: Optional[str] = None
