"""
Experience Description Value Object.
"""

from dataclasses import dataclass


@dataclass(frozen=True)
class ExperienceDescription:
    """
    Represents an experience description.
    """

    value: str

    def __post_init__(self):

        if self.value is None:
            raise ValueError(
                "Description cannot be None."
            )

        if not self.value.strip():
            raise ValueError(
                "Description cannot be empty."
            )

        if len(self.value.strip()) > 1000:
            raise ValueError(
                "Description cannot exceed 1000 characters."
            )

    def __str__(self):
        return self.value