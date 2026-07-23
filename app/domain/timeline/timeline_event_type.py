from enum import Enum


class TimelineEventType(Enum):
    """
    Represents every event that can appear
    in a Professional's career timeline.
    """

    EDUCATION_STARTED = "Education Started"
    EDUCATION_COMPLETED = "Education Completed"

    EXPERIENCE_STARTED = "Experience Started"
    EXPERIENCE_COMPLETED = "Experience Completed"

    PROJECT_CREATED = "Project Created"

    CERTIFICATE_EARNED = "Certificate Earned"

    ACHIEVEMENT_UNLOCKED = "Achievement Unlocked"

    GOAL_CREATED = "Goal Created"
    GOAL_COMPLETED = "Goal Completed"