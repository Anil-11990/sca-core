from app.domain.common.value_objects.full_name import FullName
from app.domain.goal.goal import Goal
from app.domain.goal.value_objects.goal_title import GoalTitle
from app.domain.professional.professional import Professional
from app.domain.services.profile_completeness_service import (
    ProfileCompletenessService,
)
from app.domain.skill.skill import Skill


def test_profile_completeness_returns_100():
    professional = Professional(
        full_name=FullName("Anil Khanal"),
        primary_goal="Build ANIrex AI",
    )

    professional.add_skill(Skill("Python"))
    professional.add_goal(
        Goal(title=GoalTitle("Launch MVP"))
    )

    service = ProfileCompletenessService()

    score = service.calculate(professional)

    assert score == 100