"""
Remove Goal Use Case.
"""

from uuid import UUID

from app.domain.professional.professional import Professional

from app.domain.repositories.professional_repository import (
    ProfessionalRepository,
)

from app.exceptions.professional_not_found import (
    ProfessionalNotFoundException,
)



class RemoveGoal:
    """
    Legacy use case.

    Works directly with Professional aggregate.
    """

    def execute(
        self,
        professional: Professional,
        goal_id: UUID,
    ) -> None:

        professional.remove_goal(
            goal_id
        )



class RemoveGoalUseCase:
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
        goal_id: UUID,
    ):


        professional = (
            self._repository.get_by_id(
                professional_id
            )
        )


        if professional is None:
            raise ProfessionalNotFoundException(
                professional_id
            )


        professional.remove_goal(
            goal_id
        )


        self._repository.save(
            professional
        )


        return professional