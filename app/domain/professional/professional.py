"""
Professional Aggregate Root.

This module defines the Professional entity, which is the heart of the
SCA (Sovereign Career Architect) domain model.

Every change to a professional's career profile should be performed
through this aggregate to ensure business rules remain consistent.
"""

from __future__ import annotations

# =============================================================================
# Standard Library
# =============================================================================

from dataclasses import dataclass, field
from datetime import UTC, datetime

# =============================================================================
# Domain
# =============================================================================

from app.domain.achievement.achievement import Achievement
from app.domain.certificate.certificate import Certificate
from app.domain.common.entity import Entity
from app.domain.common.value_objects.full_name import FullName
from app.domain.education.education import Education
from app.domain.experience.experience import Experience
from app.domain.goal.goal import Goal
from app.domain.project.project import Project
from app.domain.skill.skill import Skill
from app.domain.timeline.timeline_event import (
    TimelineEvent,
)


# =============================================================================
# Professional Aggregate Root
# =============================================================================

@dataclass(eq=False, slots=True)
class Professional(Entity):
    """
    Represents a Professional within the SCA domain.

    The Professional is the Aggregate Root responsible for managing
    professional identity, career progression, achievements,
    projects, education, skills and goals.
    """

    # =========================================================================
    # Required Fields
    # =========================================================================

    full_name: FullName
    primary_goal: str

    # =========================================================================
    # Optional Profile Information
    # =========================================================================

    current_title: str = ""
    location: str = ""

    # =========================================================================
    # Aggregate Collections
    # =========================================================================

    experiences: list[Experience] = field(
        default_factory=list
    )

    projects: list[Project] = field(
        default_factory=list
    )

    educations: list[Education] = field(
        default_factory=list
    )

    # =========================================================================
    # Internal Collections
    # =========================================================================

    # Always modify through add_skill()
    _skills: list[Skill] = field(
        default_factory=list,
        init=False,
        repr=False,
    )

    # Always modify through add_goal()
    _goals: list[Goal] = field(
        default_factory=list,
        init=False,
        repr=False,
    )

    # Always modify through add_achievement()
    _achievements: list[Achievement] = field(
        default_factory=list,
        init=False,
        repr=False,
    )

    # Always modify through add_certificate()
    _certificates: list[Certificate] = field(
        default_factory=list,
        init=False,
        repr=False,
    )
    timeline: list[TimelineEvent] = field(
        default_factory=list

    )

    # =========================================================================
    # Metadata
    # =========================================================================

    created_at: datetime = field(
        default_factory=lambda: datetime.now(UTC)
    )

    # =========================================================================
    # Read-only Properties
    # =========================================================================

    @property
    def skills(self) -> tuple[Skill, ...]:
        """
        Returns every skill owned by the Professional.

        External code cannot modify the internal collection.
        """

        return tuple(self._skills)

    @property
    def goals(self) -> tuple[Goal, ...]:
        """
        Returns every goal owned by the Professional.

        External code cannot modify the internal collection.
        """

        return tuple(self._goals)

    @property
    def achievements(self) -> tuple[Achievement, ...]:
        """
        Returns every achievement owned by the Professional.
        """

        return tuple(self._achievements)

    @property
    def certificates(self) -> tuple[Certificate, ...]:
        """
        Returns every certificate owned by the Professional.
        """

        return tuple(self._certificates)

    # =========================================================================
    # Validation
    # =========================================================================

    def __post_init__(self) -> None:
        """
        Validates the Professional immediately after creation.
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

    # =========================================================================
    # Skill Operations
    # =========================================================================

    def add_skill(
        self,
        skill: Skill,
    ) -> None:
        """
        Adds a Skill.

        Duplicate skills are ignored.
        """

        if skill in self._skills:
            return

        self._skills.append(skill)

    # =========================================================================
    # Goal Operations
    # =========================================================================

    def add_goal(
        self,
        goal: Goal,
    ) -> None:
        """
        Adds a Goal.

        Duplicate goals are ignored.
        """

        if goal in self._goals:
            return

        self._goals.append(goal)

    # =========================================================================
    # Achievement Operations
    # =========================================================================

    def add_achievement(
        self,
        achievement: Achievement,
    ) -> None:
        """
        Adds an Achievement.

        Duplicate achievements are ignored.
        """

        if achievement in self._achievements:
            return

        self._achievements.append(achievement)

    # =========================================================================
    # Certificate Operations
    # =========================================================================

    def add_certificate(
        self,
        certificate: Certificate,
    ) -> None:
        """
        Adds a Certificate.

        Duplicate certificates are ignored.
        """

        if certificate in self._certificates:
            return

        self._certificates.append(certificate)

    # =========================================================================
    # Experience Operations
    # =========================================================================

    def add_experience(
        self,
        experience: Experience,
    ) -> None:
        """
        Adds an Experience.

        Business Rule:
            Duplicate experiences are not allowed.
        """

        if experience in self.experiences:
            raise ValueError(
                "Experience already exists."
            )

        self.experiences.append(experience)

    def remove_experience(
        self,
        experience_id,
    ) -> None:
        """
        Removes an Experience by its identifier.
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
        Returns an Experience by its identifier.

        Returns:
            Experience if found, otherwise None.
        """

        for experience in self.experiences:
            if experience.id == experience_id:
                return experience

        return None

    # =========================================================================
    # Project Operations
    # =========================================================================

    def add_project(
        self,
        project: Project,
    ) -> None:
        """
        Adds a Project.

        Duplicate projects are currently allowed.
        """

        self.projects.append(project)

    def remove_project(
        self,
        project_id,
    ) -> None:
        """
        Removes a Project by its identifier.
        """

        self.projects = [
            project
            for project in self.projects
            if project.id != project_id
        ]

    # =========================================================================
    # Education Operations
    # =========================================================================

    def add_education(
            self,
            education: Education,
    ) -> None:
        """
        Adds an Education record.

        Duplicate education records are ignored.
        """

        if education in self.educations:
            return

        self.educations.append(
            education
        )

    def remove_education(
            self,
            education_id,
    ) -> None:
        """
        Removes Education by identifier.
        """

        self.educations = [
            education
            for education in self.educations
            if education.id != education_id
        ]

    def get_education(
            self,
            education_id,
    ):
        """
        Returns Education by identifier.
        """

        for education in self.educations:
            if education.id == education_id:
                return education

        return None

    def add_timeline_event(
            self,
            event: TimelineEvent,
    ) -> None:
        """
        Adds a timeline event.

        Duplicate events are ignored.
        """

        if event in self.timeline:
            return

        self.timeline.append(event)

    def remove_timeline_event(
            self,
            event_id,
    ) -> None:
        """
        Removes a timeline event.
        """

        self.timeline = [
            event
            for event in self.timeline
            if event.id != event_id
        ]

    def get_timeline_event(
            self,
            event_id,
    ):
        """
        Returns a timeline event by id.
        """

        for event in self.timeline:
            if event.id == event_id:
                return event

        return None