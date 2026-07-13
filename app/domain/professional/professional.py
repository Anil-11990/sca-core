"""
Professional Aggregate Root.

This module defines the Professional entity, which is the heart of the
SCA (Sovereign Career Architect) domain model.

Every change to a professional's career profile should be performed
through this aggregate to ensure business rules remain consistent.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import UTC, datetime

from app.domain.common.entity import Entity
from app.domain.common.value_objects.full_name import FullName
from app.domain.goal.goal import Goal
from app.domain.skill.skill import Skill


@dataclass(eq=False, slots=True)
class Professional(Entity):
    """
    Represents a professional within the SCA domain.

    The Professional is the Aggregate Root responsible for managing
    professional identity, goals, and capabilities.
    """

    # ==========================================================
    # Required Fields
    # ==========================================================

    full_name: FullName
    primary_goal: str

    # ==========================================================
    # Optional Fields
    # ==========================================================

    current_title: str = ""
    location: str = ""

    # ==========================================================
    # Private Collections
    # ==========================================================

    # Internal list of skills.
    # Always modify using add_skill().
    _skills: list[Skill] = field(
        default_factory=list,
        init=False,
        repr=False
    )

    # Internal list of goals.
    # Always modify using add_goal().
    _goals: list[Goal] = field(
        default_factory=list,
        init=False,
        repr=False
    )

    # ==========================================================
    # Metadata
    # ==========================================================

    created_at: datetime = field(
        default_factory=lambda: datetime.now(UTC)
    )

    # ==========================================================
    # Read-only Properties
    # ==========================================================

    @property
    def skills(self) -> tuple[Skill, ...]:
        """
        Purpose:
            Returns a read-only collection of skills.

        Business Rule:
            Outside code cannot directly modify
            the Professional's internal skills list.
        """
        return tuple(self._skills)

    @property
    def goals(self) -> tuple[Goal, ...]:
        """
        Purpose:
            Returns a read-only collection of goals.

        Business Rule:
            Outside code cannot directly modify
            the Professional's internal goals list.
        """
        return tuple(self._goals)

    # ==========================================================
    # Business Methods
    # ==========================================================

    def add_skill(self, skill: Skill) -> None:
        """
        Purpose:
            Adds a skill to the Professional.

        Business Rule:
            Duplicate skills are ignored.

        Future Extension:
            Skill proficiency and acquisition
            dates may be handled here.
        """

        if skill in self._skills:
            return

        self._skills.append(skill)

    def add_goal(self, goal: Goal) -> None:
        """
        Purpose:
            Adds a goal to the Professional.

        Business Rule:
            Duplicate goals are ignored.

        Future Extension:
            Goal priorities, dependencies and
            scheduling logic may be added here.
        """

        if goal in self._goals:
            return

        self._goals.append(goal)

    # ==========================================================
    # Validation
    # ==========================================================

    def __post_init__(self) -> None:
        """
        Normalises and validates the Professional
        immediately after creation.
        """

        self.primary_goal = self.primary_goal.strip()

        if not self.full_name:
            raise ValueError(
                "Professional name cannot be empty."
            )

        if not self.primary_goal:
            raise ValueError(
                "Primary goal cannot be empty."
            )