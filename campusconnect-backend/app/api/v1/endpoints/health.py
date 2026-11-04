from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import text
from app.api.deps import get_db
from app.core.config import settings
from app.schemas.common import HealthCheck

router = APIRouter()

@router.get("/health", response_model=HealthCheck, summary="API & Database health check")
def health_check(db: Session = Depends(get_db)):
    """
    Returns service uptime and database connectivity status.
    """
    db_status = "connected"
    try:
        db.execute(text("SELECT 1"))
    except Exception as e:
        db_status = f"unhealthy: {str(e)}"

    return {
        "status": "healthy" if db_status == "connected" else "degraded",
        "service": settings.PROJECT_NAME,
        "version": settings.VERSION,
        "database": db_status
    }
