"""
Add Timeline Event Use Case.
"""

from uuid import UUID

from app.domain.timeline.timeline_event import TimelineEvent
from app.infrastructure.repositories.sqlite_professional_repository import (
    SQLiteProfessionalRepository,
)


class AddTimelineEventUseCase:
    """
    Adds a timeline event to a Professional.
    """

    def __init__(
        self,
        repository: SQLiteProfessionalRepository,
    ):
        self.repository = repository


    def execute(
        self,
        professional_id: UUID,
        event: TimelineEvent,
    ):

        professional = (
            self.repository.get_by_id(
                professional_id
            )
        )

        if professional is None:
            return None


        professional.add_timeline_event(
            event
        )

        self.repository.save(
            professional
        )

        return professional