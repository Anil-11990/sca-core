"""
Get Projects Use Case.
"""

from uuid import UUID

from app.domain.professional.repository import (
    ProfessionalRepository,
)


class GetProjects:
    """
    Returns every Project belonging
    to a Professional.
    """

    def __init__(
        self,
        repository: ProfessionalRepository,
    ):
        self._repository = repository

    def execute(
        self,
        professional_id: UUID,
    ):

        professional = self._repository.get_by_id(
            professional_id
        )

        if professional is None:
            return []

        return professional.projects