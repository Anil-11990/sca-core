from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_add_skill():
    professional = client.post(
        "/professionals",
        json={
            "full_name": "Anil Khanal",
            "primary_goal": "Build ANIrex AI",
        },
    )

    professional_id = professional.json()["id"]

    response = client.post(
        f"/professionals/{professional_id}/skills",
        json={
            "name": "Python",
        },
    )

    assert response.status_code == 200
    assert response.json()["name"] == "Python"


def test_get_skills():
    professional = client.post(
        "/professionals",
        json={
            "full_name": "Anil Khanal",
            "primary_goal": "Build ANIrex AI",
        },
    )

    professional_id = professional.json()["id"]

    client.post(
        f"/professionals/{professional_id}/skills",
        json={
            "name": "Python",
        },
    )

    response = client.get(
        f"/professionals/{professional_id}/skills"
    )

    assert response.status_code == 200
    assert len(response.json()) == 1
    assert response.json()[0]["name"] == "Python"