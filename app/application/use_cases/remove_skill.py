"""
Remove Skill Use Case.
"""

from uuid import UUID

from app.domain.professional.professional import Professional
from app.domain.skill.skill import Skill

from app.domain.repositories.professional_repository import (
    ProfessionalRepository,
)


class RemoveSkill:
    """
    Legacy unit-test use case.
    """

    def execute(
        self,
        professional: Professional,
        skill: Skill,
    ) -> None:

        professional.remove_skill(
            skill.id
        )


class RemoveSkillUseCase:
    """
    Repository-backed API use case.
    """

    def __init__(
        self,
        repository: ProfessionalRepository,
    ):
        self._repository = repository

    def execute(
        self,
        professional_id: UUID,
        skill_id: UUID,
    ):

        professional = self._repository.get_by_id(
            professional_id
        )

        if professional is None:
            return None

        professional.remove_skill(
            skill_id
        )

        self._repository.save(
            professional
        )

        return professional