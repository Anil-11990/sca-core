from uuid import UUID

from app.exceptions.professional_not_found import (
    ProfessionalNotFoundException,
)


class DeleteProfessional:
    """
    Delete a Professional.
    """

    def __init__(
        self,
        repository,
    ):
        self._repository = repository

    def execute(
        self,
        professional_id: UUID,
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

        self._repository.delete(
            professional_id
        )