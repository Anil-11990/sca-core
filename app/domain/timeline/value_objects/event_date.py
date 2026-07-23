"""
Timeline Event Date Value Object.
"""

from dataclasses import dataclass
from datetime import date


@dataclass(frozen=True, slots=True)
class EventDate:
    """
    Represents the date of a timeline event.
    """

    value: date

    def __post_init__(self):

        if self.value > date.today():

            raise ValueError(
                "Event date cannot be in the future."
            )

    def __str__(self):

        return self.value.isoformat()