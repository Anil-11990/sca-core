"""
Experience Entity.
"""

from dataclasses import dataclass

from app.domain.common.entity import Entity

from app.domain.experience.value_objects.job_title import (
    JobTitle,
)

from app.domain.experience.value_objects.company_name import (
    CompanyName,
)

from app.domain.experience.value_objects.experience_period import (
    ExperiencePeriod,
)

from app.domain.experience.experience_description import (
    ExperienceDescription,
)

from app.domain.experience.employment_type import (
    EmploymentType,
)
from app.domain.experience.value_objects.job_title import JobTitle
from app.domain.experience.value_objects.company_name import CompanyName
from app.domain.experience.value_objects.experience_period import (
    ExperiencePeriod,
)
from app.domain.experience.experience_description import (
    ExperienceDescription,
)
from app.domain.experience.employment_type import EmploymentType

@dataclass(eq=False, slots=True)
class Experience(Entity):
    """
    Represents a Professional Experience.
    """

    job_title: JobTitle

    company_name: CompanyName

    employment_type: EmploymentType

    experience_period: ExperiencePeriod

    description: ExperienceDescription