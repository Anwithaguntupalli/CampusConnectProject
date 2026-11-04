# Import all models so Base has all metadata registered before create_all is called
from app.core.database import Base
from app.models.user import User
from app.models.event import Event
from app.models.registration import Registration
from app.models.bookmark import Bookmark
from app.models.notification import Notification
from app.models.squad import CoBuilder, SquadInvite

__all__ = [
    "Base",
    "User",
    "Event",
    "Registration",
    "Bookmark",
    "Notification",
    "CoBuilder",
    "SquadInvite"
]
