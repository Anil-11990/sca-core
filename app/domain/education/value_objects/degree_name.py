"""
Degree Name Value Object.

This module represents the academic qualification name
inside the SCA education domain.

Examples:
    - Bachelor of Computer Science
    - Master of Artificial Intelligence
    - PhD Computer Science

A Value Object:
- Has no identity.
- Is immutable in meaning.
- Is compared by its value.
"""

from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class DegreeName:
    """
    Represents an academic degree title.

    Business Rules:
        - Degree name cannot be empty.
        - Leading/trailing spaces are removed.
        - Degree names are stored consistently.
    """

    value: str

    def __post_init__(self) -> None:
        """
        Validate and normalise degree name.
        """

        cleaned_value = self.value.strip()

        if not cleaned_value:
            raise ValueError(
                "Degree name cannot be empty."
            )

        object.__setattr__(
            self,
            "value",
            cleaned_value,
        )

    def __str__(self) -> str:
        """
        Returns the readable degree name.
        """

        return self.value