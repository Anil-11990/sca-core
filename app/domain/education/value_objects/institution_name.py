"""
Institution Name Value Object.

Represents the educational organisation
where a professional studied.

Examples:
    - University of West London
    - Stanford University
    - MIT

This keeps institution validation inside
the domain instead of spreading rules everywhere.
"""

from dataclasses import dataclass


@dataclass(frozen=True)
class InstitutionName:

    value: str

    def __str__(self) -> str:
        return self.value

    def __eq__(self, other) -> bool:
        if isinstance(other, InstitutionName):
            return self.value == other.value

        if isinstance(other, str):
            return self.value == other

        return False

    def __post_init__(self) -> None:
        """
        Validate and clean institution name.
        """

        cleaned_value = self.value.strip()

        if not cleaned_value:
            raise ValueError(
                "Institution name cannot be empty."
            )

        object.__setattr__(
            self,
            "value",
            cleaned_value,
        )

    def __str__(self) -> str:
        """
        Returns readable institution name.
        """

        return self.value