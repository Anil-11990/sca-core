"""
Achievement Response DTO.

Represents an Achievement returned to API clients.
"""

from datetime import datetime

from pydantic import BaseModel


class AchievementResponse(BaseModel):
    """
    Achievement returned by the API.
    """

    id: str

    title: str

    issuer: str

    achievement_type: str

    description: str

    credential_url: str

    awarded_at: datetime