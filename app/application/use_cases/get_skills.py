from uuid import UUID

from app.domain.professional.professional import Professional
from app.domain.skill.skill import Skill
from app.exceptions.professional_not_found import ProfessionalNotFoundException


class GetSkills:
    """
    Legacy unit-test use case.
    """

    def execute(
        self,
        professional: Professional,
    ) -> list[Skill]:
        return professional.skills


class GetSkillsUseCase:
    """
    API repository-based use case.
    """

    def __init__(self, repository):
        self._repository = repository

    def execute(
        self,
        professional_id: UUID,
    ):
        professional = self._repository.get_by_id(
            professional_id
        )

        if professional is None:
            raise ProfessionalNotFoundException()

        return professional.skills