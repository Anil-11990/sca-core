"""
Response DTO for Certificate.
"""

from dataclasses import dataclass
from datetime import datetime


@dataclass(slots=True, frozen=True)
class CertificateResponse:

    id: str

    name: str

    issuer: str

    status: str

    credential_id: str

    credential_url: str

    issued_at: datetime