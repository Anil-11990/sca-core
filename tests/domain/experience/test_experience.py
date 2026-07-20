from datetime import date

from app.domain.experience.experience import Experience
from app.domain.experience.value_objects.job_title import JobTitle
from app.domain.experience.value_objects.company_name import CompanyName
from app.domain.experience.value_objects.experience_period import (
    ExperiencePeriod,
)
from app.domain.experience.experience_description import (
    ExperienceDescription,
)
from app.domain.experience.employment_type import (
    EmploymentType,
)


def test_create_experience():

    experience = Experience(
        job_title=JobTitle("Software Engineer"),
        company_name=CompanyName("ANIrex"),
        employment_type=EmploymentType.FULL_TIME,
        experience_period=ExperiencePeriod(
            start_date=date(2024, 1, 1),
            end_date=None,
        ),
        description=ExperienceDescription(
            "Building AI systems."
        ),
    )

    assert experience.job_title == JobTitle(
        "Software Engineer"
    )

    assert experience.company_name == CompanyName(
        "ANIrex"
    )

    assert (
        experience.employment_type
        == EmploymentType.FULL_TIME
    )