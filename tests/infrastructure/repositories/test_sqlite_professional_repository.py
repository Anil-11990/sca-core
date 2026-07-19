from app.domain.common.value_objects.full_name import FullName
from app.domain.goal.goal import Goal
from app.domain.goal.value_objects.goal_title import GoalTitle
from app.domain.professional.professional import Professional
from app.infrastructure.repositories.sqlite_professional_repository import (
    SQLiteProfessionalRepository,
)


def test_save_and_load_goals():
    repo = SQLiteProfessionalRepository()

    professional = Professional(
        full_name=FullName("Anil Khanal"),
        primary_goal="Build ANIrex AI",
    )

    professional.add_goal(
        Goal(GoalTitle("Launch MVP"))
    )

    professional.add_goal(
        Goal(GoalTitle("Get first customer"))
    )

    repo.save(professional)

    loaded = repo.get_by_id(professional.id)

    assert loaded is not None
    assert len(loaded.goals) == 2

from app.domain.achievement.achievement import Achievement
from app.domain.achievement.achievement_type import (
    AchievementType,
)
from app.domain.achievement.value_objects.achievement_title import (
    AchievementTitle,
)
from app.domain.achievement.value_objects.issuer import Issuer


def test_save_and_load_achievement():
    """
    A Professional's achievements should be
    persisted and restored.
    """

    repo = SQLiteProfessionalRepository()

    professional = Professional(
        full_name=FullName("Anil Khanal"),
        primary_goal="Build ANIrex AI",
    )

    achievement = Achievement(
        title=AchievementTitle(
            "AWS Certified Developer"
        ),
        issuer=Issuer(
            "Amazon Web Services"
        ),
        achievement_type=AchievementType.CERTIFICATION,
        description="Associate Level",
    )

    professional.add_achievement(
        achievement
    )

    repo.save(professional)

    loaded = repo.get_by_id(professional.id)

    assert loaded is not None

    assert len(
        loaded.achievements
    ) == 1

    restored = loaded.achievements[0]

    assert restored.title == AchievementTitle(
        "AWS Certified Developer"
    )

    assert restored.issuer == Issuer(
        "Amazon Web Services"
    )

    assert (
        restored.achievement_type
        == AchievementType.CERTIFICATION
    )

    assert (
        restored.description
        == "Associate Level"
    )