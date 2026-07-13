"""
Response models for the API.

These models describe what data
is returned to API clients.
"""

from pydantic import BaseModel


class ProfessionalResponse(BaseModel):
    """
    JSON returned when a Professional is requested.
    """

    id: str
    full_name: str
    primary_goal: str