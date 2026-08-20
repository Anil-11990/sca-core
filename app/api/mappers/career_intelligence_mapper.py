"""
Maps Career Intelligence results into API response schemas.
"""

from app.api.schemas.career_intelligence_response import (
    CareerInsightSchema,
    MarketSignalSchema,
    RecommendationSchema,
    CareerIntelligenceResponse,
)


class CareerIntelligenceMapper:

    @staticmethod
    def to_response(
        result: dict,
    ) -> CareerIntelligenceResponse:

        return CareerIntelligenceResponse(

            insight=CareerInsightSchema(

                title=result["insight"].title,

                description=result["insight"].description,

                category=result["insight"].category,
            ),

            market_signals=[

                MarketSignalSchema(
                    skill=item.skill,
                    demand_level=item.demand_level,
                    trend=item.trend,
                    source=item.source,
                )

                for item in result["market_signals"]

            ],

            recommendations=[

                RecommendationSchema(
                    action=item.action,
                    reason=item.reason,
                    priority=item.priority,
                )

                for item in result["recommendations"]

            ],
        )