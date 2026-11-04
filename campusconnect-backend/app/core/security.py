from typing import Optional
from fastapi import Header, HTTPException, status
from app.core.config import settings

def get_header_user_email(x_user_email: Optional[str] = Header(None)) -> str:
    """
    Extracts user email from header 'X-User-Email'.
    Defaults to settings.DEFAULT_USER_EMAIL if not explicitly provided,
    allowing frictionless evaluation and frontend communication.
    """
    if x_user_email and x_user_email.strip():
        return x_user_email.strip().lower()
    return settings.DEFAULT_USER_EMAIL.lower()

def get_header_organizer_id(x_organizer_id: Optional[str] = Header(None)) -> str:
    """
    Extracts organizer identifier from header 'X-Organizer-Id'.
    Defaults to settings.DEFAULT_ORGANIZER_ID ('tech-club').
    """
    if x_organizer_id and x_organizer_id.strip():
        return x_organizer_id.strip().lower()
    return settings.DEFAULT_ORGANIZER_ID.lower()
