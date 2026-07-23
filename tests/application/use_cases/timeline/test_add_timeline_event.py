"""
Tests for Add Timeline Event Use Case.
"""

from datetime import date

from app.domain.common.value_objects.full_name import FullName
from app.domain.professional.professional import Professional

from app.domain.timeline.timeline_event import TimelineEvent
from app.domain.timeline.timeline_event_type import TimelineEventType

from app.application.use_cases.add_timeline_event import (
    AddTimelineEventUseCase,
)

from app.infrastructure.repositories.memory_professional_repository import (
    MemoryProfessionalRepository,
)



def test_add_timeline_event():

    repository = MemoryProfessionalRepository()


    professional = Professional(
        full_name=FullName(
            "Anil Khanal"
        ),
        primary_goal="Build ANIrex AI",
    )


    repository.save(
        professional
    )


    event = TimelineEvent(

        title="Started University",

        event_type=(
            TimelineEventType
            .EDUCATION_STARTED
        ),

        event_date=date(
            2022,
            9,
            1,
        ),

        description=(
            "Started BSc Computer Science"
        ),
    )


    use_case = AddTimelineEventUseCase(
        repository
    )


    result = use_case.execute(
        professional.id,
        event,
    )


    assert result is not None

    assert len(
        result.timeline
    ) == 1

    assert (
        result.timeline[0]
        == event
    )