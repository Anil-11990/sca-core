"""
Get Goals Use Case.
"""

from uuid import UUID

from app.domain.goal.goal import Goal
from app.domain.professional.professional import Professional

from app.exceptions.professional_not_found import (
    ProfessionalNotFoundException,
)


class GetGoals:
    """
    Legacy use case used by unit tests.
    """

    def execute(
        self,
        professional: Professional,
    ) -> list[Goal]:

        return professional.goals



class GetGoalsUseCase:
    """
    Repository-backed use case used by API.
    """

    def __init__(
        self,
        repository,
    ):
        self._repository = repository


    def execute(
        self,
        professional_id: UUID,
    ) -> list[Goal]:

        professional = self._repository.get_by_id(
            professional_id
        )

        if professional is None:
            raise ProfessionalNotFoundException()


        return list(
            professional.goals
        )