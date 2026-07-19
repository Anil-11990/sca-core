from app.domain.certificate.certificate_status import (
    CertificateStatus,
)


def test_certificate_status_values():

    assert (
        CertificateStatus.ACTIVE.value
        == "Active"
    )

    assert (
        CertificateStatus.EXPIRED.value
        == "Expired"
    )

    assert (
        CertificateStatus.REVOKED.value
        == "Revoked"
    )