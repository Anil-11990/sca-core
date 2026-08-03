from datetime import date

from app.application.use_cases.update_certificate import UpdateCertificate

from app.domain.certificate.certificate import Certificate
from app.domain.certificate.certificate_status import CertificateStatus

from app.domain.certificate.value_objects.certificate_name import (
    CertificateName,
)

from app.domain.certificate.value_objects.certificate_issuer import (
    Issuer,
)

from app.domain.certificate.value_objects.credential_id import (
    CredentialId,
)

from app.domain.common.value_objects.full_name import FullName
from app.domain.professional.professional import Professional

from app.infrastructure.repositories.memory_professional_repository import (
    MemoryProfessionalRepository,
)


def test_update_certificate():

    # Arrange
    # Create repository
    repo = MemoryProfessionalRepository()

    # Create professional
    professional = Professional(
        full_name=FullName("Anil Khanal"),
        primary_goal="Build ANIrex AI",
    )

    # Existing certificate
    old_certificate = Certificate(
        name=CertificateName("AWS"),
        issuer=Issuer("Amazon"),
        credential_id=CredentialId("ABC123"),
        issued_date=date(2025, 1, 1),
        status=CertificateStatus.ACTIVE,
    )

    professional.add_certificate(
        old_certificate
    )

    repo.save(
        professional
    )


    # New updated certificate
    new_certificate = Certificate(
        name=CertificateName("Azure"),
        issuer=Issuer("Microsoft"),
        credential_id=CredentialId("XYZ999"),
        issued_date=date(2026, 1, 1),
        status=CertificateStatus.ACTIVE,
    )

    # Replace ID for update operation
    new_certificate.id = old_certificate.id

    # Execute update
    use_case = UpdateCertificate(repo)

    updated = use_case.execute(
        professional.id,
        new_certificate,
    )


    # Assert
    assert len(
        updated.certificates
    ) == 1

    assert (
        updated.certificates[0]
        .name.value
        == "Azure"
    )