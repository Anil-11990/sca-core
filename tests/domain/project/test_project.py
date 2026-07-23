from app.domain.project.project import Project
from app.domain.project.value_objects.project_name import (
    ProjectName,
)


def test_create_project():

    project = Project(

        name=ProjectName(
            "ANIrex AI"
        ),

        description="AI Career Platform",

        repository_url="https://github.com/anirex",

        live_url="",

        technologies=[
            "Python",
            "FastAPI",
        ],
    )

    assert project.name == ProjectName(
        "ANIrex AI"
    )

    assert project.description == (
        "AI Career Platform"
    )

    assert project.repository_url == (
        "https://github.com/anirex"
    )

    assert len(
        project.technologies
    ) == 2