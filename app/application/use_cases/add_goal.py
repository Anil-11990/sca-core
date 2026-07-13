"""
Application Use Case:
Add Goal
"""

from app.domain.goal.goal import Goal
from app.domain.professional.professional import Professional


class AddGoal:
    """
    Application use case for adding a goal
    to a Professional.
    """

    def execute(
        self,
        professional: Professional,
        goal: Goal,
    ) -> None:
        """
        Purpose:
            Adds a goal to a Professional.

        Business Rule:
            Delegates the operation to the
            Professional Aggregate Root.

        Future:
            Repository persistence,
            domain events,
            audit logging,
            notifications.
        """

        professional.add_goal(goal)