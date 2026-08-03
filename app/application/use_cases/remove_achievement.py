"""
Remove Achievement Use Case.
"""

from uuid import UUID

from app.domain.repositories.professional_repository import (
    ProfessionalRepository,
)


class RemoveAchievement:
    """
    Removes an achievement from a Professional.
    """

    def __init__(
        self,
        repository: ProfessionalRepository,
    ):
        self._repository = repository


    def execute(
        self,
        professional_id: UUID,
        achievement_id: UUID,
    ):

        professional = self._repository.get_by_id(
            professional_id
        )


        if professional is None:
            return None


        professional.remove_achievement(
            achievement_id
        )


        self._repository.save(
            professional
        )


        return professional