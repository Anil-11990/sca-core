"""
Education Period Value Object.

Represents the duration of an education record.

Example:

    Start:
        2022-09-01

    End:
        2026-06-30

Business Rules:
    - End date cannot be before start date.
    - Dates are stored as immutable values.
"""

from dataclasses import dataclass
from datetime import date


@dataclass(frozen=True, slots=True)
class EducationPeriod:
    """
    Represents a period of study.
    """

    start_date: date
    end_date: date | None = None

    def __post_init__(self) -> None:
        """
        Validate education timeline.
        """

        if (
            self.end_date is not None
            and self.end_date < self.start_date
        ):
            raise ValueError(
                "Education end date cannot be before start date."
            )

    @property
    def is_completed(self) -> bool:
        """
        Determines whether education has finished.

        Returns:
            True if an end date exists.
        """

        return self.end_date is not None