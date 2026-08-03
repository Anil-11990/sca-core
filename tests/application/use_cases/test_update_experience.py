"""
Tests for Update Experience Use Case.
"""

from app.application.use_cases.update_experience import (
    UpdateExperience,
)

from app.domain.experience.experience import (
    Experience,
)

from app.domain.experience.employment_type import (
    EmploymentType,
)

from app.domain.experience.experience_description import (
    ExperienceDescription,
)

from app.domain.experience.value_objects.company_name import (
    CompanyName,
)

from app.domain.experience.value_objects.job_title import (
    JobTitle,
)

from app.domain.experience.value_objects.experience_period import (
    ExperiencePeriod,
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


def test_update_experience():

    # -----------------------------
    # Arrange
    # -----------------------------

    repo = MemoryProfessionalRepository()


    professional = Professional(
        full_name=FullName("Anil Khanal"),
        primary_goal="Build ANIrex AI",
    )


    # Existing experience
    old_experience = Experience(
        job_title=JobTitle("Software Developer"),
        company_name=CompanyName("Old Company"),
        employment_type=EmploymentType.FULL_TIME,
        experience_period=ExperiencePeriod(
            "2024",
            "2025",
        ),
        description=ExperienceDescription(
            "Backend development",
        ),
    )


    professional.add_experience(
        old_experience
    )


    repo.save(
        professional
    )


    # New updated experience

    new_experience = Experience(
        job_title=JobTitle("Senior Software Developer"),
        company_name=CompanyName("ANIrex AI"),
        employment_type=EmploymentType.FULL_TIME,
        experience_period=ExperiencePeriod(
            "2025",
            "2026",
        ),
        description=ExperienceDescription(
            "AI platform development",
        ),
    )


    # -----------------------------
    # Execute
    # -----------------------------

    use_case = UpdateExperience(
        repo
    )


    updated = use_case.execute(
        professional.id,
        old_experience.id,
        new_experience,
    )


    # -----------------------------
    # Assert
    # -----------------------------

    assert len(
        updated.experiences
    ) == 1


    assert (
        updated.experiences[0]
        .job_title.value
        == "Senior Software Developer"
    )