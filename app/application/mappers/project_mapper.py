from app.domain.project.project import Project
from app.application.dto.responses.project_response import (
    ProjectResponse,
)


class ProjectMapper:
    """
    Maps Project entity to ProjectResponse DTO.
    """

    @staticmethod
    def to_response(
        project: Project,
    ) -> ProjectResponse:

        return ProjectResponse(
            id=str(project.id),
            name=str(project.name),
            description=str(
                project.description
            ),
            technologies=[
                str(item)
                for item in project.technologies
            ],
            repository_url=(
                project.repository_url
            ),
            live_url=(
                project.live_url
            ),
        )