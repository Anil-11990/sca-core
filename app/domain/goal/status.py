"""
GoalStatus Enumeration.

Represents the lifecycle of a professional goal.
"""

from enum import Enum


class GoalStatus(Enum):
    """
    Valid states for a Goal.

    A Goal always starts as NOT_STARTED,
    moves to IN_PROGRESS,
    and finally reaches COMPLETED.
    """

    NOT_STARTED = "NOT_STARTED"
    IN_PROGRESS = "IN_PROGRESS"
    COMPLETED = "COMPLETED"