from dataclasses import dataclass

from app.domain.events.domain_event import DomainEvent
from app.domain.goal.goal import Goal


@dataclass(frozen=True, slots=True)
class GoalCompleted(DomainEvent):
    """
    Raised when a goal reaches 100% completion.
    """

    goal: Goal