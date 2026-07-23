"""
Request DTO for adding Experience.
"""

from dataclasses import dataclass
from datetime import date


@dataclass(slots=True, frozen=True)
class AddExperienceRequest:

    professional_id: str

    job_title: str

    company_name: str

    employment_type: str

    start_date: date

    end_date: date | None

    description: str