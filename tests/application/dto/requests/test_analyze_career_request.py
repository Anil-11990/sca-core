from app.application.dto.requests.analyze_career_request import (
    AnalyzeCareerRequest,
)


def test_analyze_career_request_creation():

    request = AnalyzeCareerRequest(
        professional_id="123",
        required_skills=[
            "Python",
            "AI",
        ],
    )


    assert request.professional_id == "123"

    assert len(
        request.required_skills
    ) == 2



def test_analyze_career_request_requires_professional_id():

    try:

        AnalyzeCareerRequest(
            professional_id="",
            required_skills=[],
        )

        assert False

    except ValueError:

        assert True