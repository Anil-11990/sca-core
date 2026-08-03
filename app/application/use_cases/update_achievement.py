"""
Update Achievement Use Case.
"""

from uuid import UUID

from app.domain.achievement.achievement import Achievement

from app.domain.repositories.professional_repository import (
    ProfessionalRepository,
)


class UpdateAchievement:
    """
    Updates an existing Achievement.
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
        achievement: Achievement,
    ):

        professional = self._repository.get_by_id(
            professional_id
        )

        if professional is None:
            return None

        professional.remove_achievement(
            achievement_id
        )

        professional.add_achievement(
            achievement
        )

        self._repository.save(
            professional
        )

        return professional