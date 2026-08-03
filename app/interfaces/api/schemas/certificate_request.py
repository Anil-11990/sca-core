"""
Certificate Request DTO.
"""

from datetime import date

from pydantic import BaseModel


class CertificateRequest(BaseModel):
    """
    Incoming Certificate payload.
    """

    name: str
    issuer: str
    credential_id: str
    issued_date: date
    expiry_date: date | None = None
    verification_url: str = ""
    status: str