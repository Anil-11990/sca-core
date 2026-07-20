from app.domain.professional.professional import (
    Professional,
)

from app.domain.common.value_objects.full_name import (
    FullName,
)

from app.domain.project.project import (
    Project,
)

from app.domain.project.value_objects.project_name import (
    ProjectName,
)


def test_add_project():

    professional = Professional(
        full_name=FullName(
            "Anil Khanal"
        ),
        primary_goal="Build ANIrex AI",
    )

    project = Project(
        name=ProjectName(
            "ANIrex AI"
        )
    )

    professional.add_project(
        project
    )

    assert len(
        professional.projects
    ) == 1


def test_remove_project():

    professional = Professional(
        full_name=FullName(
            "Anil Khanal"
        ),
        primary_goal="Build ANIrex AI",
    )

    project = Project(
        name=ProjectName(
            "ANIrex AI"
        )
    )

    professional.add_project(
        project
    )

    professional.remove_project(
        project.id
    )

    assert len(
        professional.projects
    ) == 0