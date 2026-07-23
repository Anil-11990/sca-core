"""
Project API Mapper.
"""

from app.domain.project.project import Project

from app.interfaces.api.schemas.project_response import (
    ProjectResponse,
)


class ProjectMapper:

    @staticmethod
    def to_response(
        project: Project,
    ) -> ProjectResponse:

        return ProjectResponse(

            id=str(project.id),

            name=str(project.name),

            description=project.description,

            repository_url=project.repository_url,

            live_url=project.live_url,

            technologies=project.technologies,
        )