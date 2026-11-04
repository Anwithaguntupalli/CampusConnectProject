# CampusConnect • Event Product Frontend

A responsive web frontend faithfully recreating the **CampusConnect Event Product UI** from the Figma design, paired with a lightweight Python REST API server implementing the exact API endpoints specified.

---

## 🎨 Implemented Figma Screens (12 Distinct Views)

You can explore every screen via the in-app navigation or click any screen on the **Floating Screen Switcher** dock at the bottom of the page:

1. **Screen 1: Explore & Browse (`Find your next campus moment.`)**
   - Hero header, real-time search bar, category filter chips (`All`, `Tech`, `Culture`, `Workshops`, `Career`, `Sports`).
   - "Featured this week" cards with direct links to event details.
   - Comprehensive upcoming campus events grid with bookmarks and quick details.

2. **Screen 2: Monthly Calendar & Coming Up (`Your campus, at a glance.`)**
   - Full interactive November 2026 calendar with date indicators, "Today" jumper, and event tags.
   - Chronological "Coming up" agenda on the right panel.

3. **Screen 3: Event Registration (`You're one step away from being there.`)**
   - Left: Event summary card with pricing, dates, and venue.
   - Right: Verified student registration form with name, email, department, and ticket category.
   - Connected directly to `POST /api/registrations`, handling both **201 Created** and **409 Conflict** (duplicate registration check).

4. **Screen 4: Notifications & Email Inbox (`Never miss a campus moment.`)**
   - 3-column layout: Navigation categories, live notifications list with unread pills, and rich email confirmation preview with "Add to calendar" and "Open Digital Pass".

5. **Screen 5: Student Hub / Dashboard (`Good morning, Anwitha 👋`)**
   - Dark gradient announcement banner ("Make room for something new.").
   - 4 KPI stat counters (Upcoming events, Saved items, Past attendances, Team invitations).
   - "Picked for you" personalized event cards.

6. **Screen 6: Event Detail View (`AI & the Future`)**
   - High-contrast hero banner with session tags, auditorium venue, and date.
   - "About this event" writeup and "What you'll get" perks checklist.
   - Organizer details, capacity counters, and "Register for free" action button (changes to "View My Digital Pass" if already registered).

7. **Screen 7: My Activity & Registrations (`My Activity`)**
   - Status tabs: `Upcoming (3)`, `Past (4)`, `Cancelled`.
   - Cards showing verified registration badges (`CONFIRMED`, `WAITLIST`) with instant access to tickets.
   - Powered by `GET /api/me/registrations`.

8. **Screen 8: Digital Event Pass (`Your digital event pass`)**
   - Authentic ticket UI with perforated cut notches, tear line, scannable QR code visual, attendee identity badge, and ticket ID (`CC-2026-FUT-0481`).
   - Action buttons: "Add to calendar" and "View event details".

9. **Screen 9: Tech Club Organizer Dashboard (`Good afternoon, Tech Club`)**
   - Organizer management portal with "+ Create event" action.
   - 4 KPI stat cards (Published events, Total registrations, 76% Attendee turnout, Pending requests).
   - Event roster table with "View Attendees" buttons.
   - Attendee List Modal fetching live attendee rosters via `GET /api/events/{id}/registrations`.

10. **Screen 10: Interest Discovery (`Made for your interests`)**
    - Interactive interest selector chips (`AI & ML`, `Web Dev`, `Design`, `Leadership`, `Cybersecurity`, `Robotics`).
    - Filtered recommendations dynamically matching student topics.

11. **Screen 11: Student Profile (`Your profile, your way`)**
    - Profile card with avatar, name (`Anwitha Guntupalli`), grade (`3rd Year CS`), and `STUDENT ACCOUNT` badge.
    - Saved bookmarks drawer with remove / view controls.

12. **Screen 12: Co-Builder Squad Matcher (`Find your people. Build something great.`)**
    - Hackathon team formation banner ("Meet your future co-builders").
    - Co-builder profiles with avatars, skills tags, match affinity percentage (`96% match`, `92% match`, etc.), and interactive "Invite to squad" buttons.

---

## ⚡ REST API Specification

The application integrates with the following REST API endpoints:

| Method | Endpoint | Description |
| :--- | :--- | :--- |
| `GET` | `/api/events` | Browse all events (supports `?category=` and `?search=`). |
| `GET` | `/api/events/{id}` | Retrieve detailed event metadata, perks, speakers, and registration status. |
| `POST` | `/api/registrations` | Create registration. Returns `201 Created` with ticket or `409 Conflict` if duplicate. |
| `GET` | `/api/me/registrations` | List registrations and tickets for current user (`anwitha@campus.edu`). |
| `GET` | `/api/events/{id}/registrations` | Retrieve attendee roster for an event (restricted to owning organizer). |

---

## 🚀 How to Run

### Option 1: Run with the Python API Server (Recommended)

1. Open PowerShell or Command Prompt.
2. Navigate to this directory:
   ```powershell
   cd "C:\Users\Anwitha Guntupalli\.gemini\antigravity\scratch\campusconnect-ui"
   ```
3. Start the server:
   ```powershell
   python server.py
   ```
4. Open your browser at:
   ```text
   http://localhost:8000
   ```

### Option 2: Open Directly in Browser (Zero Setup)

You can also double-click `index.html` to open it in your browser. The application includes a self-contained local state fallback that simulates the full API workflow (including 201 Created and 409 Conflict handling) without requiring any backend.

---

## 📂 Project Structure

```text
campusconnect-ui/
├── index.html        # Single Page Application featuring all 12 Figma screens
├── app.js            # Reactive application controller, router, and API client
├── styles.css        # Design tokens, perforated ticket styling, QR matrix, animations
├── server.py         # REST API server implementing all endpoints & static hosting
└── README.md         # Documentation and guide
```
