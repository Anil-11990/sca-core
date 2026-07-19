from app.domain.professional.professional import Professional
from app.domain.common.value_objects.full_name import FullName

from app.domain.achievement.achievement import Achievement
from app.domain.achievement.achievement_type import (
    AchievementType,
)
from app.domain.achievement.value_objects.achievement_title import (
    AchievementTitle,
)
from app.domain.achievement.value_objects.issuer import Issuer


def test_add_achievement():
    professional = Professional(
        full_name=FullName("Anil Khanal"),
        primary_goal="Build ANIrex AI",
    )

    achievement = Achievement(
        title=AchievementTitle("AWS Certified"),
        issuer=Issuer("Amazon"),
        achievement_type=AchievementType.CERTIFICATION,
    )

    professional.add_achievement(
        achievement
    )

    assert achievement in professional.achievements


def test_duplicate_achievement_is_ignored():
    professional = Professional(
        full_name=FullName("Anil Khanal"),
        primary_goal="Build ANIrex AI",
    )

    achievement = Achievement(
        title=AchievementTitle("AWS Certified"),
        issuer=Issuer("Amazon"),
        achievement_type=AchievementType.CERTIFICATION,
    )

    professional.add_achievement(
        achievement
    )

    professional.add_achievement(
        achievement
    )

    assert len(
        professional.achievements
    ) == 1