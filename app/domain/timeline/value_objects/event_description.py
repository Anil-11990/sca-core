"""
Timeline Event Description Value Object.
"""

from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class EventDescription:

    value: str

    def __post_init__(self):

        value = self.value.strip()

        if len(value) > 1000:

            raise ValueError(
                "Event description cannot exceed 1000 characters."
            )

        object.__setattr__(
            self,
            "value",
            value,
        )

    def __str__(self):

        return self.value