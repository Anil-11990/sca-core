from app.domain.project.project import Project
from app.domain.project.value_objects.project_name import (
    ProjectName,
)


def test_add_technology():

    project = Project(

        name=ProjectName(
            "SCA"
        ),
    )

    project.add_technology(
        "Python"
    )

    project.add_technology(
        "FastAPI"
    )

    assert len(
        project.technologies
    ) == 2


def test_duplicate_technology_is_ignored():

    project = Project(

        name=ProjectName(
            "SCA"
        ),
    )

    project.add_technology(
        "Python"
    )

    project.add_technology(
        "Python"
    )

    assert len(
        project.technologies
    ) == 1


def test_remove_technology():

    project = Project(

        name=ProjectName(
            "SCA"
        ),
    )

    project.add_technology(
        "Python"
    )

    project.remove_technology(
        "Python"
    )

    assert len(
        project.technologies
    ) == 0