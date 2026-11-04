def test_get_event_registrations_owning_organizer(client):
    # Event 1 is owned by 'tech-club'
    headers = {"X-Organizer-Id": "tech-club"}
    response = client.get("/api/events/1/registrations", headers=headers)
    assert response.status_code == 200
    data = response.json()
    assert "event" in data
    assert "registrations" in data
    assert data["total"] >= 5 # 5 attendees in seed data for event 1

def test_get_event_registrations_unauthorized_organizer(client):
    # Pass different organizer id
    headers = {"X-Organizer-Id": "drama-society"}
    response = client.get("/api/events/1/registrations", headers=headers)
    assert response.status_code == 403
    assert "Access denied" in response.json()["detail"]

def test_get_organizer_stats(client):
    headers = {"X-Organizer-Id": "tech-club"}
    response = client.get("/api/organizer/stats", headers=headers)
    assert response.status_code == 200
    data = response.json()
    assert "published_events" in data
    assert "total_registrations" in data
    assert "turnout_rate" in data

def test_export_attendees_csv(client):
    headers = {"X-Organizer-Id": "tech-club"}
    response = client.get("/api/organizer/events/1/export-csv", headers=headers)
    assert response.status_code == 200
    assert response.headers["content-type"].startswith("text/csv")
    csv_text = response.text
    assert "Ticket ID" in csv_text
    assert "CC-2026-FUT-0481" in csv_text
