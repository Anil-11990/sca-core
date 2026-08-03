from uuid import uuid4

from app.application.use_cases.update_project import (
    UpdateProject,
)

from app.domain.project.project import (
    Project,
)

from app.domain.project.value_objects.project_name import (
    ProjectName,
)

from app.domain.common.value_objects.full_name import (
    FullName,
)

from app.domain.professional.professional import (
    Professional,
)

from app.infrastructure.repositories.memory_professional_repository import (
    MemoryProfessionalRepository,
)


def test_update_project():

    # ---------------------------------
    # Arrange
    # Create repository
    # ---------------------------------

    repo = MemoryProfessionalRepository()


    # ---------------------------------
    # Create professional
    # ---------------------------------

    professional = Professional(
        full_name=FullName(
            "Anil Khanal"
        ),
        primary_goal="Build ANIrex AI",
    )


    # ---------------------------------
    # Existing project
    # ---------------------------------

    project = Project(
        name=ProjectName(
            "Old Project"
        ),
        description="Old description",
        repository_url="old_repo",
        live_url="old_live",
        technologies=[
            "Python"
        ],
    )


    professional.add_project(
        project
    )


    repo.save(
        professional
    )


    # ---------------------------------
    # Execute update
    # ---------------------------------

    use_case = UpdateProject(
        repo
    )


    updated = use_case.execute(
        professional.id,
        project.id,
        name=ProjectName(
            "SCA Core"
        ),
        description="AI Career Platform",
        repository_url="github.com/sca-core",
        live_url="sca.ai",
        technologies=[
            "Python",
            "FastAPI",
        ],
    )


    # ---------------------------------
    # Assert
    # ---------------------------------

    assert updated is not None

    assert (
        updated.name
        == ProjectName("SCA Core")
    )

    assert (
        updated.description
        == "AI Career Platform"
    )

    assert (
        updated.repository_url
        == "github.com/sca-core"
    )

    assert (
        updated.live_url
        == "sca.ai"
    )

    assert (
        "FastAPI"
        in updated.technologies
    )