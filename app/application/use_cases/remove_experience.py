"""
Remove Experience Use Case.
"""

from uuid import UUID

from app.domain.repositories.professional_repository import (
    ProfessionalRepository,
)


class RemoveExperience:

    def __init__(
        self,
        repository: ProfessionalRepository,
    ):
        self._repository = repository

    def execute(
        self,
        professional_id: UUID,
        experience_id: UUID,
    ):
        professional = self._repository.get_by_id(
            professional_id
        )

        if professional is None:
            return None

        professional.remove_experience(
            experience_id
        )

        self._repository.save(
            professional
        )

        return professional