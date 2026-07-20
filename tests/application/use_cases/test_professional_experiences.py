"""
Professional Experience Tests.
"""

from datetime import date

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


def build_experience():

    return Experience(
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


def test_add_experience():

    professional = Professional(
        full_name=FullName(
            "Anil Khanal"
        ),
        primary_goal="Build ANIrex AI",
    )

    professional.add_experience(
        build_experience()
    )

    assert len(
        professional.experiences
    ) == 1


def test_get_experience():

    professional = Professional(
        full_name=FullName(
            "Anil Khanal"
        ),
        primary_goal="Build ANIrex AI",
    )

    experience = build_experience()

    professional.add_experience(
        experience
    )

    found = professional.get_experience(
        experience.id
    )

    assert found == experience


def test_remove_experience():

    professional = Professional(
        full_name=FullName(
            "Anil Khanal"
        ),
        primary_goal="Build ANIrex AI",
    )

    experience = build_experience()

    professional.add_experience(
        experience
    )

    professional.remove_experience(
        experience.id
    )

    assert len(
        professional.experiences
    ) == 0