def test_list_events(client):
    response = client.get("/api/events")
    assert response.status_code == 200
    data = response.json()
    assert "events" in data
    assert "total" in data
    assert data["total"] >= 6

def test_filter_events_by_category(client):
    response = client.get("/api/events?category=Culture")
    assert response.status_code == 200
    data = response.json()
    assert data["total"] >= 1
    for ev in data["events"]:
        assert ev["category"].lower() == "culture"

def test_search_events(client):
    response = client.get("/api/events?search=Hackathon")
    assert response.status_code == 200
    data = response.json()
    assert data["total"] >= 1
    assert "Hackathon" in data["events"][0]["title"]

def test_get_event_detail(client):
    response = client.get("/api/events/1")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == "1"
    assert "AI & the Future" in data["title"]
    assert "is_current_user_registered" in data
    assert data["is_current_user_registered"] is True # Seeded for Anwitha

def test_get_event_not_found(client):
    response = client.get("/api/events/999999")
    assert response.status_code == 404
