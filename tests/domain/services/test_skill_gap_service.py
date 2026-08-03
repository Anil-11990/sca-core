from app.domain.professional.professional import Professional
from app.domain.common.value_objects.full_name import FullName
from app.domain.skill.skill import Skill

from app.domain.services.skill_gap_service import (
    SkillGapService,
)


def test_skill_gap_identifies_missing_skills():

    professional = Professional(
        full_name=FullName(
            "Anil Khanal"
        ),
        primary_goal="Become AI Engineer",
    )

    professional.add_skill(
        Skill("Python")
    )

    professional.add_skill(
        Skill("Java")
    )


    service = SkillGapService()


    gaps = service.calculate(
        professional,
        [
            "Python",
            "Machine Learning",
            "LLM",
            "Docker",
        ],
    )


    assert gaps == [
        "Machine Learning",
        "LLM",
        "Docker",
    ]