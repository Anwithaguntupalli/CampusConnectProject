from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.api.deps import get_db, get_current_user, get_current_organizer
from app.models.user import User
from app.crud.crud_notification import crud_notification
from app.schemas.notification import (
    NotificationRead,
    NotificationListResponse,
    BroadcastCreate
)
from app.schemas.common import MessageResponse

router = APIRouter()

@router.get("", response_model=NotificationListResponse, summary="Get inbox notifications")
def list_notifications(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """
    Retrieve message updates and event confirmations for current student.
    """
    notifs = crud_notification.list_by_user(db, current_user.id)
    unread = crud_notification.count_unread(db, current_user.id)
    return {
        "notifications": notifs,
        "unread_count": unread,
        "total": len(notifs)
    }

@router.patch("/{id}/read", response_model=NotificationRead, summary="Mark notification as read")
def mark_read(
    id: str,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """
    Mark an unread message as read.
    """
    notif = crud_notification.mark_as_read(db, id, current_user.id)
    if not notif:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Notification not found."
        )
    return notif

@router.post("/broadcast", response_model=MessageResponse, summary="Broadcast campus announcement")
def broadcast_announcement(
    broadcast_in: BroadcastCreate,
    db: Session = Depends(get_db),
    organizer_id: str = Depends(get_current_organizer)
):
    """
    Broadcast update or announcement to campus students (restricted to organizer).
    """
    sent_count = crud_notification.broadcast(db, broadcast_in)
    return {
        "message": f"Broadcast delivered successfully to {sent_count} students.",
        "status": 200
    }
