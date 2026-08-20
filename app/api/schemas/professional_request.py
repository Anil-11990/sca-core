"""
Professional Request DTO.

Represents incoming data used to create
a Professional through the API.
"""

from pydantic import BaseModel, Field


class ProfessionalRequest(BaseModel):
    """
    Request model for creating a Professional.
    """

    full_name: str = Field(
        ...,
        min_length=2,
        max_length=100,
        description="Professional full name.",
    )

    primary_goal: str = Field(
        ...,
        min_length=3,
        max_length=300,
        description="Primary professional goal.",
    )