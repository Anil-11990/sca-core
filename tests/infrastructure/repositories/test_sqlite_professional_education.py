from app.domain.professional.professional import Professional
from app.domain.common.value_objects.full_name import FullName

from app.domain.education.education import Education
from app.domain.education.degree_level import DegreeLevel
from app.domain.education.graduation_status import GraduationStatus

from app.infrastructure.repositories.sqlite_professional_repository import (
    SQLiteProfessionalRepository,
)


def test_save_and_restore_professional_education():

    repository = SQLiteProfessionalRepository()


    professional = Professional(
        full_name=FullName(
            "Anil Khanal"
        ),
        primary_goal="Build ANIrex AI",
    )


    education = Education(
        institution="University of West London",
        degree_level=DegreeLevel.BACHELOR,
        field_of_study="Computer Science",
        graduation_status=GraduationStatus.COMPLETED,
    )


    professional.add_education(
        education
    )


    repository.save(
        professional
    )


    restored = repository.get_by_id(
        professional.id
    )


    assert restored is not None


    assert len(
        restored.educations
    ) == 1


    restored_education = (
        restored.educations[0]
    )


    assert (
        str(restored_education.institution)
        ==
        "University of West London"
    )


    assert (
        restored_education.degree_level
        ==
        DegreeLevel.BACHELOR
    )


    assert (
        restored_education.graduation_status
        ==
        GraduationStatus.COMPLETED
    )