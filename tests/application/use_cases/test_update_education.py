from app.application.use_cases.update_education import (
    UpdateEducation,
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

from app.domain.common.value_objects.full_name import (
    FullName,
)

from app.domain.professional.professional import (
    Professional,
)

from app.infrastructure.repositories.memory_professional_repository import (
    MemoryProfessionalRepository,
)


def test_update_education():

    # -----------------------------
    # Arrange
    # Create repository
    # -----------------------------

    repo = MemoryProfessionalRepository()


    # -----------------------------
    # Create professional
    # -----------------------------

    professional = Professional(
        full_name=FullName("Anil Khanal"),
        primary_goal="Build ANIrex AI",
    )


    # -----------------------------
    # Existing education
    # -----------------------------

    old_education = Education(
        institution="University of West London",
        degree_level=DegreeLevel.BACHELOR,
        field_of_study="Computer Science",
        graduation_status=GraduationStatus.COMPLETED,
    )


    professional.add_education(
        old_education
    )


    repo.save(
        professional
    )


    # -----------------------------
    # New updated education
    # -----------------------------

    new_education = Education(
        institution="University of London",
        degree_level=DegreeLevel.MASTER,
        field_of_study="Artificial Intelligence",
        graduation_status=GraduationStatus.COMPLETED,
    )


    # -----------------------------
    # Execute update
    # -----------------------------

    use_case = UpdateEducation(
        repo
    )

    updated = use_case.execute(
        professional.id,
        old_education.id,
        new_education,
    )


    # -----------------------------
    # Assert
    # -----------------------------

    assert len(
        updated.educations
    ) == 1


    assert (
        updated.educations[0].field_of_study
        == "Artificial Intelligence"
    )