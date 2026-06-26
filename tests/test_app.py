from fastapi.testclient import TestClient

from src.app import app


client = TestClient(app)


def test_unregister_participant_removes_email_from_activity():
    client.post("/activities/Chess Club/signup?email=test@mergington.edu")

    response = client.delete("/activities/Chess Club/participants/test@mergington.edu")

    assert response.status_code == 200
    assert "test@mergington.edu" not in client.get("/activities").json()["Chess Club"]["participants"]
