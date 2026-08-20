"""
Professional API tests.
"""

from fastapi.testclient import TestClient

from app.api.main import app


client = TestClient(app)


def test_create_professional():

    response = client.post(
        "/professionals",
        json={
            "full_name": "Anil Khanal",
            "primary_goal": "Build ANIrex AI",
        },
    )

    assert response.status_code == 201

    body = response.json()

    assert body["full_name"] == "Anil Khanal"

    assert body["primary_goal"] == "Build ANIrex AI"


def test_get_professional():

    created = client.post(
        "/professionals",
        json={
            "full_name": "Anil Khanal",
            "primary_goal": "Build ANIrex AI",
        },
    )

    professional_id = created.json()["id"]

    response = client.get(
        f"/professionals/{professional_id}"
    )

    assert response.status_code == 200

    assert response.json()["id"] == professional_id