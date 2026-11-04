def test_list_notifications(client):
    response = client.get("/api/notifications")
    assert response.status_code == 200
    data = response.json()
    assert "notifications" in data
    assert "unread_count" in data
    assert data["total"] >= 4

def test_mark_notification_read(client):
    response = client.patch("/api/notifications/notif-1/read")
    assert response.status_code == 200
    assert response.json()["unread"] is False

def test_list_cobuilders(client):
    response = client.get("/api/squads/co-builders")
    assert response.status_code == 200
    data = response.json()
    assert len(data) >= 4
    first = data[0]
    assert "name" in first
    assert "skills" in first
    assert "match_score" in first

def test_invite_cobuilder(client):
    payload = {
        "cobuilder_id": "cb-1",
        "message": "Let's team up for CodeSphere Hackathon!"
    }
    response = client.post("/api/squads/invite", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert data["cobuilder_id"] == "cb-1"
    assert data["status"] == "INVITED"
