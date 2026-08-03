from app.application.use_cases.remove_certificate import (
    RemoveCertificate,
)

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

from app.domain.common.value_objects.full_name import (
    FullName,
)

from app.domain.professional.professional import (
    Professional,
)

from app.infrastructure.repositories.memory_professional_repository import (
    MemoryProfessionalRepository,
)

from datetime import date


def test_remove_certificate():

    # Arrange
    # Create repository
    repo = MemoryProfessionalRepository()

    # Create professional
    professional = Professional(
        full_name=FullName("Anil Khanal"),
        primary_goal="Build ANIrex AI",
    )

    # Create certificate
    certificate = Certificate(
        name=CertificateName("AWS"),
        issuer=Issuer("Amazon"),
        credential_id=CredentialId("ABC123"),
        issued_date=date(2025, 1, 1),
        status=CertificateStatus.ACTIVE,
    )

    # Add certificate to professional
    professional.add_certificate(
        certificate
    )

    # Save professional
    repo.save(
        professional
    )


    # Execute remove
    use_case = RemoveCertificate(
        repo
    )

    updated = use_case.execute(
        professional.id,
        certificate.id,
    )


    # Assert certificate removed
    assert len(
        updated.certificates
    ) == 0