"""
Tests for AddExperienceUseCase.
"""

from app.application.use_cases.add_experience import (
    AddExperienceUseCase,
)

from app.domain.professional.professional import (
    Professional,
)

from app.domain.common.value_objects.full_name import (
    FullName,
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

from app.domain.experience.value_objects.job_title import (
    JobTitle,
)

from app.domain.experience.value_objects.company_name import (
    CompanyName,
)

from app.domain.experience.value_objects.experience_period import (
    ExperiencePeriod,
)

from app.infrastructure.repositories.memory_professional_repository import (
    MemoryProfessionalRepository,
)

from datetime import date


def test_add_experience():

    repository = (
        MemoryProfessionalRepository()
    )

    professional = Professional(
        full_name=FullName(
            "Anil Khanal"
        ),
        primary_goal="Build ANIrex AI",
    )

    repository.save(
        professional
    )

    experience = Experience(
        job_title=JobTitle(
            "Software Engineer"
        ),
        company_name=CompanyName(
            "ANIrex"
        ),
        employment_type=EmploymentType.FULL_TIME,
        experience_period=ExperiencePeriod(
            start_date=date.today(),
            end_date=None,
        ),
        description=ExperienceDescription(
            "Building AI systems."
        ),
    )

    use_case = AddExperienceUseCase(
        repository
    )

    use_case.execute(
        professional.id,
        experience,
    )

    updated = repository.get_by_id(
        professional.id
    )

    assert len(
        updated.experiences
    ) == 1