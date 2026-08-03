from app.domain.intelligence.recommendation import (
    Recommendation,
)


def test_create_recommendation():

    recommendation = Recommendation(
        action="Learn AWS",
        reason="Cloud skills are required for backend roles.",
        priority="HIGH",
    )

    assert recommendation.action == "Learn AWS"
    assert recommendation.priority == "HIGH"


def test_empty_action_is_invalid():

    try:
        Recommendation(
            action="",
            reason="Improve skills",
            priority="LOW",
        )

    except ValueError:
        assert True

    else:
        assert False