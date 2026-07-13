from __future__ import annotations

from dataclasses import dataclass

from app.domain.common.entity import Entity


@dataclass(eq=False, slots=True)
class Skill(Entity):
    """
    Represents a professional skill.

    Every skill has a unique identity inherited from Entity.
    """

    name: str

    def __post_init__(self) -> None:
        self.name = self.name.strip()

        if not self.name:
            raise ValueError("Skill name cannot be empty.")