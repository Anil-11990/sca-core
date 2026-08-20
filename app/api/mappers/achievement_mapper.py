"""
Achievement API Mapper.

Converts Achievement domain objects
into API response DTOs.
"""

from app.domain.achievement.achievement import Achievement

from app.api.schemas.achievement_response import (
    AchievementResponse,
)


class AchievementMapper:
    """
    Converts Achievement domain objects
    into API response models.
    """

    @staticmethod
    def to_response(
        achievement: Achievement,
    ) -> AchievementResponse:
        """
        Convert Domain Achievement
        into AchievementResponse DTO.
        """

        return AchievementResponse(
            id=str(achievement.id),
            title=str(achievement.title),
            issuer=str(achievement.issuer),
            achievement_type=(
                achievement.achievement_type.value
            ),
            description=achievement.description,
            credential_url=achievement.credential_url,
            awarded_at=achievement.awarded_at,
        )