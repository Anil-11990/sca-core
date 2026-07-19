"""
Project Name Value Object.

Represents the validated name of a project.
"""

from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class ProjectName:
    """
    Immutable value object representing a project name.
    """

    value: str

    def __post_init__(self) -> None:
        cleaned = self.value.strip()

        if not cleaned:
            raise ValueError(
                "Project name cannot be empty."
            )

        object.__setattr__(self, "value", cleaned)

    def __str__(self) -> str:
        return self.value