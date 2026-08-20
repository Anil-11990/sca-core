from app.application.dto.responses.career_intelligence_response import (
    CareerIntelligenceResponse,
)



def test_career_intelligence_response_creation():

    response = CareerIntelligenceResponse(
        career_score=90,
        profile_completion=80,
        skill_gaps=[
            "Docker"
        ],
        career_readiness=85,
    )


    assert response.career_score == 90

    assert response.profile_completion == 80

    assert response.skill_gaps == [
        "Docker"
    ]

    assert response.career_readiness == 85



def test_career_intelligence_response_rejects_negative_score():

    try:

        CareerIntelligenceResponse(
            career_score=-1,
            profile_completion=50,
            skill_gaps=[],
            career_readiness=50,
        )

        assert False

    except ValueError:

        assert True