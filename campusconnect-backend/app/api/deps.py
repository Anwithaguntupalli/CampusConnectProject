from typing import Generator, Optional
from fastapi import Depends, HTTPException, status, Header
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.core.config import settings
from app.core.security import get_header_user_email, get_header_organizer_id
from app.models.user import User
from app.crud.crud_user import crud_user

def get_current_user(
    db: Session = Depends(get_db),
    user_email: str = Depends(get_header_user_email)
) -> User:
    """
    Returns the User entity for the current request.
    If the default test user doesn't exist in the DB, it creates a profile automatically.
    """
    user = crud_user.get_by_email(db, user_email)
    if not user:
        from app.schemas.user import UserCreate
        user = crud_user.create(
            db,
            UserCreate(
                email=user_email,
                name=settings.DEFAULT_USER_NAME,
                phone="+91 98765 43210",
                department="Computer Science & Technology",
                grade="3rd Year CS",
                student_id="STU-2024-CS-094",
                account_type="Student Account",
                role="student",
                interests=["AI & ML", "Web Dev", "Design", "Leadership"]
            )
        )
    return user

def get_current_organizer(
    organizer_id: str = Depends(get_header_organizer_id)
) -> str:
    """
    Returns the verified organizer id for restricted organizer operations.
    """
    if not organizer_id:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Organizer identification header required."
        )
    return organizer_id
