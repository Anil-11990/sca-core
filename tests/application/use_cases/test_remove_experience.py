"""
Tests for Remove Experience Use Case.
"""

from app.application.use_cases.remove_experience import (
    RemoveExperience,
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


def test_remove_experience():

    # -----------------------------
    # Arrange
    # -----------------------------

    repo = MemoryProfessionalRepository()


    professional = Professional(
        full_name=FullName("Anil Khanal"),
        primary_goal="Build ANIrex AI",
    )


    experience = Experience(
        job_title=JobTitle("Developer"),
        company_name=CompanyName("Company"),
        employment_type=EmploymentType.FULL_TIME,
        experience_period=ExperiencePeriod(
            "2024",
            "2025",
        ),
        description=ExperienceDescription(
            "Development work",
        ),
    )


    professional.add_experience(
        experience
    )


    repo.save(
        professional
    )


    # -----------------------------
    # Execute
    # -----------------------------

    use_case = RemoveExperience(
        repo
    )


    result = use_case.execute(
        professional.id,
        experience.id,
    )


    # -----------------------------
    # Assert
    # -----------------------------

    assert len(
        result.experiences
    ) == 0