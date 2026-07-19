"""
Achievement Request DTO.

Represents the JSON received from API clients
when creating a new Achievement.
"""

from pydantic import BaseModel, Field


class AchievementRequest(BaseModel):
    """
    Request body for creating an Achievement.
    """

    title: str = Field(
        min_length=1,
        max_length=150,
    )

    issuer: str = Field(
        min_length=1,
        max_length=150,
    )

    achievement_type: str

    description: str = ""

    credential_url: str = ""