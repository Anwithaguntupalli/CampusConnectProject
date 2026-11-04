from sqlalchemy import Column, String, DateTime, ForeignKey, UniqueConstraint
from sqlalchemy.orm import relationship
from datetime import datetime, timezone
import uuid
from app.core.database import Base

def generate_uuid() -> str:
    return str(uuid.uuid4())

class Registration(Base):
    __tablename__ = "registrations"

    id = Column(String(64), primary_key=True, default=generate_uuid, index=True)
    event_id = Column(String(64), ForeignKey("events.id", ondelete="CASCADE"), nullable=False, index=True)
    user_id = Column(String(64), ForeignKey("users.id", ondelete="SET NULL"), nullable=True, index=True)
    user_email = Column(String(120), nullable=False, index=True)
    user_name = Column(String(120), nullable=False)
    phone = Column(String(50), nullable=True)
    department = Column(String(150), nullable=True)
    registration_type = Column(String(80), default="Student Attendee")
    ticket_id = Column(String(80), unique=True, index=True, nullable=False)
    status = Column(String(30), default="CONFIRMED") # CONFIRMED, WAITLIST, CHECKED_IN, CANCELLED
    checked_in_at = Column(DateTime, nullable=True)
    created_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))

    __table_args__ = (
        UniqueConstraint('event_id', 'user_email', name='uq_event_user_email'),
    )

    # Relationships
    event = relationship("Event", back_populates="registrations")
    user = relationship("User", back_populates="registrations")
