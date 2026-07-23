from app.domain.professional.professional import Professional

from app.domain.education.education import Education
from app.domain.education.degree_level import DegreeLevel
from app.domain.education.graduation_status import GraduationStatus


def test_add_education():

    professional = Professional(
        "Anil Khanal",
        "Build ANIrex AI"
    )


    education = Education(
        institution="University of West London",
        degree_level=DegreeLevel.BACHELOR,
        field_of_study="Computer Science",
        graduation_status=GraduationStatus.COMPLETED
    )


    professional.add_education(
        education
    )


    assert len(
        professional.educations
    ) == 1



def test_get_education():

    professional = Professional(
        "Anil Khanal",
        "Build ANIrex AI"
    )


    education = Education(
        institution="University of West London",
        degree_level=DegreeLevel.BACHELOR,
        field_of_study="Computer Science",
        graduation_status=GraduationStatus.COMPLETED
    )


    professional.add_education(
        education
    )


    result = professional.get_education(
        education.id
    )


    assert result == education