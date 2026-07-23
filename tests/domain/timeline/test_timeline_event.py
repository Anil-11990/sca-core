from datetime import date

from app.domain.timeline.timeline_event import TimelineEvent
from app.domain.timeline.timeline_event_type import TimelineEventType


def test_create_timeline_event():

    event = TimelineEvent(
        title="Started University",
        event_type=TimelineEventType.EDUCATION_STARTED,
        event_date=date.today(),
        description="BSc Computer Science",
    )

    assert str(event.title) == "Started University"

    assert (
        event.event_type
        == TimelineEventType.EDUCATION_STARTED
    )

    assert (
        str(event.description)
        == "BSc Computer Science"
    )

    assert event.event_date.value == date.today()