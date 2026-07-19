from app.application.use_cases.get_achievements import GetAchievements
from app.domain.achievement.achievement import Achievement
from app.domain.achievement.achievement_type import AchievementType
from app.domain.achievement.value_objects.achievement_title import AchievementTitle
from app.domain.achievement.value_objects.issuer import Issuer
from app.domain.common.value_objects.full_name import FullName
from app.domain.professional.professional import Professional
from app.infrastructure.repositories.memory_professional_repository import (
    MemoryProfessionalRepository,
)


def test_get_achievements():
    repo = MemoryProfessionalRepository()

    professional = Professional(
        full_name=FullName("Anil Khanal"),
        primary_goal="Build ANIrex AI",
    )

    achievement = Achievement(
        title=AchievementTitle("AWS"),
        issuer=Issuer("Amazon"),
        achievement_type=AchievementType.CERTIFICATION,
    )

    professional.add_achievement(
        achievement
    )

    repo.save(professional)

    use_case = GetAchievements(repo)

    achievements = use_case.execute(
        professional.id
    )

    assert len(achievements) == 1