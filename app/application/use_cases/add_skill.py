from uuid import UUID

from app.domain.professional.professional import Professional
from app.domain.skill.skill import Skill
from app.exceptions.professional_not_found import ProfessionalNotFoundException


class AddSkill:
    """
    Original application use case used by unit tests.
    """

    def execute(
        self,
        professional: Professional,
        skill: Skill,
    ) -> None:
        professional.add_skill(skill)


class AddSkillUseCase:
    """
    Repository-backed use case used by the API.
    """

    def __init__(self, repository):
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
            raise ProfessionalNotFoundException()

        professional.add_skill(skill)

        self._repository.save(professional)

        return professional