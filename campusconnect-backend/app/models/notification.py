from sqlalchemy import Column, String, Boolean, Text, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime, timezone
import uuid
from app.core.database import Base

def generate_uuid() -> str:
    return str(uuid.uuid4())

class Notification(Base):
    __tablename__ = "notifications"

    id = Column(String(64), primary_key=True, default=generate_uuid, index=True)
    user_id = Column(String(64), ForeignKey("users.id", ondelete="CASCADE"), nullable=False, index=True)
    title = Column(String(150), nullable=False)
    subtitle = Column(String(200), nullable=True)
    message = Column(Text, nullable=False)
    category = Column(String(50), default="Registration") # Registration, Reminder, Update
    event_id = Column(String(64), nullable=True)
    date = Column(String(80), nullable=True)
    time_slot = Column(String(80), nullable=True)
    venue = Column(String(150), nullable=True)
    unread = Column(Boolean, default=True)
    created_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))

    user = relationship("User", back_populates="notifications")
