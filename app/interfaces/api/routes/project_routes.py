"""
Project API Routes.

Responsibilities
-----------------
- Expose Project endpoints.
- Convert API requests into domain objects.
- Delegate logic to use cases.
- Convert domain objects into responses.

No business rules belong here.
"""


from uuid import UUID

from fastapi import APIRouter, HTTPException


from app.bootstrap.container import container


# ============================================================================
# Schemas
# ============================================================================

from app.interfaces.api.schemas.project_request import (
    ProjectRequest,
)



# ============================================================================
# Mapper
# ============================================================================

from app.interfaces.api.mappers.project_mapper import (
    ProjectMapper,
)



# ============================================================================
# Domain
# ============================================================================

from app.domain.project.project import Project



router = APIRouter(
    prefix="/projects",
    tags=["Projects"],
)



# ============================================================================
# ADD PROJECT
# ============================================================================


@router.post(
    "/{professional_id}",
)
def add_project(
    professional_id: UUID,
    request: ProjectRequest,
):
    """
    Add project to Professional.
    """


    project = Project(
        name=request.name,
        description=request.description,
        repository_url=request.repository_url,
        live_url=request.live_url,
        technologies=request.technologies,
    )


    professional = (
        container
        .add_project_use_case()
        .execute(
            professional_id,
            project,
        )
    )


    if professional is None:
        raise HTTPException(
            status_code=404,
            detail="Professional not found",
        )


    return ProjectMapper.to_response(
        project
    )



# ============================================================================
# GET PROJECTS
# ============================================================================


@router.get(
    "/{professional_id}",
)
def get_projects(
    professional_id: UUID,
):
    """
    Get all projects of Professional.
    """


    projects = (
        container
        .get_projects_use_case()
        .execute(
            professional_id
        )
    )


    return [

        ProjectMapper.to_response(
            project
        )

        for project in projects

    ]



# ============================================================================
# REMOVE PROJECT
# ============================================================================


@router.delete(
    "/{professional_id}/{project_id}",
)
def remove_project(
    professional_id: UUID,
    project_id: UUID,
):
    """
    Remove project from Professional.
    """


    result = (
        container
        .remove_project_use_case()
        .execute(
            professional_id,
            project_id,
        )
    )


    if result is False:
        raise HTTPException(
            status_code=404,
            detail="Project not found",
        )


    return {
        "message": "Project removed successfully"
    }



# ============================================================================
# UPDATE PROJECT
# ============================================================================


@router.patch(
    "/{professional_id}/{project_id}",
)
def update_project(
    professional_id: UUID,
    project_id: UUID,
    request: ProjectRequest,
):
    """
    Update existing project.
    """


    project = (
        container
        .update_project_use_case()
        .execute(
            professional_id,
            project_id,
            name=request.name,
            description=request.description,
            repository_url=request.repository_url,
            live_url=request.live_url,
            technologies=request.technologies,
        )
    )


    if project is None:
        raise HTTPException(
            status_code=404,
            detail="Project not found",
        )


    return ProjectMapper.to_response(
        project
    )