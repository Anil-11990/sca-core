"""
Certificate Entity.

Represents a verifiable professional
credential owned by a Professional.

A certificate is career evidence
inside the SCA Professional Identity.
"""

from dataclasses import dataclass, field
from datetime import date
from uuid import UUID, uuid4

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


@dataclass(eq=False)
class Certificate:
    """
    Certificate domain entity.
    """

    name: CertificateName

    issuer: Issuer

    credential_id: CredentialId

    issued_date: date

    expiry_date: date | None = None

    verification_url: str = ""

    status: CertificateStatus = CertificateStatus.ACTIVE

    id: UUID = field(
        default_factory=uuid4,
        init=False,
    )

    def __post_init__(self) -> None:
        """
        Validate certificate rules.
        """

        if (
            self.expiry_date is not None
            and self.expiry_date < self.issued_date
        ):
            raise ValueError(
                "Expiry date cannot be before issue date."
            )

    def is_expired(
        self,
        current_date: date,
    ) -> bool:
        """
        Returns True if the certificate
        has expired.
        """

        if self.expiry_date is None:
            return False

        return current_date > self.expiry_date