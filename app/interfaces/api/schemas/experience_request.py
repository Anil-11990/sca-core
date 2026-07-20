"""
Experience Request Schema.
"""

from pydantic import BaseModel


class ExperienceRequest(BaseModel):
    """
    Request payload for creating
    an Experience.
    """

    job_title: str

    company_name: str

    employment_type: str

    description: str

    start_date: str

    end_date: str | None = None