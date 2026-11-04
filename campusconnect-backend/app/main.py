from contextlib import asynccontextmanager
from fastapi import FastAPI, Request, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from fastapi.staticfiles import StaticFiles
import os
from pathlib import Path

from app.core.config import settings
from app.db.init_db import init_db
from app.api.v1.router import api_router

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup: ensure SQLite database tables & seed data are initialized
    init_db()
    yield
    # Shutdown logic if any

app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.VERSION,
    description="""
    ## CampusConnect REST API Server
    
    A production-grade backend powering student events, hackathons, calendar schedules,
    digital passes, and organizer management.
    
    ### Specification Endpoints:
    * **`GET /api/events`**: Browse events with search & category filtering.
    * **`GET /api/events/{id}`**: Event details & registration state.
    * **`POST /api/registrations`**: Create registration (**201 Created** or **409 Conflict**).
    * **`GET /api/me/registrations`**: Current user's registered passes.
    * **`GET /api/events/{id}/registrations`**: Attendee list (**owning organizer only**).
    
    ### Extended Features:
    * **`/api/organizer`**: Stats & CSV exports.
    * **`/api/me`**: Profile, interests, and bookmark management.
    * **`/api/notifications`**: Real-time alerts and organizer broadcasts.
    * **`/api/squads`**: Hackathon co-builder squad talent matchmaking.
    """,
    lifespan=lifespan,
    docs_url="/docs",
    redoc_url="/redoc"
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.BACKEND_CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Custom Exception Handler for Validation Errors
@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    return JSONResponse(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        content={"detail": exc.errors(), "message": "Validation Error"}
    )

# Include API Router under /api
app.include_router(api_router, prefix=settings.API_V1_STR)

# Mount frontend Single Page Application if directory exists
frontend_path = settings.FRONTEND_DIR
if frontend_path.exists() and (frontend_path / "index.html").exists():
    app.mount("/", StaticFiles(directory=str(frontend_path), html=True), name="frontend")
else:
    @app.get("/")
    def root():
        return {
            "message": "Welcome to CampusConnect API!",
            "docs": "/docs",
            "redoc": "/redoc",
            "api": "/api/events"
        }
