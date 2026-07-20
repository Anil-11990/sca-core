"""
Tests for GetExperiencesUseCase.
"""

from datetime import date

from app.application.use_cases.get_experiences import (
    GetExperiencesUseCase,
)

from app.domain.common.value_objects.full_name import (
    FullName,
)

from app.domain.professional.professional import (
    Professional,
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


def test_get_experiences():

    repository = (
        MemoryProfessionalRepository()
    )

    professional = Professional(
        full_name=FullName(
            "Anil Khanal"
        ),
        primary_goal="Build ANIrex AI",
    )

    professional.add_experience(

        Experience(
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
    )

    repository.save(
        professional
    )

    use_case = (
        GetExperiencesUseCase(
            repository
        )
    )

    experiences = use_case.execute(
        professional.id
    )

    assert len(
        experiences
    ) == 1