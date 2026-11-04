from typing import Optional, List
from fastapi import APIRouter, Depends, HTTPException, status, Query
from sqlalchemy.orm import Session
from app.api.deps import get_db, get_current_user, get_current_organizer
from app.models.user import User
from app.crud.crud_event import crud_event
from app.crud.crud_registration import crud_registration
from app.schemas.event import (
    EventRead,
    EventDetail,
    EventCreate,
    EventUpdate,
    EventListResponse
)
from app.schemas.organizer import EventAttendeeResponse, AttendeeListItem

router = APIRouter()

@router.get("", response_model=EventListResponse, summary="Browse campus events")
def list_events(
    category: Optional[str] = Query(None, description="Filter by event category, e.g. Tech, Culture, Workshops"),
    search: Optional[str] = Query(None, description="Search keyword in title, description, or organizer"),
    is_featured: Optional[bool] = Query(None, description="Filter featured events"),
    skip: int = Query(0, ge=0),
    limit: int = Query(100, ge=1, le=200),
    db: Session = Depends(get_db)
):
    """
    Browse events with optional category filtering and keyword search.
    Implements specification: GET /api/events
    """
    events, total = crud_event.list(
        db,
        category=category,
        search=search,
        is_featured=is_featured,
        skip=skip,
        limit=limit
    )
    return {"events": events, "total": total}

@router.get("/{id}", response_model=EventDetail, summary="Get event details")
def get_event(
    id: str,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """
    Retrieve single event details and current user registration state.
    Implements specification: GET /api/events/{id}
    """
    event = crud_event.get(db, id)
    if not event:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Event with id '{id}' not found."
        )

    is_registered = crud_event.is_user_registered(db, event.id, current_user.email)
    
    # Construct response
    data = EventDetail.model_validate(event)
    data.is_current_user_registered = is_registered
    return data

@router.post("", response_model=EventRead, status_code=status.HTTP_201_CREATED, summary="Create a new event")
def create_event(
    event_in: EventCreate,
    db: Session = Depends(get_db),
    organizer_id: str = Depends(get_current_organizer)
):
    """
    Publish a new event (restricted to organizer).
    """
    event_in.organizer_id = organizer_id
    event = crud_event.create(db, event_in)
    return event

@router.put("/{id}", response_model=EventRead, summary="Update an event")
def update_event(
    id: str,
    event_in: EventUpdate,
    db: Session = Depends(get_db),
    organizer_id: str = Depends(get_current_organizer)
):
    """
    Update existing event details.
    """
    event = crud_event.get(db, id)
    if not event:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Event with id '{id}' not found."
        )
    # Check ownership
    if organizer_id != "admin" and event.organizer_id != organizer_id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Forbidden: Only the owning organizer can modify this event."
        )

    updated = crud_event.update(db, event, event_in)
    return updated

@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT, summary="Delete an event")
def delete_event(
    id: str,
    db: Session = Depends(get_db),
    organizer_id: str = Depends(get_current_organizer)
):
    """
    Delete an event.
    """
    event = crud_event.get(db, id)
    if not event:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Event with id '{id}' not found."
        )
    if organizer_id != "admin" and event.organizer_id != organizer_id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Forbidden: Only the owning organizer can delete this event."
        )
    crud_event.delete(db, event)
    return None

@router.get("/{id}/registrations", response_model=EventAttendeeResponse, summary="Get attendee list for an event")
def get_event_registrations(
    id: str,
    db: Session = Depends(get_db),
    organizer_id: str = Depends(get_current_organizer)
):
    """
    Retrieve attendee roster for an event.
    Implements specification: GET /api/events/{id}/registrations (Attendee list, owning organizer only).
    """
    event = crud_event.get(db, id)
    if not event:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Event with id '{id}' not found."
        )

    # Restrict to owning organizer (or platform admin)
    if organizer_id != "admin" and event.organizer_id.lower() != organizer_id.lower():
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Access denied: Only the owning organizer can view this attendee roster."
        )

    attendees = crud_registration.get_by_event(db, event.id)
    return {
        "event": {
            "id": event.id,
            "title": event.title,
            "organizer": event.organizer,
            "capacity": event.capacity,
            "registered_count": len(attendees)
        },
        "registrations": attendees,
        "total": len(attendees)
    }
