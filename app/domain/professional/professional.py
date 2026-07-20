"""
Professional Aggregate Root.

This module defines the Professional entity, which is the heart of the
SCA (Sovereign Career Architect) domain model.

Every change to a professional's career profile should be performed
through this aggregate to ensure business rules remain consistent.
"""

from __future__ import annotations
from app.domain.certificate.certificate import Certificate
from dataclasses import dataclass, field
from datetime import UTC, datetime

from app.domain.common.entity import Entity
from app.domain.common.value_objects.full_name import FullName
from app.domain.goal.goal import Goal
from app.domain.skill.skill import Skill
from app.domain.project.project import Project
from app.domain.achievement.achievement import Achievement
from app.domain.experience.experience import (
    Experience,
)
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

    experiences: list[Experience] = field(
        default_factory=list
    )

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
    # Internal list of achievements.
    # Always modify using add_achievement().
    _achievements: list[Achievement] = field(
        default_factory=list,
        init=False,
        repr=False,
    )
    # Internal list of certificates.
    # Always modify using add_certificate().
    _certificates: list[Certificate] = field(
        default_factory=list,
        init=False,
        repr=False,
    )
    projects: list[Project] = field(
        default_factory=list
    )
    # ==========================================================
    # Read-only Properties
    # ==========================================================

    @property
    def certificates(self) -> tuple[Certificate, ...]:
        """
        Returns every certificate owned by the professional.
        """

        return tuple(self._certificates)

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

    @property
    def achievements(self) -> tuple[Achievement, ...]:
        """
        Returns a read-only collection of achievements.
        """

        return tuple(self._achievements)

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

    def add_certificate(
            self,
            certificate: Certificate,
    ) -> None:
        """
        Adds a certificate.

        Duplicate certificates are ignored.
        """

        if certificate in self._certificates:
            return

        self._certificates.append(
            certificate
        )

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

    def add_achievement(
            self,
            achievement: Achievement,
    ) -> None:
        """
        Adds an achievement.

        Duplicate achievements are ignored.
        """

        if achievement in self._achievements:
            return

        self._achievements.append(
            achievement
        )

    def add_experience(
            self,
            experience: Experience,
    ):
        """
        Add an Experience.
        """

        if experience in self.experiences:
            raise ValueError(
                "Experience already exists."
            )

        self.experiences.append(
            experience
        )

    def remove_experience(
            self,
            experience_id,
    ):
        """
        Remove an Experience.
        """

        self.experiences = [

            experience

            for experience in self.experiences

            if experience.id != experience_id
        ]

    def get_experience(
            self,
            experience_id,
    ):
        """
        Retrieve an Experience.
        """

        for experience in self.experiences:

            if experience.id == experience_id:
                return experience

        return None

    def add_project(
            self,
            project: Project,
    ) -> None:
        """
        Add a project.
        """

        self.projects.append(
            project
        )

    def remove_project(
            self,
            project_id,
    ) -> None:
        """
        Remove a project.
        """

        self.projects = [
            project
            for project in self.projects
            if project.id != project_id
        ]