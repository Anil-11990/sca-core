"""
Goal Entity.

Represents a measurable professional objective.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime, UTC

from app.domain.common.entity import Entity
from app.domain.goal.status import GoalStatus
from app.domain.goal.value_objects.goal_title import GoalTitle


@dataclass(eq=False, slots=True)
class Goal(Entity):
    """
    Represents a professional goal.

    A Goal has identity and changes over time.
    """

    title: GoalTitle

    status: GoalStatus = GoalStatus.NOT_STARTED

    progress: int = 0

    created_at: datetime = field(
        default_factory=lambda: datetime.now(UTC)
    )

    def update_progress(self, value: int) -> None:
        """
        Updates the goal progress.

        Business Rules
        --------------
        - Progress must be between 0 and 100.
        - Reaching 100% automatically completes the goal.
        """

        if value < 0 or value > 100:
            raise ValueError(
                "Progress must be between 0 and 100."
            )

        self.progress = value

        if value == 100:
            self.status = GoalStatus.COMPLETED
        elif value > 0:
            self.status = GoalStatus.IN_PROGRESS