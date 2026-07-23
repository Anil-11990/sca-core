from app.application.use_cases.add_project import (
    AddProject,
)

from app.domain.common.value_objects.full_name import (
    FullName,
)

from app.domain.professional.professional import (
    Professional,
)

from app.domain.project.project import (
    Project,
)

from app.domain.project.value_objects.project_name import (
    ProjectName,
)

from app.infrastructure.repositories.memory_professional_repository import (
    MemoryProfessionalRepository,
)


def test_add_project():

    repository = MemoryProfessionalRepository()

    professional = Professional(
        full_name=FullName("Anil Khanal"),
        primary_goal="Build ANIrex",
    )

    repository.save(professional)

    project = Project(
        name=ProjectName("SCA"),
    )

    use_case = AddProject(
        repository,
    )

    result = use_case.execute(
        professional.id,
        project,
    )

    assert result is not None

    assert len(
        result.projects
    ) == 1