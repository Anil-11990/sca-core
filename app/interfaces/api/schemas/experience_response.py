"""
Experience Response Schema.
"""

from pydantic import BaseModel


class ExperienceResponse(BaseModel):
    """
    Experience response DTO.
    """

    id: str

    job_title: str

    company_name: str

    employment_type: str

    description: str

    start_date: str

    end_date: str | None