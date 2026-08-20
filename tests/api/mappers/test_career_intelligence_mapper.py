from app.api.mappers.career_intelligence_mapper import (
    CareerIntelligenceMapper,
)

from app.domain.intelligence.career_insight import CareerInsight
from app.domain.intelligence.market_signal import MarketSignal
from app.domain.intelligence.recommendation import Recommendation


def test_mapper_creates_api_response():

    result = {

        "insight": CareerInsight(
            title="Backend Strength",
            description="Strong backend engineer.",
            category="Strength",
        ),

        "market_signals": [

            MarketSignal(
                skill="Python",
                demand_level="High",
                trend="Rising",
                source="LinkedIn",
            )

        ],

        "recommendations": [

            Recommendation(
                action="Learn FastAPI",
                reason="High demand",
                priority="High",
            )

        ],
    }

    response = CareerIntelligenceMapper.to_response(
        result
    )

    assert response.insight.title == "Backend Strength"

    assert (
        response.insight.description
        == "Strong backend engineer."
    )

    assert response.insight.category == "Strength"

    assert len(response.market_signals) == 1

    assert len(response.recommendations) == 1

    assert response.market_signals[0].skill == "Python"

    assert response.recommendations[0].action == "Learn FastAPI"