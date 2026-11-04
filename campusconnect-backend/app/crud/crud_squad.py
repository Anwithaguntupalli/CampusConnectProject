from typing import List, Optional
from sqlalchemy.orm import Session
from app.models.squad import CoBuilder, SquadInvite
from app.schemas.squad import SquadInviteCreate

class CRUDSquad:
    def list_cobuilders(self, db: Session, current_user_email: str) -> List[CoBuilder]:
        cobuilders = db.query(CoBuilder).all()
        # Find who current user invited
        invited_ids = set(
            db.query(SquadInvite.cobuilder_id).filter(
                SquadInvite.sender_email == current_user_email.strip().lower()
            ).all()
        )
        # We attach dynamic invited attribute
        result = []
        for cb in cobuilders:
            cb_dict = {
                "id": cb.id,
                "name": cb.name,
                "role": cb.role,
                "skills": cb.skills or [],
                "avatar": cb.avatar,
                "match_score": cb.match_score,
                "status": cb.status,
                "bio": cb.bio,
                "invited": (cb.id,) in invited_ids
            }
            result.append(cb_dict)
        return result

    def send_invite(self, db: Session, sender_email: str, obj_in: SquadInviteCreate) -> SquadInvite:
        existing = db.query(SquadInvite).filter(
            SquadInvite.sender_email == sender_email.strip().lower(),
            SquadInvite.cobuilder_id == obj_in.cobuilder_id
        ).first()

        if existing:
            return existing

        invite = SquadInvite(
            sender_email=sender_email.strip().lower(),
            cobuilder_id=obj_in.cobuilder_id,
            status="INVITED",
            message=obj_in.message
        )
        db.add(invite)
        db.commit()
        db.refresh(invite)
        return invite

    def list_invites(self, db: Session, sender_email: str) -> List[SquadInvite]:
        return db.query(SquadInvite).filter(
            SquadInvite.sender_email == sender_email.strip().lower()
        ).all()

crud_squad = CRUDSquad()
