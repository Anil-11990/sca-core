from uuid import UUID

from app.domain.common.value_objects.full_name import FullName
from app.exceptions.professional_not_found import (
    ProfessionalNotFoundException,
)


class UpdateProfessional:
    """
    Update an existing Professional.
    """

    def __init__(
        self,
        repository,
    ):
        self._repository = repository

    def execute(
        self,
        professional_id: UUID,
        full_name: str,
        primary_goal: str,
    ):
        professional = self._repository.get_by_id(
            professional_id
        )

        if professional is None:
            raise ProfessionalNotFoundException(
                professional_id
            )

        professional.full_name = FullName(
            full_name
        )

        professional.primary_goal = (
            primary_goal
        )

        self._repository.save(
            professional
        )

        return professional