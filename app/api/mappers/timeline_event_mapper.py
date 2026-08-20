"""
Timeline Event API Mapper.

Responsibilities
----------------
- Convert TimelineEvent domain objects
  into API response objects.
"""

from app.domain.timeline.timeline_event import (
    TimelineEvent,
)

from app.api.schemas.timeline_event_response import (
    TimelineEventResponse,
)


class TimelineEventMapper:
    """
    Maps TimelineEvent domain objects
    to API response schemas.
    """

    @staticmethod
    def to_response(
        event: TimelineEvent,
    ) -> TimelineEventResponse:
        """
        Convert domain TimelineEvent
        into API response.
        """

        return TimelineEventResponse(
            id=str(event.id),
            title=str(event.title),
            event_type=event.event_type.value,
            event_date=event.event_date.value,
            description=str(event.description),
            reference_id=event.reference_id,
        )