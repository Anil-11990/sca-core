from app.domain.professional.professional import Professional
from app.domain.common.value_objects.full_name import FullName

from app.domain.services.career_readiness_service import (
    CareerReadinessService,
)


def test_career_readiness_reduces_for_skill_gaps():

    professional = Professional(
        full_name=FullName(
            "Anil Khanal"
        ),
        primary_goal="AI Engineer",
    )


    service = CareerReadinessService()


    readiness = service.calculate(
        professional,
        career_score=80,
        skill_gaps=[
            "Machine Learning",
            "LLM",
        ],
    )


    assert readiness == 70