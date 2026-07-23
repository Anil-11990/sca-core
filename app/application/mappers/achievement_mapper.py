from app.domain.achievement.achievement import Achievement
from app.application.dto.responses.achievement_response import (
    AchievementResponse,
)


class AchievementMapper:
    """
    Maps Achievement entity to DTO.
    """

    @staticmethod
    def to_response(
        achievement: Achievement,
    ) -> AchievementResponse:

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