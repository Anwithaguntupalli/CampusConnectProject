from sqlalchemy import Column, String, Text, DateTime, JSON, ForeignKey
from datetime import datetime, timezone
import uuid
from app.core.database import Base

def generate_uuid() -> str:
    return str(uuid.uuid4())

class CoBuilder(Base):
    __tablename__ = "cobuilders"

    id = Column(String(64), primary_key=True, default=generate_uuid, index=True)
    name = Column(String(120), nullable=False)
    role = Column(String(100), nullable=False) # e.g. "Frontend Developer", "ML Engineer"
    skills = Column(JSON, default=list) # ["React", "TypeScript", ...]
    avatar = Column(String(500), nullable=True)
    match_score = Column(String(20), default="90%")
    status = Column(String(80), default="Available")
    bio = Column(Text, nullable=True)
    created_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))

class SquadInvite(Base):
    __tablename__ = "squad_invites"

    id = Column(String(64), primary_key=True, default=generate_uuid, index=True)
    sender_email = Column(String(120), nullable=False, index=True)
    cobuilder_id = Column(String(64), ForeignKey("cobuilders.id", ondelete="CASCADE"), nullable=False)
    status = Column(String(30), default="INVITED") # INVITED, ACCEPTED, CANCELLED
    message = Column(Text, nullable=True)
    created_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))
