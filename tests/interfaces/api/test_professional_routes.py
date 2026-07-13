from fastapi.testclient import TestClient

from app.interfaces.api.main import app

client = TestClient(app)
import uuid

def test_create_professional_endpoint():
    response = client.post(
        "/professionals",
        json={
            "full_name": "Anil Khanal",
            "primary_goal": "Build ANIrex AI"
        },
    )

    assert response.status_code == 201

    data = response.json()

    assert data["full_name"] == "Anil Khanal"
    assert data["primary_goal"] == "Build ANIrex AI"
    assert "id" in data
def test_get_professional_endpoint():
    create = client.post(
        "/professionals",
        json={
            "full_name": "Anil Khanal",
            "primary_goal": "Build ANIrex AI"
        },
    )

    professional_id = create.json()["id"]

    response = client.get(f"/professionals/{professional_id}")

    assert response.status_code == 200

    data = response.json()

    assert data["id"] == professional_id
    assert data["full_name"] == "Anil Khanal"
def test_invalid_uuid_returns_400():
    response = client.get("/professionals/invalid-id")

    assert response.status_code == 400

def test_missing_professional_returns_404():
    response = client.get(f"/professionals/{uuid.uuid4()}")

    assert response.status_code == 404