from app.application.use_cases.update_achievement import UpdateAchievement
from app.domain.achievement.achievement import Achievement
from app.domain.achievement.achievement_type import AchievementType
from app.domain.achievement.value_objects.achievement_title import AchievementTitle
from app.domain.achievement.value_objects.issuer import Issuer
from app.domain.common.value_objects.full_name import FullName
from app.domain.professional.professional import Professional
from app.infrastructure.repositories.memory_professional_repository import (
    MemoryProfessionalRepository,
)


def test_update_achievement():
    repo = MemoryProfessionalRepository()

    professional = Professional(
        full_name=FullName("Anil Khanal"),
        primary_goal="Build ANIrex AI",
    )

    achievement = Achievement(
        title=AchievementTitle("Old Achievement"),
        issuer=Issuer("Old Issuer"),
        achievement_type=AchievementType.CERTIFICATION,
    )

    professional.add_achievement(achievement)

    repo.save(professional)

    updated_achievement = Achievement(
        title=AchievementTitle("New Achievement"),
        issuer=Issuer("New Issuer"),
        achievement_type=AchievementType.CERTIFICATION,
    )

    use_case = UpdateAchievement(repo)

    updated = use_case.execute(
        professional.id,
        achievement.id,
        updated_achievement,
    )

    assert len(updated.achievements) == 1
    assert (
        updated.achievements[0].title.value
        == "New Achievement"
    )