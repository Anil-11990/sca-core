"""
Application Use Case:
Get Certificates
"""

from uuid import UUID

from app.domain.certificate.certificate import Certificate
from app.domain.professional.repository import (
    ProfessionalRepository,
)


class GetCertificates:
    """
    Retrieves every Certificate
    belonging to a Professional.
    """

    def __init__(
        self,
        repository: ProfessionalRepository,
    ) -> None:
        self._repository = repository

    def execute(
        self,
        professional_id: UUID,
    ) -> list[Certificate]:
        """
        Retrieve certificates for a Professional.
        """

        professional = self._repository.get_by_id(
            professional_id
        )

        if professional is None:
            return []

        return list(
            professional.certificates
        )