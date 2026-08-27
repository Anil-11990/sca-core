"""
API Schema Tests:
Market Intelligence

Verifies that the Market Intelligence API
response schema correctly represents the
application result.
"""

from app.api.schemas.market_intelligence_response import (
    MarketIntelligenceResponse,
)


def test_market_intelligence_response():

    response = MarketIntelligenceResponse(
        matched_skills=[
            "Python",
        ],
        opportunity_skills=[
            "Machine Learning",
            "Kubernetes",
        ],
        high_priority_opportunities=[
            "Machine Learning",
            "Kubernetes",
        ],
    )

    assert response.matched_skills == [
        "Python",
    ]

    assert response.opportunity_skills == [
        "Machine Learning",
        "Kubernetes",
    ]

    assert response.high_priority_opportunities == [
        "Machine Learning",
        "Kubernetes",
    ]


def test_market_intelligence_response_defaults():

    response = MarketIntelligenceResponse()

    assert response.matched_skills == []

    assert response.opportunity_skills == []

    assert response.high_priority_opportunities == []