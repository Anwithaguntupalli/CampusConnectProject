from typing import Optional, List, Any
from pydantic import BaseModel, ConfigDict
from datetime import datetime

class Speaker(BaseModel):
    name: str
    role: str
    avatar: Optional[str] = None

class EventBase(BaseModel):
    title: str
    tag: str = "CAMPUS EVENT"
    category: str = "Tech"
    interests: List[str] = []
    hero_badge: Optional[str] = "FEATURED SESSION"
    date: str
    day: str
    time: str
    location: str
    organizer: str
    organizer_id: str = "tech-club"
    price: str = "Free Entry"
    price_val: float = 0.0
    is_featured: bool = False
    badge_color: str = "blue"
    icon: str = "cpu"
    short_desc: str
    description: str
    perks: List[str] = []
    speakers: List[Speaker] = []
    capacity: int = 200

class EventCreate(EventBase):
    slug: Optional[str] = None

class EventUpdate(BaseModel):
    title: Optional[str] = None
    tag: Optional[str] = None
    category: Optional[str] = None
    interests: Optional[List[str]] = None
    hero_badge: Optional[str] = None
    date: Optional[str] = None
    day: Optional[str] = None
    time: Optional[str] = None
    location: Optional[str] = None
    organizer: Optional[str] = None
    price: Optional[str] = None
    is_featured: Optional[bool] = None
    badge_color: Optional[str] = None
    icon: Optional[str] = None
    short_desc: Optional[str] = None
    description: Optional[str] = None
    perks: Optional[List[str]] = None
    speakers: Optional[List[Speaker]] = None
    capacity: Optional[int] = None
    status: Optional[str] = None

class EventRead(EventBase):
    id: str
    slug: Optional[str] = None
    registered_count: int = 0
    status: str = "Active"
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class EventDetail(EventRead):
    is_current_user_registered: bool = False

class EventListResponse(BaseModel):
    events: List[EventRead]
    total: int
