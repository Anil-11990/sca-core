from app.bootstrap.container import container

repository = container.professional_repository

from app.domain.professional.professional import Professional

from app.domain.common.value_objects.full_name import FullName

from app.domain.achievement.achievement import Achievement


from app.domain.achievement.value_objects.achievement_title import (
    AchievementTitle,
)

from app.domain.achievement.value_objects.issuer import (
    Issuer,
)
from datetime import date

from app.domain.certificate.certificate import (
    Certificate,
)

from app.domain.certificate.certificate_status import (
    CertificateStatus,
)

from app.domain.certificate.value_objects.certificate_name import (
    CertificateName,
)

from app.domain.certificate.value_objects.certificate_issuer import (
    Issuer,
)

from app.domain.certificate.value_objects.credential_id import (
    CredentialId,
)
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

from app.domain.achievement.achievement_type import (
    AchievementType,
)


def test_add_achievement():
    """
    API should allow adding an achievement
    to an existing Professional.
    """

    professional = Professional(
        full_name=FullName("Anil Khanal"),
        primary_goal="Build ANIrex AI",
    )

    repository.save(professional)

    response = client.post(
        f"/professionals/{professional.id}/achievements",
        json={
            "title": "AWS Certified Developer",
            "issuer": "Amazon Web Services",
            "achievement_type": "certificate",
            "description": "Associate Level",
            "credential_url": "",
        },
    )

    assert response.status_code == 200

    data = response.json()

    assert data["title"] == "AWS Certified Developer"

    assert (
        data["achievement_type"]
        == AchievementType.CERTIFICATION.value
    )

def test_get_achievements():
    """
    API should return every achievement
    belonging to a Professional.
    """

    professional = Professional(
        full_name=FullName("Anil Khanal"),
        primary_goal="Build ANIrex AI",
    )

    achievement = Achievement(
        title=AchievementTitle(
            "AWS Certified Developer"
        ),
        issuer=Issuer(
            "Amazon Web Services"
        ),
        achievement_type=AchievementType.CERTIFICATION,
    )

    professional.add_achievement(
        achievement
    )

    repository.save(professional)

    response = client.get(
        f"/professionals/{professional.id}/achievements"
    )

    assert response.status_code == 200

    data = response.json()

    assert len(data) == 1

    assert (
        data[0]["title"]
        == "AWS Certified Developer"
    )

    assert (
        data[0]["issuer"]
        == "Amazon Web Services"
    )
# ==========================================================
# Certificate API Tests
# ==========================================================

def test_add_certificate():
    """
    API should allow adding a certificate
    to an existing Professional.
    """

    professional = Professional(
        full_name=FullName("Anil Khanal"),
        primary_goal="Build ANIrex AI",
    )

    repository.save(professional)

    response = client.post(
        f"/professionals/{professional.id}/certificates",
        json={
            "name": "AWS Developer",
            "issuer": "Amazon",
            "credential_id": "AWS-001",
            "credential_url": "",
            "status": "active",
        },
    )

    assert response.status_code == 200

    data = response.json()

    assert data["name"] == "AWS Developer"

    assert data["issuer"] == "Amazon"


def test_get_certificates():
    """
    API should return every certificate
    belonging to a Professional.
    """

    professional = Professional(
        full_name=FullName("Anil Khanal"),
        primary_goal="Build ANIrex AI",
    )

    certificate = Certificate(
        name=CertificateName(
            "AWS Developer"
        ),
        issuer=Issuer(
            "Amazon"
        ),
        credential_id=CredentialId(
            "AWS-001"
        ),
        issued_date=date.today(),
        expiry_date=None,
        verification_url="",
        status=CertificateStatus.ACTIVE,
    )

    professional.add_certificate(
        certificate
    )

    repository.save(professional)

    response = client.get(
        f"/professionals/{professional.id}/certificates"
    )

    assert response.status_code == 200

    data = response.json()

    assert len(data) == 1

    assert data[0]["name"] == "AWS Developer"

    assert data[0]["issuer"] == "Amazon"

def test_add_project():

    professional = client.post(
        "/professionals",
        json={
            "full_name": "Anil Khanal",
            "primary_goal": "Build ANIrex",
        },
    ).json()

    response = client.post(
        f"/professionals/{professional['id']}/projects",
        json={
            "name": "SCA",
            "description": "Professional Operating System",
            "repository_url": "https://github.com/anirex/sca",
            "live_url": "",
            "technologies": [
                "Python",
                "FastAPI",
            ],
        },
    )

    assert response.status_code == 200

    data = response.json()

    assert data["name"] == "SCA"

def test_get_projects():

    professional = client.post(
        "/professionals",
        json={
            "full_name": "Anil Khanal",
            "primary_goal": "Build ANIrex",
        },
    ).json()

    client.post(
        f"/professionals/{professional['id']}/projects",
        json={
            "name": "SCA",
            "description": "Professional Operating System",
            "repository_url": "",
            "live_url": "",
            "technologies": [
                "Python",
            ],
        },
    )

    response = client.get(
        f"/professionals/{professional['id']}/projects"
    )

    assert response.status_code == 200

    projects = response.json()

    assert len(projects) == 1

    assert projects[0]["name"] == "SCA"