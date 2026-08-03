"""
Recommendation Domain Object.

Represents an actionable career recommendation.
"""

from dataclasses import dataclass
from uuid import UUID, uuid4


@dataclass(eq=False, slots=True)
class Recommendation:
    """
    Represents a recommended career action.
    """

    action: str
    reason: str
    priority: str

    id: UUID = uuid4()

    def __post_init__(self) -> None:

        self.action = self.action.strip()
        self.reason = self.reason.strip()
        self.priority = self.priority.strip()

        if not self.action:
            raise ValueError(
                "Recommendation action cannot be empty."
            )

        if not self.reason:
            raise ValueError(
                "Recommendation reason cannot be empty."
            )

        if not self.priority:
            raise ValueError(
                "Recommendation priority cannot be empty."
            )