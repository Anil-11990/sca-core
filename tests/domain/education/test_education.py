from app.domain.education.education import Education
from app.domain.education.degree_level import DegreeLevel
from app.domain.education.graduation_status import GraduationStatus


def test_create_education():

    education = Education(
        institution="University of West London",
        degree_level=DegreeLevel.BACHELOR,
        field_of_study="Computer Science",
        graduation_status=GraduationStatus.COMPLETED
    )

    assert education.institution == "University of West London"
    assert education.degree_level == DegreeLevel.BACHELOR
    assert education.graduation_status == GraduationStatus.COMPLETED