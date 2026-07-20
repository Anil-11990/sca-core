"""
Project Entity.
"""

from dataclasses import dataclass, field

from app.domain.common.entity import Entity
from app.domain.project.value_objects.project_name import (
    ProjectName,
)


@dataclass(eq=False, slots=True)
class Project(Entity):
    """
    Represents a professional project.
    """

    name: ProjectName

    description: str = ""

    repository_url: str = ""

    live_url: str = ""

    technologies: list[str] = field(
        default_factory=list
    )

    def add_technology(
        self,
        technology: str,
    ) -> None:

        technology = technology.strip()

        if not technology:
            return

        if technology not in self.technologies:
            self.technologies.append(
                technology
            )

    def remove_technology(
        self,
        technology: str,
    ) -> None:

        if technology in self.technologies:
            self.technologies.remove(
                technology
            )