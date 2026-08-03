"""
Update Skill Use Case.
"""

from uuid import UUID

from app.domain.skill.skill import Skill

from app.domain.repositories.professional_repository import (
    ProfessionalRepository,
)


class UpdateSkill:
    """
    Updates an existing Skill.
    """

    def __init__(
        self,
        repository: ProfessionalRepository,
    ):
        self._repository = repository

    def execute(
        self,
        professional_id: UUID,
        skill: Skill,
    ):

        professional = self._repository.get_by_id(
            professional_id
        )

        if professional is None:
            return None

        professional.remove_skill(
            skill.id
        )

        professional.add_skill(
            skill
        )

        self._repository.save(
            professional
        )

        return professional