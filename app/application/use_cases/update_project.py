"""
Update Project Use Case.
"""

from uuid import UUID

from app.domain.professional.repository import (
    ProfessionalRepository,
)


class UpdateProject:
    """
    Updates an existing project
    belonging to a Professional.
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
        name=None,
        description=None,
        repository_url=None,
        live_url=None,
        technologies=None,
    ):

        professional = self._repository.get_by_id(
            professional_id
        )

        if professional is None:
            return None


        project = None

        for item in professional.projects:
            if item.id == project_id:
                project = item
                break


        if project is None:
            return None


        if name is not None:
            project.name = name


        if description is not None:
            project.description = description


        if repository_url is not None:
            project.repository_url = repository_url


        if live_url is not None:
            project.live_url = live_url


        if technologies is not None:
            project.technologies = technologies


        self._repository.save(
            professional
        )

        return project