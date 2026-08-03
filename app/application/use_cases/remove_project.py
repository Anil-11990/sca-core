"""
Remove Project Use Case.
"""

from uuid import UUID

from app.domain.repositories.professional_repository import (
    ProfessionalRepository,
)


class RemoveProject:
    """
    Removes a project from a Professional.
    """

    def __init__(
        self,
        repository: ProfessionalRepository,
    ):
        self._repository = repository

    def execute(
        self,
        professional_id: UUID,
        project_id: UUID,
    ):

        professional = self._repository.get_by_id(
            professional_id
        )

        if professional is None:
            return False

        existing = any(
            project.id == project_id
            for project in professional.projects
        )

        if not existing:
            return False

        professional.remove_project(
            project_id
        )

        self._repository.save(
            professional
        )

        return True