"""
Tests for Remove Project Use Case.
"""

from app.application.use_cases.remove_project import (
    RemoveProject,
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



def test_remove_project():

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
    # Add existing project
    # ---------------------------------

    project = Project(
        name=ProjectName(
            "SCA Core"
        ),
        description="AI Career Platform",
    )


    professional.add_project(
        project
    )


    repo.save(
        professional
    )



    # ---------------------------------
    # Execute remove
    # ---------------------------------

    use_case = RemoveProject(
        repo
    )


    result = use_case.execute(
        professional.id,
        project.id,
    )



    # ---------------------------------
    # Assert
    # ---------------------------------

    assert result is True


    updated_professional = repo.get_by_id(
        professional.id
    )


    assert len(
        updated_professional.projects
    ) == 0