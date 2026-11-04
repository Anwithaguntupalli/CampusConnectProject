from fastapi import APIRouter, Depends, HTTPException, status, Response
from sqlalchemy.orm import Session
from app.api.deps import get_db, get_current_user
from app.models.user import User
from app.crud.crud_registration import (
    crud_registration,
    DuplicateRegistrationError,
    EventNotFoundError
)
from app.schemas.registration import (
    RegistrationCreate,
    RegistrationRead,
    RegistrationCreateResponse,
    ConflictErrorResponse,
    CheckInUpdate
)
from app.schemas.common import MessageResponse

router = APIRouter()

@router.post(
    "",
    response_model=RegistrationCreateResponse,
    status_code=status.HTTP_201_CREATED,
    responses={
        201: {"model": RegistrationCreateResponse, "description": "Registration created successfully"},
        409: {"model": ConflictErrorResponse, "description": "User already registered for this event"},
        404: {"description": "Event not found"}
    },
    summary="Create event registration"
)
def create_registration(
    registration_in: RegistrationCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """
    Register an attendee for an event.
    Implements specification: POST /api/registrations (Create registration, 201 or 409).
    """
    try:
        new_reg = crud_registration.create(
            db,
            obj_in=registration_in,
            current_user=current_user
        )
        return {
            "message": "Registration successful!",
            "status": 201,
            "registration": new_reg,
            "event": new_reg.event
        }
    except DuplicateRegistrationError as e:
        existing = e.existing_registration
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail={
                "error": "Conflict: You are already registered for this event.",
                "status": 409,
                "existing_registration": {
                    "id": existing.id,
                    "event_id": existing.event_id,
                    "ticket_id": existing.ticket_id,
                    "user_email": existing.user_email,
                    "status": existing.status,
                    "created_at": existing.created_at.isoformat()
                }
            }
        )
    except EventNotFoundError as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(e)
        )
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e)
        )

@router.get("/{id}", response_model=RegistrationRead, summary="Get registration details / digital pass")
def get_registration(
    id: str,
    db: Session = Depends(get_db)
):
    """
    Retrieve single registration pass by ID or Ticket ID.
    """
    reg = crud_registration.get(db, id)
    if not reg:
        # Also allow lookup by ticket_id directly (e.g. CC-2026-FUT-0481)
        reg = crud_registration.get_by_ticket_id(db, id)

    if not reg:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Registration with id or ticket '{id}' not found."
        )
    return reg

@router.delete("/{id}", response_model=MessageResponse, summary="Cancel registration")
def cancel_registration(
    id: str,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """
    Cancel an existing event registration.
    """
    reg = crud_registration.get(db, id)
    if not reg:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Registration '{id}' not found."
        )

    # Verify authorization
    if reg.user_email != current_user.email and current_user.role != "admin":
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Forbidden: Cannot cancel another user's registration."
        )

    crud_registration.cancel(db, reg)
    return {"message": "Registration cancelled successfully.", "status": 200}

@router.patch("/{id}/checkin", response_model=RegistrationRead, summary="Check-in attendee via QR scan")
def checkin_attendee(
    id: str,
    db: Session = Depends(get_db)
):
    """
    Mark attendee pass as checked in at the entrance venue.
    """
    reg = crud_registration.get(db, id)
    if not reg:
        reg = crud_registration.get_by_ticket_id(db, id)

    if not reg:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Registration with ticket '{id}' not found."
        )

    updated_reg = crud_registration.check_in(db, reg)
    return updated_reg
