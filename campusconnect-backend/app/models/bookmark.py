from sqlalchemy import Column, String, DateTime, ForeignKey, UniqueConstraint
from sqlalchemy.orm import relationship
from datetime import datetime, timezone
import uuid
from app.core.database import Base

def generate_uuid() -> str:
    return str(uuid.uuid4())

class Bookmark(Base):
    __tablename__ = "bookmarks"

    id = Column(String(64), primary_key=True, default=generate_uuid, index=True)
    user_id = Column(String(64), ForeignKey("users.id", ondelete="CASCADE"), nullable=False, index=True)
    event_id = Column(String(64), ForeignKey("events.id", ondelete="CASCADE"), nullable=False, index=True)
    created_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))

    __table_args__ = (
        UniqueConstraint('user_id', 'event_id', name='uq_user_event_bookmark'),
    )

    user = relationship("User", back_populates="bookmarks")
    event = relationship("Event", back_populates="bookmarks")
