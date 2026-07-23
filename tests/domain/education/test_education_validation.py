import pytest

from app.domain.education.education import Education
from app.domain.education.degree_level import DegreeLevel
from app.domain.education.graduation_status import GraduationStatus



def test_empty_field_of_study():

    with pytest.raises(ValueError):

        Education(
            institution="University",
            degree_level=DegreeLevel.BACHELOR,
            field_of_study="",
            graduation_status=GraduationStatus.COMPLETED
        )



def test_create_master_degree():

    education = Education(
        institution="University of West London",
        degree_level=DegreeLevel.MASTER,
        field_of_study="Artificial Intelligence",
        graduation_status=GraduationStatus.IN_PROGRESS
    )


    assert education.degree_level == DegreeLevel.MASTER

    assert education.graduation_status == GraduationStatus.IN_PROGRESS