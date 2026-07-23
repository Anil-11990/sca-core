"""
Remove Timeline Event Use Case.
"""

from uuid import UUID

from app.infrastructure.repositories.sqlite_professional_repository import (
    SQLiteProfessionalRepository,
)


class RemoveTimelineEventUseCase:
    """
    Removes a timeline event.
    """

    def __init__(
        self,
        repository: SQLiteProfessionalRepository,
    ):
        self.repository = repository


    def execute(
        self,
        professional_id: UUID,
        event_id: UUID,
    ):

        professional = (
            self.repository.get_by_id(
                professional_id
            )
        )

        if professional is None:
            return None


        professional.remove_timeline_event(
            event_id
        )

        self.repository.save(
            professional
        )

        return professional