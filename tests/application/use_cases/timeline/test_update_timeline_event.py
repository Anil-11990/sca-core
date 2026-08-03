"""
Test Update Timeline Event Use Case.
"""

from datetime import date

from app.application.use_cases.update_timeline_event import (
    UpdateTimelineEvent,
)

from app.domain.professional.professional import (
    Professional,
)

from app.domain.common.value_objects.full_name import (
    FullName,
)

from app.infrastructure.repositories.memory_professional_repository import (
    MemoryProfessionalRepository,
)
from app.domain.timeline.timeline_event import (
    TimelineEvent,
)

from app.domain.timeline.timeline_event_type import (
    TimelineEventType,
)


def test_update_timeline_event():

    # ---------------------------------
    # Arrange
    # Create repository
    # ---------------------------------

    repo = MemoryProfessionalRepository()


    # ---------------------------------
    # Create professional
    # ---------------------------------

    professional = Professional(
        full_name=FullName(
            "Anil Khanal"
        ),
        primary_goal="Build ANIrex AI",
    )

    # ---------------------------------
    # Existing timeline event
    # ---------------------------------

    old_event = TimelineEvent(
        title="Started Computer Science Degree",
        event_type=TimelineEventType.EDUCATION_STARTED,
        event_date=date(2022, 1, 1),
        description="Started BSc Computer Science",
    )

    professional.add_timeline_event(
        old_event
    )

    repo.save(
        professional
    )

    # ---------------------------------
    # Updated timeline event
    # Keep same ID because update
    # replaces existing entity
    # ---------------------------------

    updated_event = TimelineEvent(
        title="Completed Computer Science Degree",
        event_type=TimelineEventType.EDUCATION_COMPLETED,
        event_date=date(2026, 1, 1),
        description="Completed BSc Computer Science",
    )

    updated_event.id = old_event.id

    # ---------------------------------
    # Execute
    # ---------------------------------

    use_case = UpdateTimelineEvent(
        repo
    )


    updated = use_case.execute(
        professional.id,
        updated_event,
    )


    # ---------------------------------
    # Assert
    # ---------------------------------

    assert updated is not None

    assert len(
        updated.timeline
    ) == 1


    assert updated.timeline[0].title.value == (
        "Completed Computer Science Degree"
    )

    assert updated.timeline[0].description.value == (
        "Completed BSc Computer Science"
    )