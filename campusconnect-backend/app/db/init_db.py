import logging
from sqlalchemy.orm import Session
from app.core.database import engine, SessionLocal
from app.db.base import Base
from app.models.event import Event
from app.models.user import User
from app.models.registration import Registration
from app.models.bookmark import Bookmark
from app.models.notification import Notification
from app.models.squad import CoBuilder
from app.db.seed_data import (
    EVENTS_SEED,
    USERS_SEED,
    REGISTRATIONS_SEED,
    COBUILDERS_SEED,
    NOTIFICATIONS_SEED,
    BOOKMARKS_SEED
)

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def init_db(db: Session = None) -> None:
    """
    Creates tables and seeds initial data if the database is unpopulated.
    """
    close_session = False
    if db is None:
        db = SessionLocal()
        close_session = True

    target_engine = db.get_bind()
    logger.info("Initializing database tables...")
    Base.metadata.create_all(bind=target_engine)

    try:
        # Check if events table is seeded
        if db.query(Event).first() is None:
            logger.info("Seeding initial events...")
            for e_data in EVENTS_SEED:
                event = Event(**e_data)
                db.add(event)

            logger.info("Seeding initial users...")
            for u_data in USERS_SEED:
                user = User(**u_data)
                db.add(user)

            db.commit()

            logger.info("Seeding initial registrations...")
            for r_data in REGISTRATIONS_SEED:
                reg = Registration(**r_data)
                db.add(reg)

            logger.info("Seeding co-builders...")
            for cb_data in COBUILDERS_SEED:
                cb = CoBuilder(**cb_data)
                db.add(cb)

            logger.info("Seeding notifications...")
            for n_data in NOTIFICATIONS_SEED:
                notif = Notification(**n_data)
                db.add(notif)

            logger.info("Seeding bookmarks...")
            for b_data in BOOKMARKS_SEED:
                bm = Bookmark(**b_data)
                db.add(bm)

            db.commit()
            logger.info("Database successfully seeded with Figma dataset!")
        else:
            logger.info("Database already initialized and populated.")
    finally:
        if close_session:
            db.close()

if __name__ == "__main__":
    init_db()
