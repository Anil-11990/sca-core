"""
FullName Value Object.

A Value Object represents a concept whose identity is defined
entirely by its value.

Two FullName objects are equal if their values are equal.

Example:
    FullName("Anil Khanal") == FullName("Anil Khanal")
"""

from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class FullName:
    """
    Represents a person's full name.

    Business Rules
    --------------
    - Name cannot be empty.
    - Leading/trailing whitespace is removed.
    - Equality is based on value.
    """

    value: str


    def __post_init__(self) -> None:
        """
        Normalize and validate the name.

        Since this dataclass is frozen (immutable),
        we use object.__setattr__() to update the value
        during initialization.
        """

        # Remove unnecessary spaces.
        cleaned = self.value.strip()

        # Business rule:
        # Every Professional must have a valid name.
        if not cleaned:
            raise ValueError("Full name cannot be empty.")

        # Because the dataclass is frozen, this is the
        # correct way to assign the normalized value.
        object.__setattr__(self, "value", cleaned)

    def __str__(self) -> str:
        """
        Returns the plain text representation
        of the person's full name.
        """
        return self.value