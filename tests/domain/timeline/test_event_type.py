from app.domain.timeline.timeline_event_type import TimelineEventType


def test_event_type_values():

    assert (
        TimelineEventType.EDUCATION_STARTED.value
        == "Education Started"
    )

    assert (
        TimelineEventType.EDUCATION_COMPLETED.value
        == "Education Completed"
    )

    assert (
        TimelineEventType.EXPERIENCE_STARTED.value
        == "Experience Started"
    )

    assert (
        TimelineEventType.EXPERIENCE_COMPLETED.value
        == "Experience Completed"
    )

    assert (
        TimelineEventType.PROJECT_CREATED.value
        == "Project Created"
    )

    assert (
        TimelineEventType.CERTIFICATE_EARNED.value
        == "Certificate Earned"
    )

    assert (
        TimelineEventType.ACHIEVEMENT_UNLOCKED.value
        == "Achievement Unlocked"
    )

    assert (
        TimelineEventType.GOAL_CREATED.value
        == "Goal Created"
    )

    assert (
        TimelineEventType.GOAL_COMPLETED.value
        == "Goal Completed"
    )