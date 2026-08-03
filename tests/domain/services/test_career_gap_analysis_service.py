from app.domain.professional.professional import Professional
from app.domain.common.value_objects.full_name import FullName
from app.domain.skill.skill import Skill

from app.domain.services.career_gap_analysis_service import (
    CareerGapAnalysisService,
)


def test_detect_missing_skills():

    professional = Professional(
        full_name=FullName(
            "Anil Khanal"
        ),
        primary_goal="Become AI Engineer",
    )


    professional.add_skill(
        Skill("Python")
    )


    service = CareerGapAnalysisService()


    result = service.calculate(
        professional,
        [
            "Python",
            "Machine Learning",
            "LLM",
        ]
    )


    assert result["completion_percentage"] == 33

    assert (
        "Machine Learning"
        in result["missing_skills"]
    )

    assert (
        "LLM"
        in result["missing_skills"]
    )