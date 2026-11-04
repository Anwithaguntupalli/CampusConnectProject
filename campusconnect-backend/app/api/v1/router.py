from fastapi import APIRouter
from app.api.v1.endpoints import (
    events,
    registrations,
    me,
    organizer,
    notifications,
    squads,
    health
)

api_router = APIRouter()

api_router.include_router(events.router, prefix="/events", tags=["Events"])
api_router.include_router(registrations.router, prefix="/registrations", tags=["Registrations"])
api_router.include_router(me.router, prefix="/me", tags=["Current User"])
api_router.include_router(organizer.router, prefix="/organizer", tags=["Organizer Portal"])
api_router.include_router(notifications.router, prefix="/notifications", tags=["Notifications"])
api_router.include_router(squads.router, prefix="/squads", tags=["Co-Builder Squads"])
api_router.include_router(health.router, tags=["Health"])
