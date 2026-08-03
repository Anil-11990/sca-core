from app.domain.professional.professional import (
    Professional,
)

from app.domain.common.value_objects.full_name import (
    FullName,
)

from app.domain.services.career_intelligence_service import (
    CareerIntelligenceService,
)


def create_professional():

    return Professional(
        full_name=FullName(
            "Anil Khanal"
        ),
        primary_goal="Build ANIrex AI",
    )


def test_empty_profile_generates_recommendation():

    professional = create_professional()

    service = CareerIntelligenceService()

    result = service.analyse(
        professional
    )

    assert len(
        result["recommendations"]
    ) > 0



def test_profile_with_projects_creates_strength():

    professional = create_professional()

    service = CareerIntelligenceService()

    result = service.analyse(
        professional
    )

    assert "insights" in result