from typing import Optional, List
from sqlalchemy.orm import Session
from app.models.user import User
from app.models.bookmark import Bookmark
from app.models.event import Event
from app.schemas.user import UserCreate, UserUpdate

class CRUDUser:
    def get_by_email(self, db: Session, email: str) -> Optional[User]:
        return db.query(User).filter(User.email == email.strip().lower()).first()

    def get(self, db: Session, user_id: str) -> Optional[User]:
        return db.query(User).filter(User.id == user_id).first()

    def create(self, db: Session, obj_in: UserCreate) -> User:
        data = obj_in.model_dump()
        data["email"] = data["email"].strip().lower()
        user = User(**data)
        db.add(user)
        db.commit()
        db.refresh(user)
        return user

    def update(self, db: Session, db_obj: User, obj_in: UserUpdate) -> User:
        update_data = obj_in.model_dump(exclude_unset=True)
        for field, value in update_data.items():
            setattr(db_obj, field, value)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def get_saved_event_ids(self, db: Session, user_id: str) -> List[str]:
        bookmarks = db.query(Bookmark.event_id).filter(Bookmark.user_id == user_id).all()
        return [b[0] for b in bookmarks]

    def get_bookmarked_events(self, db: Session, user_id: str) -> List[Event]:
        return db.query(Event).join(Bookmark, Bookmark.event_id == Event.id).filter(
            Bookmark.user_id == user_id
        ).all()

    def add_bookmark(self, db: Session, user_id: str, event_id: str) -> Bookmark:
        existing = db.query(Bookmark).filter(
            Bookmark.user_id == user_id,
            Bookmark.event_id == str(event_id)
        ).first()
        if existing:
            return existing
        b = Bookmark(user_id=user_id, event_id=str(event_id))
        db.add(b)
        db.commit()
        db.refresh(b)
        return b

    def remove_bookmark(self, db: Session, user_id: str, event_id: str) -> bool:
        b = db.query(Bookmark).filter(
            Bookmark.user_id == user_id,
            Bookmark.event_id == str(event_id)
        ).first()
        if b:
            db.delete(b)
            db.commit()
            return True
        return False

crud_user = CRUDUser()
