"""
Role Title Value Object.
"""

from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class RoleTitle:
    """
    Represents a professional role title.
    """

    value: str

    def __post_init__(self) -> None:
        value = self.value.strip()

        if not value:
            raise ValueError(
                "Role title cannot be empty."
            )

        object.__setattr__(self, "value", value)

    def __str__(self) -> str:
        return self.value