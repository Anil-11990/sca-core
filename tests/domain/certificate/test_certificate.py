from datetime import date

import pytest

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


def create_certificate():

    return Certificate(

        name=CertificateName(
            "AWS Certified Developer Associate"
        ),

        issuer=Issuer(
            "Amazon Web Services"
        ),

        credential_id=CredentialId(
            "AWS-123456"
        ),

        issued_date=date(
            2026,
            1,
            1,
        ),

        expiry_date=date(
            2029,
            1,
            1,
        ),

        verification_url="https://verify.aws.com",
    )


def test_create_certificate():

    certificate = create_certificate()

    assert (
        certificate.name
        == CertificateName(
            "AWS Certified Developer Associate"
        )
    )

    assert (
        certificate.issuer
        == Issuer(
            "Amazon Web Services"
        )
    )

    assert (
        certificate.status
        == CertificateStatus.ACTIVE
    )


def test_certificate_has_identity():

    certificate = create_certificate()

    assert certificate.id is not None


def test_expiry_date_before_issue_date_fails():

    with pytest.raises(ValueError):

        Certificate(

            name=CertificateName(
                "Invalid Certificate"
            ),

            issuer=Issuer(
                "Test"
            ),

            credential_id=CredentialId(
                "123"
            ),

            issued_date=date(
                2026,
                1,
                1,
            ),

            expiry_date=date(
                2025,
                1,
                1,
            ),
        )


def test_certificate_without_expiry_is_valid():

    certificate = Certificate(

        name=CertificateName(
            "Lifetime Certificate"
        ),

        issuer=Issuer(
            "University"
        ),

        credential_id=CredentialId(
            "CERT-001"
        ),

        issued_date=date(
            2026,
            1,
            1,
        ),
    )

    assert certificate.expiry_date is None