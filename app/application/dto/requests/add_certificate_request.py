"""
Request DTO for adding Certificate.
"""

from dataclasses import dataclass
from datetime import datetime


@dataclass(slots=True, frozen=True)
class AddCertificateRequest:

    professional_id: str

    name: str

    issuer: str

    status: str

    credential_id: str

    credential_url: str

    issued_at: datetime