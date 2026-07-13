from uuid import UUID

from app.domain.professional.professional import Professional
from app.domain.professional.repository import ProfessionalRepository


class GetProfessional:
    """
    Retrieves a Professional by ID.
    """

    def __init__(self, repository: ProfessionalRepository):
        self.repository = repository

    def execute(self, professional_id: UUID) -> Professional | None:
        """
        Retrieve a Professional using its UUID.

        The API layer is responsible for converting
        incoming strings into UUID objects.
        """
        return self.repository.get_by_id(professional_id)