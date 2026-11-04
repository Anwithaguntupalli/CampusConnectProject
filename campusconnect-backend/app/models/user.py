from sqlalchemy import Column, String, DateTime, JSON
from sqlalchemy.orm import relationship
from datetime import datetime, timezone
import uuid
from app.core.database import Base

def generate_uuid() -> str:
    return str(uuid.uuid4())

class User(Base):
    __tablename__ = "users"

    id = Column(String(64), primary_key=True, default=generate_uuid, index=True)
    email = Column(String(120), unique=True, index=True, nullable=False)
    name = Column(String(120), nullable=False)
    phone = Column(String(50), nullable=True)
    department = Column(String(150), nullable=True)
    grade = Column(String(50), nullable=True)
    student_id = Column(String(60), unique=True, nullable=True, index=True)
    account_type = Column(String(50), default="Student Account")
    role = Column(String(30), default="student")  # 'student', 'organizer', 'admin'
    organizer_id = Column(String(60), nullable=True) # if role is organizer
    avatar = Column(String(500), nullable=True)
    interests = Column(JSON, default=list)  # ["AI & ML", "Web Dev", ...]
    
    created_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))
    updated_at = Column(DateTime, default=lambda: datetime.now(timezone.utc), onupdate=lambda: datetime.now(timezone.utc))

    # Relationships
    registrations = relationship("Registration", back_populates="user", cascade="all, delete-orphan")
    bookmarks = relationship("Bookmark", back_populates="user", cascade="all, delete-orphan")
    notifications = relationship("Notification", back_populates="user", cascade="all, delete-orphan")
