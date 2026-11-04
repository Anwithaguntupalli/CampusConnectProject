from typing import Optional, List, Tuple
from sqlalchemy.orm import Session
from sqlalchemy import or_, desc
from app.models.event import Event
from app.models.registration import Registration
from app.schemas.event import EventCreate, EventUpdate

class CRUDEvent:
    def get(self, db: Session, event_id: str) -> Optional[Event]:
        return db.query(Event).filter(Event.id == str(event_id)).first()

    def get_by_slug(self, db: Session, slug: str) -> Optional[Event]:
        return db.query(Event).filter(Event.slug == slug).first()

    def list(
        self,
        db: Session,
        category: Optional[str] = None,
        search: Optional[str] = None,
        is_featured: Optional[bool] = None,
        skip: int = 0,
        limit: int = 100
    ) -> Tuple[List[Event], int]:
        query = db.query(Event)

        if category and category.lower() != "all":
            query = query.filter(Event.category.ilike(category))

        if search:
            search_pattern = f"%{search.strip().lower()}%"
            query = query.filter(
                or_(
                    Event.title.ilike(search_pattern),
                    Event.short_desc.ilike(search_pattern),
                    Event.description.ilike(search_pattern),
                    Event.tag.ilike(search_pattern),
                    Event.location.ilike(search_pattern),
                    Event.organizer.ilike(search_pattern)
                )
            )

        if is_featured is not None:
            query = query.filter(Event.is_featured == is_featured)

        total = query.count()
        events = query.order_by(desc(Event.is_featured), Event.created_at.asc()).offset(skip).limit(limit).all()
        return events, total

    def is_user_registered(self, db: Session, event_id: str, user_email: str) -> bool:
        if not user_email:
            return False
        return db.query(Registration).filter(
            Registration.event_id == str(event_id),
            Registration.user_email == user_email.lower(),
            Registration.status.in_(["CONFIRMED", "WAITLIST", "CHECKED_IN"])
        ).first() is not None

    def create(self, db: Session, obj_in: EventCreate) -> Event:
        obj_data = obj_in.model_dump()
        if "speakers" in obj_data and obj_data["speakers"]:
            obj_data["speakers"] = [s if isinstance(s, dict) else s.model_dump() for s in obj_data["speakers"]]
        db_obj = Event(**obj_data)
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def update(self, db: Session, db_obj: Event, obj_in: EventUpdate) -> Event:
        update_data = obj_in.model_dump(exclude_unset=True)
        if "speakers" in update_data and update_data["speakers"] is not None:
            update_data["speakers"] = [s if isinstance(s, dict) else s.model_dump() for s in update_data["speakers"]]
        for field, value in update_data.items():
            setattr(db_obj, field, value)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def delete(self, db: Session, db_obj: Event) -> None:
        db.delete(db_obj)
        db.commit()

crud_event = CRUDEvent()
