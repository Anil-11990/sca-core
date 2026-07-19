"""
Application Use Case:
Add Certificate
"""

from uuid import UUID

from app.domain.certificate.certificate import Certificate
from app.domain.professional.professional import Professional
from app.domain.professional.repository import ProfessionalRepository


class AddCertificate:
    """
    Adds a Certificate to an existing Professional.
    """

    def __init__(
        self,
        repository: ProfessionalRepository,
    ) -> None:
        self._repository = repository

    def execute(
        self,
        professional_id: UUID,
        certificate: Certificate,
    ) -> Professional | None:
        """
        Add a certificate to a Professional.
        """

        professional = self._repository.get_by_id(
            professional_id
        )

        if professional is None:
            return None

        professional.add_certificate(
            certificate
        )

        self._repository.save(
            professional
        )

        return professional