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
def test_each_recommendation_gets_unique_id():

    first = Recommendation(
        action="Learn Python",
        reason="Python is important for AI development.",
        priority="High",
    )

    second = Recommendation(
        action="Learn Docker",
        reason="Docker improves deployment skills.",
        priority="Medium",
    )

    assert first.id != second.id