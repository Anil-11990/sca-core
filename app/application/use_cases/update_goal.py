"""
Update Goal Use Case.
"""

from uuid import UUID

from app.domain.goal.goal import Goal
from app.domain.professional.professional import Professional

from app.domain.repositories.professional_repository import (
    ProfessionalRepository,
)


class UpdateGoal:
    """
    Legacy use case.

    Used when a Professional object
    is already available.
    """

    def execute(
        self,
        professional: Professional,
        goal: Goal,
    ) -> None:

        professional.remove_goal(
            goal.id
        )

        professional.add_goal(
            goal
        )



class UpdateGoalUseCase:
    """
    Repository-backed use case used by API.
    """

    def __init__(
        self,
        repository: ProfessionalRepository,
    ):
        self._repository = repository


    def execute(
        self,
        professional_id: UUID,
        goal: Goal,
    ):

        professional = (
            self._repository.get_by_id(
                professional_id
            )
        )


        if professional is None:
            return None


        professional.remove_goal(
            goal.id
        )


        professional.add_goal(
            goal
        )


        self._repository.save(
            professional
        )


        return professional