"""
Update Timeline Event Use Case.
"""

from uuid import UUID

from app.domain.timeline.timeline_event import (
    TimelineEvent,
)

from app.domain.repositories.professional_repository import (
    ProfessionalRepository,
)


class UpdateTimelineEvent:
    """
    Updates a timeline event.
    """

    def __init__(
        self,
        repository: ProfessionalRepository,
    ):
        self._repository = repository


    def execute(
        self,
        professional_id: UUID,
        event: TimelineEvent,
    ):

        professional = self._repository.get_by_id(
            professional_id
        )


        if professional is None:
            return None


        professional.remove_timeline_event(
            event.id
        )


        professional.add_timeline_event(
            event
        )


        self._repository.save(
            professional
        )


        return professional