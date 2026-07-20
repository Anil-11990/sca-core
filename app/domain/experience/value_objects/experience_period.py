"""
Experience Period Value Object.
"""

from dataclasses import dataclass
from datetime import date


@dataclass(frozen=True)
class ExperiencePeriod:
    """
    Represents a period of employment.
    """

    start_date: date
    end_date: date | None = None

    def __post_init__(self):
        """
        Validate the employment period.
        """

        if self.end_date is not None:

            if self.end_date < self.start_date:

                raise ValueError(
                    "End date cannot be before start date."
                )

    @property
    def is_current(self) -> bool:
        """
        Returns True if this employment
        is still ongoing.
        """

        return self.end_date is None