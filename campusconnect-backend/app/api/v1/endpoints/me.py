from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.api.deps import get_db, get_current_user
from app.models.user import User
from app.crud.crud_user import crud_user
from app.crud.crud_registration import crud_registration
from app.crud.crud_event import crud_event
from app.schemas.user import UserRead, UserUpdate
from app.schemas.registration import UserRegistrationsResponse, RegistrationRead
from app.schemas.event import EventRead
from app.schemas.common import MessageResponse

router = APIRouter()

@router.get("", response_model=UserRead, summary="Get current user profile")
def get_me(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """
    Retrieve currently authenticated user's profile and saved bookmarks.
    """
    saved_ids = crud_user.get_saved_event_ids(db, current_user.id)
    user_dict = UserRead.model_validate(current_user)
    user_dict.saved_event_ids = saved_ids
    return user_dict

@router.put("", response_model=UserRead, summary="Update user profile")
def update_me(
    user_in: UserUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """
    Update profile details, contact info, and learning interests.
    """
    updated_user = crud_user.update(db, current_user, user_in)
    saved_ids = crud_user.get_saved_event_ids(db, updated_user.id)
    user_dict = UserRead.model_validate(updated_user)
    user_dict.saved_event_ids = saved_ids
    return user_dict

@router.get("/registrations", response_model=UserRegistrationsResponse, summary="Get current user's registrations")
def get_my_registrations(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """
    Retrieve all event registrations and tickets for the logged-in student.
    Implements specification: GET /api/me/registrations
    """
    registrations = crud_registration.get_by_user(db, current_user.email)
    user_summary = {
        "id": current_user.id,
        "name": current_user.name,
        "email": current_user.email,
        "department": current_user.department,
        "student_id": current_user.student_id,
        "grade": current_user.grade
    }
    return {
        "user": user_summary,
        "registrations": registrations,
        "total": len(registrations)
    }

@router.get("/bookmarks", response_model=List[EventRead], summary="Get saved events")
def get_my_bookmarks(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """
    Retrieve list of saved/bookmarked events.
    """
    events = crud_user.get_bookmarked_events(db, current_user.id)
    return events

@router.post("/bookmarks/{event_id}", response_model=MessageResponse, summary="Bookmark an event")
def bookmark_event(
    event_id: str,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """
    Save event to user bookmarks.
    """
    event = crud_event.get(db, event_id)
    if not event:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Event '{event_id}' not found."
        )
    crud_user.add_bookmark(db, current_user.id, event.id)
    return {"message": "Event bookmarked successfully.", "status": 200}

@router.delete("/bookmarks/{event_id}", response_model=MessageResponse, summary="Remove event bookmark")
def remove_bookmark(
    event_id: str,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """
    Remove event from bookmarks.
    """
    removed = crud_user.remove_bookmark(db, current_user.id, event_id)
    if not removed:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Bookmark not found."
        )
    return {"message": "Event removed from bookmarks.", "status": 200}
