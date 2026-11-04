from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.api.deps import get_db, get_current_user
from app.models.user import User
from app.crud.crud_squad import crud_squad
from app.schemas.squad import (
    CoBuilderRead,
    SquadInviteCreate,
    SquadInviteRead
)
from app.schemas.common import MessageResponse

router = APIRouter()

@router.get("/co-builders", response_model=List[CoBuilderRead], summary="List co-builder talent matches")
def get_cobuilders(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """
    Retrieve candidate builders for hackathons matching your interests.
    """
    builders = crud_squad.list_cobuilders(db, current_user.email)
    return builders

@router.post("/invite", response_model=SquadInviteRead, summary="Send squad invitation")
def invite_cobuilder(
    invite_in: SquadInviteCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """
    Invite a co-builder to team up for an upcoming hackathon.
    """
    invite = crud_squad.send_invite(db, current_user.email, invite_in)
    return invite

@router.get("/invitations", response_model=List[SquadInviteRead], summary="List sent invitations")
def list_my_invitations(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """
    List squad invitations sent by the current user.
    """
    invites = crud_squad.list_invites(db, current_user.email)
    return invites
