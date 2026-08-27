from app.domain.professional.professional import Professional
from app.domain.common.value_objects.full_name import FullName
from app.domain.intelligence.market_signal import MarketSignal
from app.domain.services.market_intelligence_service import (
    MarketIntelligenceService,
)


def test_market_intelligence_identifies_matched_and_missing_skills():

    professional = Professional(
        full_name=FullName("Anil Khanal"),
        primary_goal="Build ANIrex AI",
    )

    service = MarketIntelligenceService()

    signals = [
        MarketSignal(
            skill="Python",
            demand_level="High",
            trend="Growing",
            source="Job Market",
        ),
        MarketSignal(
            skill="FastAPI",
            demand_level="High",
            trend="Growing",
            source="Job Market",
        ),
        MarketSignal(
            skill="Kubernetes",
            demand_level="High",
            trend="Growing",
            source="Job Market",
        ),
    ]

    result = service.analyse(
        professional,
        signals,
    )

    assert result["matched_skills"] == []

    assert result["opportunity_skills"] == [
        "Python",
        "FastAPI",
        "Kubernetes",
    ]

    assert result["high_priority_opportunities"] == [
        "Python",
        "FastAPI",
        "Kubernetes",
    ]