"""
Certificate API Routes.
"""

from datetime import date
from uuid import UUID

from fastapi import APIRouter
from fastapi import HTTPException

from app.bootstrap.container import container

from app.domain.certificate.certificate import Certificate

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

from app.api.schemas.certificate_request import (
    CertificateRequest,
)

from app.api.mappers.certificate_mapper import (
    CertificateMapper,
)


router = APIRouter(
    prefix="/certificates",
    tags=["Certificates"],
)


# ==========================================================
# Add Certificate
# ==========================================================

@router.post("/{professional_id}")
def add_certificate(
    professional_id: UUID,
    request: CertificateRequest,
):

    certificate = Certificate(
        name=CertificateName(
            request.name
        ),
        issuer=Issuer(
            request.issuer
        ),
        credential_id=CredentialId(
            request.credential_id
        ),
        issued_date=date.today(),
        verification_url=request.verification_url,
        status=CertificateStatus(
            request.status
        ),
    )

    professional = (
        container
        .add_certificate_use_case()
        .execute(
            professional_id,
            certificate,
        )
    )

    if professional is None:
        raise HTTPException(
            status_code=404,
            detail="Professional not found",
        )

    return CertificateMapper.to_response(
        certificate
    )


# ==========================================================
# Get Certificates
# ==========================================================

@router.get("/{professional_id}")
def get_certificates(
    professional_id: UUID,
):

    certificates = (
        container
        .get_certificates_use_case()
        .execute(
            professional_id
        )
    )

    return [
        CertificateMapper.to_response(
            certificate
        )
        for certificate in certificates
    ]


# ==========================================================
# Remove Certificate
# ==========================================================

@router.delete("/{professional_id}/{certificate_id}")
def remove_certificate(
    professional_id: UUID,
    certificate_id: UUID,
):

    professional = (
        container
        .remove_certificate_use_case()
        .execute(
            professional_id,
            certificate_id,
        )
    )

    if professional is None:
        raise HTTPException(
            status_code=404,
            detail="Certificate not found",
        )

    return {
        "message": "Certificate removed"
    }


# ==========================================================
# Update Certificate
# ==========================================================

@router.patch("/{professional_id}/{certificate_id}")
def update_certificate(
    professional_id: UUID,
    certificate_id: UUID,
    request: CertificateRequest,
):
    certificate = Certificate(
        name=CertificateName(
            request.name
        ),
        issuer=Issuer(
            request.issuer
        ),
        credential_id=CredentialId(
            request.credential_id
        ),
        issued_date=request.issued_date,
        expiry_date=request.expiry_date,
        verification_url=request.verification_url,
        status=CertificateStatus(
            request.status
        ),
    )

    certificate.id = certificate_id

    professional = (
        container
        .update_certificate_use_case()
        .execute(
            professional_id,
            certificate,
        )
    )

    if professional is None:
        raise HTTPException(
            status_code=404,
            detail="Professional not found",
        )

    return CertificateMapper.to_response(
        certificate
    )