"""
Achievement API tests.
"""

from fastapi.testclient import TestClient

from app.api.main import app

client = TestClient(app)


def create_professional():

    response = client.post(
        "/professionals",
        json={
            "full_name": "Anil Khanal",
            "primary_goal": "Build ANIrex AI",
        },
    )

    return response.json()["id"]


def test_add_achievement():

    professional_id = create_professional()

    response = client.post(
        f"/professionals/{professional_id}/achievements",
        json={
            "title": "AWS Certified",
            "issuer": "Amazon",
            "achievement_type": "certificate",
            "description": "Cloud Certification",
            "credential_url": "https://example.com",
        },
    )

    assert response.status_code == 200

    body = response.json()

    assert body["title"] == "AWS Certified"


def test_get_achievements():

    professional_id = create_professional()

    client.post(
        f"/professionals/{professional_id}/achievements",
        json={
            "title": "AWS Certified",
            "issuer": "Amazon",
            "achievement_type": "certificate",
            "description": "Cloud Certification",
            "credential_url": "https://example.com",
        },
    )

    response = client.get(
        f"/professionals/{professional_id}/achievements"
    )

    assert response.status_code == 200

    achievements = response.json()

    assert len(achievements) == 1