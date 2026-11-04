from typing import Optional, List
from pydantic import BaseModel, ConfigDict, Field
from datetime import datetime
from app.schemas.event import EventRead

class RegistrationCreate(BaseModel):
    event_id: str = Field(..., description="ID of the event to register for", alias="eventId")
    email: Optional[str] = None
    name: Optional[str] = None
    phone: Optional[str] = None
    department: Optional[str] = None
    registration_type: Optional[str] = "Student Attendee"

    model_config = ConfigDict(populate_by_name=True)

class RegistrationRead(BaseModel):
    id: str
    event_id: str
    user_id: Optional[str] = None
    user_email: str
    user_name: str
    phone: Optional[str] = None
    department: Optional[str] = None
    registration_type: str
    ticket_id: str
    status: str
    checked_in_at: Optional[datetime] = None
    created_at: datetime
    event: Optional[EventRead] = None

    model_config = ConfigDict(from_attributes=True)

class RegistrationCreateResponse(BaseModel):
    message: str = "Registration successful!"
    status: int = 201
    registration: RegistrationRead
    event: Optional[EventRead] = None

class ConflictErrorResponse(BaseModel):
    error: str = "Conflict: You are already registered for this event."
    status: int = 409
    existing_registration: Optional[dict] = None

class UserRegistrationsResponse(BaseModel):
    user: dict
    registrations: List[RegistrationRead]
    total: int

class CheckInUpdate(BaseModel):
    status: str = "CHECKED_IN"
