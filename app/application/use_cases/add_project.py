"""
Add Project Use Case.
"""

from uuid import UUID

from app.domain.project.project import Project
from app.domain.professional.repository import (
    ProfessionalRepository,
)


class AddProject:
    """
    Adds a Project to a Professional.
    """

    def __init__(
        self,
        repository: ProfessionalRepository,
    ):
        self._repository = repository

    def execute(
        self,
        professional_id: UUID,
        project: Project,
    ):

        professional = self._repository.get_by_id(
            professional_id
        )

        if professional is None:
            return None

        professional.add_project(
            project
        )

        self._repository.save(
            professional
        )

        return professional