from datetime import date

from app.application.use_cases.get_certificates import (
    GetCertificates,
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


def test_get_certificates():

    repository = MemoryProfessionalRepository()

    professional = Professional(
        full_name=FullName("Anil Khanal"),
        primary_goal="Build ANIrex AI",
    )

    certificate = Certificate(
        name=CertificateName("AWS Developer"),
        issuer=Issuer("Amazon"),
        credential_id=CredentialId("AWS-001"),
        issued_date=date.today(),
        expiry_date=None,
        verification_url="",
        status=CertificateStatus.ACTIVE,
    )

    professional.add_certificate(
        certificate
    )

    repository.save(
        professional
    )

    use_case = GetCertificates(
        repository
    )

    certificates = use_case.execute(
        professional.id
    )

    assert len(certificates) == 1
    assert certificates[0].name == CertificateName(
        "AWS Developer"
    )