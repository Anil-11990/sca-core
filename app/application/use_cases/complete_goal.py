"""
Application Use Case:
Complete Goal
"""

from app.domain.goal.goal import Goal


class CompleteGoal:
    """
    Marks a professional goal as completed.
    """

    def execute(
        self,
        goal: Goal,
    ) -> None:
        """
        Purpose:
            Completes a goal.

        Business Rule:
            The Goal entity decides what
            completion means.

        Future:
            - Publish GoalCompleted event
            - Update growth score
            - Trigger AI recommendations
            - Record analytics
        """

        goal.update_progress(100)