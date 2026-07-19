"""
Issuer Value Object.
"""

from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class Issuer:
    """
    Represents the organisation issuing an achievement.
    """

    value: str

    def __post_init__(self) -> None:
        value = self.value.strip()

        if not value:
            raise ValueError(
                "Issuer cannot be empty."
            )

        object.__setattr__(self, "value", value)

    def __str__(self) -> str:
        return self.value