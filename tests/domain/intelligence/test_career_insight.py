from app.domain.intelligence.career_insight import (
    CareerInsight,
)


def test_create_career_insight():

    insight = CareerInsight(
        title="Missing Cloud Skills",
        description="AWS knowledge is required for target roles.",
        category="Skill Gap",
    )

    assert insight.title == "Missing Cloud Skills"
    assert insight.category == "Skill Gap"


def test_empty_title_is_invalid():

    try:
        CareerInsight(
            title="",
            description="Something",
            category="General",
        )

    except ValueError:
        assert True

    else:
        assert False