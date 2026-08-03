"""
Certificate Response DTO.
"""

from datetime import date

from pydantic import BaseModel


class CertificateResponse(BaseModel):
    """
    Returned Certificate.
    """

    id: str
    name: str
    issuer: str
    credential_id: str
    issued_date: date
    expiry_date: date | None
    verification_url: str
    status: str