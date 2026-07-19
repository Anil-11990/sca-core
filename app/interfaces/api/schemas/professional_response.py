"""
Professional Response DTO.

Represents Professional data returned
to API clients.
"""

from datetime import datetime

from pydantic import BaseModel


class ProfessionalResponse(BaseModel):
    """
    Response model representing a Professional.
    """

    id: str

    full_name: str

    primary_goal: str

    created_at: datetime