"""
Experience Period Value Object.
"""

from dataclasses import dataclass
from datetime import date


@dataclass(frozen=True, slots=True)
class ExperiencePeriod:
    """
    Represents the period during which
    a professional held an experience.
    """

    start_date: date
    end_date: date | None = None

    def __post_init__(self) -> None:
        if (
            self.end_date is not None
            and self.end_date < self.start_date
        ):
            raise ValueError(
                "End date cannot be before start date."
            )