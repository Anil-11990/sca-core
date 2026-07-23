from app.domain.certificate.certificate import Certificate
from app.application.dto.responses.certificate_response import (
    CertificateResponse,
)


class CertificateMapper:
    """
    Maps Certificate entity to DTO.
    """

    @staticmethod
    def to_response(
        certificate: Certificate,
    ) -> CertificateResponse:

        return CertificateResponse(
            id=str(certificate.id),
            name=str(certificate.name),
            issuer=str(certificate.issuer),
            credential_id=str(
                certificate.credential_id
            ),
            status=certificate.status.value,
        )