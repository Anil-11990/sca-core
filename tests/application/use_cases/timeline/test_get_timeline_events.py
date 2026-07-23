"""
Tests for Get Timeline Events Use Case.
"""

from datetime import date

from app.domain.common.value_objects.full_name import FullName
from app.domain.professional.professional import Professional
from app.domain.timeline.timeline_event import TimelineEvent
from app.domain.timeline.timeline_event_type import TimelineEventType

from app.application.use_cases.get_timeline_events import (
    GetTimelineEventsUseCase,
)

from app.infrastructure.repositories.memory_professional_repository import (
    MemoryProfessionalRepository,
)


def test_get_timeline_events():

    repository = MemoryProfessionalRepository()

    professional = Professional(
        full_name=FullName("Anil Khanal"),
        primary_goal="Build ANIrex AI",
    )

    event = TimelineEvent(
        title="Started University",
        event_type=TimelineEventType.EDUCATION_STARTED,
        event_date=date(2022, 9, 1),
        description="BSc Computer Science",
    )

    professional.add_timeline_event(event)

    repository.save(professional)

    use_case = GetTimelineEventsUseCase(repository)

    events = use_case.execute(professional.id)

    assert len(events) == 1
    assert events[0] == event