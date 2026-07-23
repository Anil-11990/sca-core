"""
Response DTO for Achievement.
"""

from dataclasses import dataclass
from datetime import datetime


@dataclass(slots=True, frozen=True)
class AchievementResponse:

    id: str

    title: str

    issuer: str

    achievement_type: str

    description: str

    credential_url: str

    awarded_at: datetime