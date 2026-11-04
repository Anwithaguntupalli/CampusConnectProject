def test_create_registration_success(client):
    payload = {
        "event_id": "4",
        "email": "anwitha@campus.edu",
        "name": "Anwitha Guntupalli",
        "phone": "+91 98765 43210",
        "department": "Computer Science & Technology",
        "registration_type": "Student Attendee"
    }
    response = client.post("/api/registrations", json=payload)
    assert response.status_code == 201
    data = response.json()
    assert data["status"] == 201
    assert "registration" in data
    assert data["registration"]["event_id"] == "4"
    assert data["registration"]["ticket_id"].startswith("CC-2026-")

def test_create_registration_conflict_409(client):
    # Event 1 is already registered for Anwitha in the seed data
    payload = {
        "event_id": "1",
        "email": "anwitha@campus.edu",
        "name": "Anwitha Guntupalli"
    }
    response = client.post("/api/registrations", json=payload)
    assert response.status_code == 409
    data = response.json()
    # Check detail conforms to conflict spec
    assert "Conflict" in str(data["detail"]) or data["detail"].get("status") == 409

def test_create_registration_event_not_found(client):
    payload = {
        "event_id": "nonexistent-id",
        "email": "anwitha@campus.edu"
    }
    response = client.post("/api/registrations", json=payload)
    assert response.status_code == 404

def test_get_registration_pass(client):
    response = client.get("/api/registrations/reg-1")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == "reg-1"
    assert data["ticket_id"] == "CC-2026-FUT-0481"
    assert data["status"] == "CONFIRMED"

def test_checkin_attendee(client):
    response = client.patch("/api/registrations/reg-1/checkin")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "CHECKED_IN"

def test_cancel_registration(client):
    # Create temp registration first
    payload = {
        "event_id": "5",
        "email": "anwitha@campus.edu",
        "name": "Anwitha Guntupalli"
    }
    create_res = client.post("/api/registrations", json=payload)
    reg_id = create_res.json()["registration"]["id"]

    del_res = client.delete(f"/api/registrations/{reg_id}")
    assert del_res.status_code == 200
    assert del_res.json()["status"] == 200
