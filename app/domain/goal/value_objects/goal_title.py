"""
GoalTitle Value Object.

Represents the title of a professional goal.

A GoalTitle is immutable and validates the business rules
for goal names before they enter the domain.
"""

from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class GoalTitle:
    """
    Represents a validated goal title.

    Business Rules
    --------------
    - Cannot be empty.
    - Leading/trailing whitespace is removed.
    - Maximum length is 200 characters.
    - Equality is based on value.
    """

    value: str

    def __post_init__(self) -> None:
        """
        Normalize and validate the goal title.
        """

        # Remove unnecessary whitespace.
        cleaned = self.value.strip()

        # Every goal must have a title.
        if not cleaned:
            raise ValueError("Goal title cannot be empty.")

        # Keep titles concise.
        if len(cleaned) > 200:
            raise ValueError("Goal title cannot exceed 200 characters.")

        # Because this object is immutable,
        # we update the value using object.__setattr__().
        object.__setattr__(self, "value", cleaned)