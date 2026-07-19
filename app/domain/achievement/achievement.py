"""
Achievement Entity.

Represents a professional achievement earned by a
Professional.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import UTC, datetime

from app.domain.common.entity import Entity

from app.domain.achievement.achievement_type import (
    AchievementType,
)

from app.domain.achievement.value_objects.achievement_title import (
    AchievementTitle,
)

from app.domain.achievement.value_objects.issuer import (
    Issuer,
)


@dataclass(eq=False, slots=True)
class Achievement(Entity):
    """
    Represents a professional achievement.
    """

    title: AchievementTitle

    issuer: Issuer

    achievement_type: AchievementType

    description: str = ""

    credential_url: str = ""

    awarded_at: datetime = field(
        default_factory=lambda: datetime.now(UTC)
    )

    def __post_init__(self) -> None:
        self.description = self.description.strip()
        self.credential_url = self.credential_url.strip()