from uuid import uuid4

from app.application.use_cases.intelligence.generate_market_intelligence import (
    GenerateMarketIntelligence,
)
from app.domain.intelligence.market_signal import MarketSignal


def test_generate_market_intelligence():

    professional_id = uuid4()

    professional = type(
        "ProfessionalStub",
        (),
        {
            "skills": [],
        },
    )()

    signals = [
        MarketSignal(
            skill="Python",
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

    class FakeRepository:

        def get_by_id(self, requested_id):

            assert requested_id == professional_id

            return professional

    class FakeMarketIntelligenceService:

        def analyse(
            self,
            professional,
            market_signals,
        ):

            assert professional is not None
            assert len(market_signals) == 2

            return {
                "matched_skills": [],
                "opportunity_skills": [
                    "Python",
                    "Kubernetes",
                ],
                "high_priority_opportunities": [
                    "Python",
                    "Kubernetes",
                ],
            }

    use_case = GenerateMarketIntelligence(
        repository=FakeRepository(),
        market_intelligence_service=(
            FakeMarketIntelligenceService()
        ),
        market_signals=signals,
    )

    result = use_case.execute(
        professional_id
    )

    assert result["matched_skills"] == []

    assert result["opportunity_skills"] == [
        "Python",
        "Kubernetes",
    ]

    assert result["high_priority_opportunities"] == [
        "Python",
        "Kubernetes",
    ]