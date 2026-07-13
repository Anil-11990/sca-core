"""
Professional Aggregate Root.

This module defines the Professional entity, which is the heart of the
SCA (Sovereign Career Architect) domain model.

Every change to a professional's career profile should be performed
through this aggregate to ensure business rules remain consistent.
"""

from __future__ import annotations
from app.domain.common.value_objects.full_name import FullName
from dataclasses import dataclass, field
from datetime import datetime, UTC

from app.domain.common.entity import Entity
from app.domain.skill.skill import Skill


@dataclass(eq=False, slots=True)
class Professional(Entity):
    """
    Represents a professional within the SCA domain.

    The Professional is the Aggregate Root responsible for managing
    professional identity, goals, and capabilities.

    Version 1 intentionally contains only the minimum attributes
    required to establish a stable domain model.
    """

    full_name: FullName
    primary_goal: str

    # Optional information that can be filled in later.
    current_title: str = ""
    location: str = ""

    # A Professional owns many skills.
    skills: list[Skill] = field(default_factory=list)

    # Records when the Professional object was created.
    created_at: datetime = field(
        default_factory=lambda: datetime.now(UTC)
    )

    def __post_init__(self) -> None:
        """
        Normalise and validate the Professional immediately after creation.
        """

        self.primary_goal = self.primary_goal.strip()

        if not self.full_name:
            raise ValueError("Professional name cannot be empty.")

        if not self.primary_goal:
            raise ValueError("Primary goal cannot be empty.")