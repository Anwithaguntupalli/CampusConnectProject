from typing import List, Optional
from sqlalchemy.orm import Session
from app.models.notification import Notification
from app.models.user import User
from app.schemas.notification import BroadcastCreate

class CRUDNotification:
    def list_by_user(self, db: Session, user_id: str) -> List[Notification]:
        return db.query(Notification).filter(
            Notification.user_id == user_id
        ).order_by(Notification.created_at.desc()).all()

    def count_unread(self, db: Session, user_id: str) -> int:
        return db.query(Notification).filter(
            Notification.user_id == user_id,
            Notification.unread == True
        ).count()

    def mark_as_read(self, db: Session, notification_id: str, user_id: str) -> Optional[Notification]:
        notif = db.query(Notification).filter(
            Notification.id == notification_id,
            Notification.user_id == user_id
        ).first()
        if notif:
            notif.unread = False
            db.commit()
            db.refresh(notif)
        return notif

    def broadcast(self, db: Session, obj_in: BroadcastCreate) -> int:
        users = db.query(User).all()
        created_count = 0
        for user in users:
            notif = Notification(
                user_id=user.id,
                title=obj_in.title,
                subtitle=obj_in.subtitle,
                message=obj_in.message,
                category=obj_in.category,
                event_id=obj_in.event_id,
                date=obj_in.date,
                time_slot=obj_in.time_slot,
                venue=obj_in.venue,
                unread=True
            )
            db.add(notif)
            created_count += 1
        db.commit()
        return created_count

crud_notification = CRUDNotification()
