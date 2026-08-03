from app.domain.intelligence.market_signal import (
    MarketSignal,
)


def test_create_market_signal():

    signal = MarketSignal(
        skill="Python",
        demand_level="High",
        trend="Growing",
        source="Job Market",
    )

    assert signal.skill == "Python"
    assert signal.demand_level == "High"


def test_empty_skill_is_invalid():

    try:
        MarketSignal(
            skill="",
            demand_level="High",
            trend="Growing",
            source="Jobs",
        )

    except ValueError:
        assert True

    else:
        assert False