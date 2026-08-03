from app.domain.professional.professional import Professional
from app.domain.common.value_objects.full_name import FullName
from app.domain.skill.skill import Skill

from app.domain.services.career_gap_service import (
    CareerGapService,
)


def test_ai_professional_has_missing_skills():

    professional = Professional(
        full_name=FullName(
            "Anil Khanal"
        ),
        primary_goal="Become AI Engineer",
    )


    professional.add_skill(
        Skill("Python")
    )


    service = CareerGapService()


    gaps = service.analyse(
        professional
    )


    assert "machine learning" in gaps
    assert "deep learning" in gaps
    assert "llm" in gaps