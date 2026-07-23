"""
Tests for Remove Timeline Event Use Case.
"""

from datetime import date

from app.domain.common.value_objects.full_name import FullName
from app.domain.professional.professional import Professional
from app.domain.timeline.timeline_event import TimelineEvent
from app.domain.timeline.timeline_event_type import TimelineEventType

from app.application.use_cases.remove_timeline_event import (
    RemoveTimelineEventUseCase,
)

from app.infrastructure.repositories.memory_professional_repository import (
    MemoryProfessionalRepository,
)


def test_remove_timeline_event():

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

    use_case = RemoveTimelineEventUseCase(repository)

    use_case.execute(
        professional.id,
        event.id,
    )

    updated = repository.get_by_id(professional.id)

    assert len(updated.timeline) == 0