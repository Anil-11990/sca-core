"""
Certificate Response DTO.
"""

from datetime import datetime

from pydantic import BaseModel


class CertificateResponse(BaseModel):
    """
    Returned Certificate.
    """

    id: str
    name: str
    issuer: str
    credential_id: str
    credential_url: str
    status: str
    issued_at: datetime