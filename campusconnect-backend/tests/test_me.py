def test_get_current_user_profile(client):
    response = client.get("/api/me")
    assert response.status_code == 200
    data = response.json()
    assert data["email"] == "anwitha@campus.edu"
    assert "saved_event_ids" in data
    assert len(data["saved_event_ids"]) >= 1

def test_update_current_user_profile(client):
    payload = {
        "name": "Anwitha G.",
        "grade": "Final Year CS"
    }
    response = client.put("/api/me", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "Anwitha G."
    assert data["grade"] == "Final Year CS"

def test_get_my_registrations(client):
    response = client.get("/api/me/registrations")
    assert response.status_code == 200
    data = response.json()
    assert "user" in data
    assert "registrations" in data
    assert data["total"] >= 3
    # Check enriched event object
    first_reg = data["registrations"][0]
    assert first_reg["event"] is not None

def test_bookmark_lifecycle(client):
    # Bookmark event 6
    res_add = client.post("/api/me/bookmarks/6")
    assert res_add.status_code == 200

    # Verify present in bookmarks list
    res_list = client.get("/api/me/bookmarks")
    assert res_list.status_code == 200
    b_ids = [e["id"] for e in res_list.json()]
    assert "6" in b_ids

    # Remove bookmark
    res_del = client.delete("/api/me/bookmarks/6")
    assert res_del.status_code == 200
