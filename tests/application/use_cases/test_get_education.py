from app.application.use_cases.get_education import (
    GetEducation,
)

from app.domain.professional.professional import (
    Professional,
)

from app.domain.common.value_objects.full_name import (
    FullName,
)

from app.domain.education.education import (
    Education,
)

from app.domain.education.degree_level import (
    DegreeLevel,
)

from app.domain.education.graduation_status import (
    GraduationStatus,
)

from app.infrastructure.repositories.memory_professional_repository import (
    MemoryProfessionalRepository,
)


def test_get_education():

    repository = MemoryProfessionalRepository()


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


    use_case = GetEducation(
        repository
    )


    result = use_case.execute(
        professional.id
    )


    assert len(result) == 1

    assert (
        result[0].field_of_study
        ==
        "Computer Science"
    )