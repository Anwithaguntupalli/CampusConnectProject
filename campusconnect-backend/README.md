# CampusConnect • Enterprise Backend Engine

A robust, production-grade backend engine for **CampusConnect**, built with **FastAPI**, **SQLAlchemy 2.0 ORM**, **Pydantic v2**, and **SQLite**.

It implements all endpoints specified in the API specification, powers the 12 screens of the CampusConnect Figma design, and includes automated database migrations, comprehensive seeding, and a 23-test automated test suite.

---

## 🏗️ Architecture & Clean Layered Design

```
campusconnect-backend/
├── app/
│   ├── api/
│   │   ├── deps.py               # Dependency injection (get_db, current_user, organizer)
│   │   └── v1/
│   │       ├── router.py          # Unified API Router
│   │       └── endpoints/
│   │           ├── events.py      # GET /api/events, GET /api/events/{id}, POST, PUT, DELETE, GET /api/events/{id}/registrations
│   │           ├── registrations.py # POST /api/registrations (201 / 409), GET /api/registrations/{id}, DELETE, PATCH checkin
│   │           ├── me.py          # GET /api/me, PUT /api/me, GET /api/me/registrations, GET /api/me/bookmarks, POST/DELETE bookmark
│   │           ├── organizer.py   # GET /api/organizer/stats, GET /api/organizer/events, GET /api/organizer/events/{id}/export-csv
│   │           ├── notifications.py # GET /api/notifications, PATCH /api/notifications/{id}/read, POST broadcast
│   │           ├── squads.py      # GET /api/squads/co-builders, POST /api/squads/invite, GET /api/squads/invitations
│   │           └── health.py      # GET /api/health (Uptime & DB status)
│   ├── core/
│   │   ├── config.py              # Pydantic Settings & environment variables
│   │   ├── database.py            # SQLAlchemy engine, session maker, get_db dependency
│   │   └── security.py            # Header-based user & organizer authentication
│   ├── crud/                      # Data access layer with isolated queries
│   │   ├── crud_event.py
│   │   ├── crud_registration.py   # Atomic registration & duplicate protection
│   │   ├── crud_user.py
│   │   ├── crud_notification.py
│   │   └── crud_squad.py
│   ├── db/
│   │   ├── base.py                # Base metadata registry
│   │   ├── init_db.py             # Automatic table creation & database seeder
│   │   └── seed_data.py           # Rich Figma dataset (6 events, users, passes, squads)
│   ├── models/                    # SQLAlchemy declarative ORM models
│   │   ├── user.py
│   │   ├── event.py
│   │   ├── registration.py
│   │   ├── bookmark.py
│   │   ├── notification.py
│   │   └── squad.py
│   ├── schemas/                   # Pydantic v2 validation & response serializers
│   │   ├── common.py
│   │   ├── user.py
│   │   ├── event.py
│   │   ├── registration.py
│   │   ├── organizer.py
│   │   ├── notification.py
│   │   └── squad.py
│   └── main.py                    # FastAPI application, CORS, error handlers, static mount
├── tests/                         # Pytest test suite (23/23 passing)
│   ├── conftest.py
│   ├── test_events.py
│   ├── test_registrations.py
│   ├── test_me.py
│   ├── test_organizer.py
│   └── test_squads_notif.py
├── .env.example
├── .env
├── pytest.ini
├── requirements.txt
└── run.py                         # One-click execution runner with banner
```

---

## ⚡ Specification API Endpoints

All 5 core endpoints required by the specification are fully implemented:

| Method | Endpoint | Description | Status Codes |
| :--- | :--- | :--- | :--- |
| **GET** | `/api/events` | Browse all campus events. Supports `?category=Tech` and `?search=keyword`. | `200 OK` |
| **GET** | `/api/events/{id}` | Event details including speakers, perks, and `is_current_user_registered`. | `200 OK`, `404 Not Found` |
| **POST** | `/api/registrations` | Create event registration. Returns digital pass and generates unique ticket ID. | **`201 Created`** or **`409 Conflict`** (if already registered) |
| **GET** | `/api/me/registrations` | Current user's registered passes, tickets, and event metadata. | `200 OK` |
| **GET** | `/api/events/{id}/registrations` | Attendee roster for event. **Restricted to owning organizer only**. | `200 OK`, `403 Forbidden` |

---

## 🌟 Extended Endpoints (Supporting All 12 Figma Screens)

| Method | Endpoint | Description |
| :--- | :--- | :--- |
| **GET** | `/api/me` | Current user profile, student ID, and saved event bookmarks. |
| **PUT** | `/api/me` | Update student profile, contact info, and learning interests. |
| **GET** | `/api/me/bookmarks` | List all saved events for the current student. |
| **POST** | `/api/me/bookmarks/{event_id}` | Bookmark / save an event. |
| **DELETE**| `/api/me/bookmarks/{event_id}` | Remove an event from saved bookmarks. |
| **GET** | `/api/registrations/{id}` | Lookup digital ticket pass by ID or Ticket ID (`CC-2026-FUT-0481`). |
| **PATCH**| `/api/registrations/{id}/checkin` | Check in attendee at venue door via QR scan. |
| **DELETE**| `/api/registrations/{id}` | Cancel event registration and release seat capacity. |
| **GET** | `/api/organizer/stats` | KPI metrics (published events, total registrations, turnout %, pending). |
| **GET** | `/api/organizer/events` | Roster of events managed by the authenticated organizer. |
| **GET** | `/api/organizer/events/{id}/export-csv` | Stream and download participant roster as a CSV spreadsheet. |
| **GET** | `/api/notifications` | User inbox notifications with unread counts. |
| **PATCH**| `/api/notifications/{id}/read` | Mark notification as read. |
| **POST** | `/api/notifications/broadcast` | Organizer announcement broadcast to all students. |
| **GET** | `/api/squads/co-builders` | Hackathon co-builder match talent profiles with match scores. |
| **POST** | `/api/squads/invite` | Send hackathon team invite to candidate builder. |
| **GET** | `/api/health` | Uptime and database connectivity health check. |

---

## 🚀 Getting Started

### 1. Requirements
- Python 3.10+
- Installed dependencies:
```powershell
cd "C:\Users\Anwitha Guntupalli\.gemini\antigravity\scratch\campusconnect-backend"
python -m pip install -r requirements.txt
```

### 2. Launching the Backend Server
Run the single runner script:
```powershell
python run.py
```

The server will automatically:
1. Initialize the SQLite database schema (`campusconnect.db`).
2. Populate the rich seed dataset (6 events, users, confirmed passes, bookmarks, co-builders).
3. Start the Uvicorn web server at `http://localhost:8000`.
4. Serve both the **REST API** and the **Fullstack Frontend UI** simultaneously!

---

## 📖 Interactive Documentation

Once running, explore and test the endpoints directly in your browser:
* **Swagger UI:** [http://localhost:8000/docs](http://localhost:8000/docs)
* **ReDoc:** [http://localhost:8000/redoc](http://localhost:8000/redoc)
* **OpenAPI JSON Spec:** [http://localhost:8000/openapi.json](http://localhost:8000/openapi.json)
* **Frontend Application:** [http://localhost:8000/](http://localhost:8000/)

---

## 🧪 Automated Test Suite

Run the 23 comprehensive tests verifying every single endpoint, duplicate conflict handling, authorization constraints, and cancellations:

```powershell
python -m pytest tests -v
```

Output:
```
tests/test_events.py::test_list_events PASSED                            [  4%]
tests/test_events.py::test_filter_events_by_category PASSED              [  8%]
tests/test_events.py::test_search_events PASSED                          [ 13%]
tests/test_events.py::test_get_event_detail PASSED                       [ 17%]
tests/test_events.py::test_get_event_not_found PASSED                    [ 21%]
tests/test_me.py::test_get_current_user_profile PASSED                   [ 26%]
tests/test_me.py::test_update_current_user_profile PASSED                [ 30%]
tests/test_me.py::test_get_my_registrations PASSED                       [ 34%]
tests/test_me.py::test_bookmark_lifecycle PASSED                         [ 39%]
tests/test_organizer.py::test_get_event_registrations_owning_organizer PASSED [ 43%]
tests/test_organizer.py::test_get_event_registrations_unauthorized_organizer PASSED [ 47%]
tests/test_organizer.py::test_get_organizer_stats PASSED                 [ 52%]
tests/test_organizer.py::test_export_attendees_csv PASSED                [ 56%]
tests/test_registrations.py::test_create_registration_success PASSED     [ 60%]
tests/test_registrations.py::test_create_registration_conflict_409 PASSED [ 65%]
tests/test_registrations.py::test_create_registration_event_not_found PASSED [ 69%]
tests/test_registrations.py::test_get_registration_pass PASSED           [ 73%]
tests/test_registrations.py::test_checkin_attendee PASSED                [ 78%]
tests/test_registrations.py::test_cancel_registration PASSED             [ 82%]
tests/test_squads_notif.py::test_list_notifications PASSED               [ 86%]
tests/test_squads_notif.py::test_mark_notification_read PASSED           [ 91%]
tests/test_squads_notif.py::test_list_cobuilders PASSED                  [ 95%]
tests/test_squads_notif.py::test_invite_cobuilder PASSED                 [100%]

============================= 23 passed in 0.37s ==============================
```
