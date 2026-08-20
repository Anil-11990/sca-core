"""
Certificate API Mapper.
"""

from app.domain.certificate.certificate import Certificate

from app.api.schemas.certificate_response import (
    CertificateResponse,
)


class CertificateMapper:

    @staticmethod
    def to_response(
        certificate: Certificate,
    ) -> CertificateResponse:

        return CertificateResponse(
            id=str(certificate.id),
            name=str(certificate.name),
            issuer=str(certificate.issuer),
            credential_id=str(certificate.credential_id),
            issued_date=certificate.issued_date,
            expiry_date=certificate.expiry_date,
            verification_url=certificate.verification_url,
            status=certificate.status.value,
        )