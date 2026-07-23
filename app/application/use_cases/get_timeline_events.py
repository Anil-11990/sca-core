"""
Get Timeline Events Use Case.
"""

from uuid import UUID

from app.infrastructure.repositories.sqlite_professional_repository import (
    SQLiteProfessionalRepository,
)


class GetTimelineEventsUseCase:
    """
    Retrieves Professional timeline events.
    """

    def __init__(
        self,
        repository: SQLiteProfessionalRepository,
    ):
        self.repository = repository


    def execute(
        self,
        professional_id: UUID,
    ):

        professional = (
            self.repository.get_by_id(
                professional_id
            )
        )

        if professional is None:
            return []


        return professional.timeline