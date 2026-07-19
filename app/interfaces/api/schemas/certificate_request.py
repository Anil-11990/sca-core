"""
Certificate Request DTO.
"""

from pydantic import BaseModel


class CertificateRequest(BaseModel):
    """
    Incoming Certificate payload.
    """

    name: str
    issuer: str
    credential_id: str
    credential_url: str
    status: str