"""
Response DTO for Certificate.
"""

from dataclasses import dataclass
from datetime import date


@dataclass(slots=True, frozen=True)
class CertificateResponse:
    """
    Immutable response DTO for Certificate.
    """

    id: str

    name: str

    issuer: str

    credential_id: str

    status: str

    verification_url: str

    issued_date: date

    expiry_date: date | None