"""
Timeline Event Title Value Object.
"""

from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class EventTitle:
    """
    Represents the title of a timeline event.
    """

    value: str

    def __post_init__(self):

        value = self.value.strip()

        if not value:
            raise ValueError(
                "Event title cannot be empty."
            )

        if len(value) > 150:
            raise ValueError(
                "Event title cannot exceed 150 characters."
            )

        object.__setattr__(
            self,
            "value",
            value,
        )

    def __str__(self):

        return self.value