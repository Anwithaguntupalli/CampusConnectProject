from typing import List, Optional
from pydantic import BaseModel, ConfigDict
from datetime import datetime

class AttendeeListItem(BaseModel):
    id: str
    user_name: str
    user_email: str
    phone: Optional[str] = None
    department: Optional[str] = None
    registration_type: str
    ticket_id: str
    status: str
    checked_in_at: Optional[datetime] = None
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)

class EventAttendeeResponse(BaseModel):
    event: dict
    registrations: List[AttendeeListItem]
    total: int

class OrganizerStats(BaseModel):
    published_events: int
    total_registrations: int
    turnout_rate: str
    pending_requests: int
