"""
Achievement Title Value Object.
"""

from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class AchievementTitle:
    """
    Represents the title of an achievement.
    """

    value: str

    def __post_init__(self) -> None:
        value = self.value.strip()

        if not value:
            raise ValueError(
                "Achievement title cannot be empty."
            )

        object.__setattr__(self, "value", value)

    def __str__(self) -> str:
        return self.value