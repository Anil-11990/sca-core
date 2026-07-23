from app.application.use_cases.add_education import (
    AddEducation,
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


def test_add_education():

    repository = MemoryProfessionalRepository()


    professional = Professional(
        full_name=FullName(
            "Anil Khanal"
        ),
        primary_goal="Build ANIrex AI",
    )


    repository.save(
        professional
    )


    education = Education(
        institution="University of West London",
        degree_level=DegreeLevel.BACHELOR,
        field_of_study="Computer Science",
        graduation_status=GraduationStatus.COMPLETED,
    )


    use_case = AddEducation(
        repository
    )


    result = use_case.execute(
        professional.id,
        education,
    )


    assert result is not None

    assert len(
        result.educations
    ) == 1

    assert (
        result.educations[0].field_of_study
        ==
        "Computer Science"
    )