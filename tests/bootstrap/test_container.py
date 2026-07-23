from app.bootstrap.container import Container
from app.application.use_cases.create_professional import CreateProfessional


def test_container_creates_use_case():
    container = Container()

    use_case = container.create_professional_use_case()

    assert isinstance(use_case, CreateProfessional)

from app.application.use_cases.get_projects import (
    GetProjects,
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


def test_get_projects():

    repository = MemoryProfessionalRepository()

    professional = Professional(
        full_name=FullName("Anil Khanal"),
        primary_goal="Build ANIrex",
    )

    project = Project(
        name=ProjectName("SCA"),
    )

    professional.add_project(
        project,
    )

    repository.save(
        professional,
    )

    use_case = GetProjects(
        repository,
    )

    projects = use_case.execute(
        professional.id,
    )

    assert len(projects) == 1

    assert projects[0].name == ProjectName(
        "SCA"
    )