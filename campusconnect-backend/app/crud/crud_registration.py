from typing import Optional, List, Tuple
from sqlalchemy.orm import Session, joinedload
from datetime import datetime, timezone
import random
from app.models.registration import Registration
from app.models.event import Event
from app.models.user import User
from app.models.notification import Notification
from app.schemas.registration import RegistrationCreate

class DuplicateRegistrationError(Exception):
    def __init__(self, existing_registration: Registration):
        self.existing_registration = existing_registration
        super().__init__("User is already registered for this event.")

class EventNotFoundError(Exception):
    pass

class CRUDRegistration:
    def get(self, db: Session, registration_id: str) -> Optional[Registration]:
        return db.query(Registration).options(joinedload(Registration.event)).filter(
            Registration.id == registration_id
        ).first()

    def get_by_ticket_id(self, db: Session, ticket_id: str) -> Optional[Registration]:
        return db.query(Registration).options(joinedload(Registration.event)).filter(
            Registration.ticket_id == ticket_id.strip()
        ).first()

    def create(self, db: Session, obj_in: RegistrationCreate, current_user: Optional[User] = None) -> Registration:
        event = db.query(Event).filter(Event.id == str(obj_in.event_id)).first()
        if not event:
            raise EventNotFoundError("Event not found")

        # Resolve user email & details
        email = (obj_in.email or (current_user.email if current_user else None) or "").strip().lower()
        if not email:
            raise ValueError("Email is required for registration.")

        name = obj_in.name or (current_user.name if current_user else "Campus Attendee")
        phone = obj_in.phone or (current_user.phone if current_user else None)
        department = obj_in.department or (current_user.department if current_user else None)
        reg_type = obj_in.registration_type or "Student Attendee"

        # Check existing registration (Duplicate Check for 409 Conflict)
        existing = db.query(Registration).filter(
            Registration.event_id == event.id,
            Registration.user_email == email
        ).first()

        if existing:
            raise DuplicateRegistrationError(existing)

        # Generate unique ticket ID, e.g. CC-2026-FUT-1048
        clean_words = "".join([c for c in event.title if c.isalnum() or c.isspace()]).split()
        prefix = "".join([w[:3].upper() for w in clean_words[:2]]) or "EVT"
        rand_suffix = random.randint(1000, 9999)
        ticket_id = f"CC-2026-{prefix}-{rand_suffix}"

        # Determine status based on capacity
        status = "CONFIRMED"
        if event.capacity and event.registered_count >= event.capacity:
            status = "WAITLIST"

        reg = Registration(
            event_id=event.id,
            user_id=current_user.id if current_user else None,
            user_email=email,
            user_name=name,
            phone=phone,
            department=department,
            registration_type=reg_type,
            ticket_id=ticket_id,
            status=status,
            created_at=datetime.now(timezone.utc)
        )
        db.add(reg)

        # Increment registered count if confirmed
        event.registered_count += 1
        
        # If user exists, create notification for them
        if current_user:
            notif = Notification(
                user_id=current_user.id,
                title="Registration confirmed",
                subtitle=f"{event.title}",
                message=f"You're registered for {event.title}! Your digital pass ({ticket_id}) is ready.",
                category="Registration",
                event_id=event.id,
                date=f"{event.day}, {event.date}",
                time_slot=event.time,
                venue=event.location,
                unread=True
            )
            db.add(notif)

        db.commit()
        db.refresh(reg)
        return reg

    def get_by_user(self, db: Session, user_email: str) -> List[Registration]:
        return db.query(Registration).options(joinedload(Registration.event)).filter(
            Registration.user_email == user_email.strip().lower()
        ).order_by(Registration.created_at.desc()).all()

    def get_by_event(self, db: Session, event_id: str) -> List[Registration]:
        return db.query(Registration).filter(
            Registration.event_id == str(event_id)
        ).order_by(Registration.created_at.asc()).all()

    def check_in(self, db: Session, registration: Registration) -> Registration:
        registration.status = "CHECKED_IN"
        registration.checked_in_at = datetime.now(timezone.utc)
        db.commit()
        db.refresh(registration)
        return registration

    def cancel(self, db: Session, registration: Registration) -> Registration:
        registration.status = "CANCELLED"
        if registration.event and registration.event.registered_count > 0:
            registration.event.registered_count -= 1
        db.commit()
        db.refresh(registration)
        return registration

crud_registration = CRUDRegistration()
