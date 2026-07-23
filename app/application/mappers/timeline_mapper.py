from app.domain.timeline.timeline_event import (
    TimelineEvent,
)

from app.application.dto.responses.timeline_event_response import (
    TimelineEventResponse,
)


class TimelineEventMapper:
    """
    Maps TimelineEvent entity to DTO.
    """

    @staticmethod
    def to_response(
        event: TimelineEvent,
    ) -> TimelineEventResponse:

        return TimelineEventResponse(
            id=str(event.id),
            title=str(event.title),
            event_type=(
                event.event_type.value
            ),
            event_date=(
                event.event_date.value
            ),
            description=str(
                event.description
            ),
            reference_id=(
                event.reference_id
            ),
        )