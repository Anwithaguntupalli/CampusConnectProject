from sqlalchemy import Column, String, Integer, Float, Boolean, Text, DateTime, JSON
from sqlalchemy.orm import relationship
from datetime import datetime, timezone
import uuid
from app.core.database import Base

def generate_uuid() -> str:
    return str(uuid.uuid4())

class Event(Base):
    __tablename__ = "events"

    id = Column(String(64), primary_key=True, default=generate_uuid, index=True)
    slug = Column(String(150), unique=True, index=True, nullable=True)
    title = Column(String(200), nullable=False, index=True)
    tag = Column(String(60), nullable=False, default="CAMPUS EVENT")
    category = Column(String(60), nullable=False, index=True, default="Tech")
    interests = Column(JSON, default=list) # ["AI & ML", "Web Dev"]
    hero_badge = Column(String(80), default="FEATURED SESSION")
    date = Column(String(60), nullable=False) # e.g. "12 Nov 2026"
    day = Column(String(20), nullable=False)  # e.g. "Thu"
    time = Column(String(80), nullable=False) # e.g. "10:00 AM - 12:00 PM"
    location = Column(String(200), nullable=False) # e.g. "Main Auditorium Hall A"
    organizer = Column(String(150), nullable=False) # e.g. "AI Club (Tech Club)"
    organizer_id = Column(String(80), nullable=False, index=True, default="tech-club")
    price = Column(String(50), default="Free Entry")
    price_val = Column(Float, default=0.0)
    is_featured = Column(Boolean, default=False, index=True)
    badge_color = Column(String(40), default="blue")
    icon = Column(String(50), default="cpu")
    short_desc = Column(String(300), nullable=False)
    description = Column(Text, nullable=False)
    perks = Column(JSON, default=list)
    speakers = Column(JSON, default=list)
    registered_count = Column(Integer, default=0)
    capacity = Column(Integer, default=200)
    status = Column(String(30), default="Active")
    
    created_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))
    updated_at = Column(DateTime, default=lambda: datetime.now(timezone.utc), onupdate=lambda: datetime.now(timezone.utc))

    # Relationships
    registrations = relationship("Registration", back_populates="event", cascade="all, delete-orphan")
    bookmarks = relationship("Bookmark", back_populates="event", cascade="all, delete-orphan")
