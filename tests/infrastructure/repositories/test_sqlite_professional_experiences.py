from datetime import date

from app.domain.common.value_objects.full_name import FullName
from app.domain.professional.professional import Professional
from app.domain.timeline.timeline_event import TimelineEvent
from app.domain.timeline.timeline_event_type import TimelineEventType


def test_add_timeline_event():

    professional = Professional(
        full_name=FullName("Anil Khanal"),
        primary_goal="Build ANIrex AI",
    )

    event = TimelineEvent(
        event_type=TimelineEventType.EDUCATION_STARTED,
        title="Started University",
        description="BSc Computer Science",
        event_date=date(2022, 9, 1),
    )

    professional.add_timeline_event(event)

    assert len(professional.timeline) == 1
    assert professional.timeline[0] == event


def test_duplicate_timeline_event_is_ignored():

    professional = Professional(
        full_name=FullName("Anil Khanal"),
        primary_goal="Build ANIrex AI",
    )

    event = TimelineEvent(
        event_type=TimelineEventType.EDUCATION_STARTED,
        title="Started University",
        description="BSc Computer Science",
        event_date=date(2022, 9, 1),
    )

    professional.add_timeline_event(event)
    professional.add_timeline_event(event)

    assert len(professional.timeline) == 1


def test_remove_timeline_event():

    professional = Professional(
        full_name=FullName("Anil Khanal"),
        primary_goal="Build ANIrex AI",
    )

    event = TimelineEvent(
        event_type=TimelineEventType.EDUCATION_STARTED,
        title="Started University",
        description="BSc Computer Science",
        event_date=date(2022, 9, 1),
    )

    professional.add_timeline_event(event)

    professional.remove_timeline_event(event.id)

    assert len(professional.timeline) == 0


def test_get_timeline_event():

    professional = Professional(
        full_name=FullName("Anil Khanal"),
        primary_goal="Build ANIrex AI",
    )

    event = TimelineEvent(
        event_type=TimelineEventType.EDUCATION_STARTED,
        title="Started University",
        description="BSc Computer Science",
        event_date=date(2022, 9, 1),
    )

    professional.add_timeline_event(event)

    found = professional.get_timeline_event(event.id)

    assert found == event


def test_get_unknown_timeline_event_returns_none():

    professional = Professional(
        full_name=FullName("Anil Khanal"),
        primary_goal="Build ANIrex AI",
    )

    assert professional.get_timeline_event("unknown") is None