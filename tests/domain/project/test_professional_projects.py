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

        primary_goal="Build ANIrex",
    )

    project = Project(

        name=ProjectName(
            "SCA"
        ),
    )

    professional.add_project(
        project
    )

    assert len(
        professional.projects
    ) == 1