from app.application.use_cases.add_achievement import AddAchievement
from app.domain.achievement.achievement import Achievement
from app.domain.achievement.achievement_type import AchievementType
from app.domain.achievement.value_objects.achievement_title import AchievementTitle
from app.domain.achievement.value_objects.issuer import Issuer
from app.domain.common.value_objects.full_name import FullName
from app.domain.professional.professional import Professional
from app.infrastructure.repositories.memory_professional_repository import (
    MemoryProfessionalRepository,
)


def test_add_achievement():
    repo = MemoryProfessionalRepository()

    professional = Professional(
        full_name=FullName("Anil Khanal"),
        primary_goal="Build ANIrex AI",
    )

    repo.save(professional)

    use_case = AddAchievement(repo)

    achievement = Achievement(
        title=AchievementTitle("AWS"),
        issuer=Issuer("Amazon"),
        achievement_type=AchievementType.CERTIFICATION,
    )

    updated = use_case.execute(
        professional.id,
        achievement,
    )

    assert len(updated.achievements) == 1