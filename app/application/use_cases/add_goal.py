"""
Add Goal Use Case.
"""

from uuid import UUID

from app.domain.goal.goal import Goal
from app.domain.professional.professional import Professional

from app.exceptions.professional_not_found import (
    ProfessionalNotFoundException,
)


class AddGoal:
    """
    Legacy use case used by unit tests.
    """

    def execute(
        self,
        professional: Professional,
        goal: Goal,
    ) -> None:

        professional.add_goal(goal)


class AddGoalUseCase:
    """
    Repository-backed use case used by the API.
    """

    def __init__(self, repository):
        self._repository = repository

    def execute(
        self,
        professional_id: UUID,
        goal: Goal,
    ):

        professional = self._repository.get_by_id(
            professional_id
        )

        if professional is None:
            raise ProfessionalNotFoundException()

        professional.add_goal(
            goal
        )

        self._repository.save(
            professional
        )

        return professional