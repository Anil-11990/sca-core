"""
API Response Schema:
Market Intelligence

Defines the HTTP response structure for
Professional market intelligence.

The API schema is responsible only for
representing application results at the
HTTP boundary.

Business rules remain inside the domain.
"""

from pydantic import BaseModel, Field


class MarketIntelligenceResponse(BaseModel):
    """
    API response for Market Intelligence.

    Contains:

        - skills already matched with the market
        - skills representing opportunities
        - high-priority market opportunities
    """

    matched_skills: list[str] = Field(
        default_factory=list
    )

    opportunity_skills: list[str] = Field(
        default_factory=list
    )

    high_priority_opportunities: list[str] = Field(
        default_factory=list
    )