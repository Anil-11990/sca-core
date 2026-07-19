import pytest

from app.domain.project.value_objects.project_name import ProjectName


def test_valid_project_name():
    name = ProjectName("ANIrex AI")

    assert str(name) == "ANIrex AI"


def test_blank_project_name():
    with pytest.raises(ValueError):
        ProjectName("")


def test_whitespace_project_name():
    with pytest.raises(ValueError):
        ProjectName("     ")