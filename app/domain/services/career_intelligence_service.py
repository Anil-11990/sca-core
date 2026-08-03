"""
Career Intelligence Service.

Transforms professional profile analysis
into intelligence insights and recommendations.
"""

from app.domain.professional.professional import Professional

from app.domain.intelligence.career_insight import (
    CareerInsight,
)

from app.domain.intelligence.recommendation import (
    Recommendation,
)


class CareerIntelligenceService:
    """
    Generates career intelligence.
    """

    def analyse(
        self,
        professional: Professional,
    ) -> dict:

        insights = []

        recommendations = []


        # -------------------------------------------------
        # Skills intelligence
        # -------------------------------------------------

        if professional.skills:

            insights.append(
                CareerInsight(
                    title="Technical Foundation",
                    description=(
                        "Professional has recorded technical skills."
                    ),
                    category="Strength",
                )
            )

        else:

            insights.append(
                CareerInsight(
                    title="Skill Gap",
                    description=(
                        "Professional has no recorded skills."
                    ),
                    category="Gap",
                )
            )

            recommendations.append(
                Recommendation(
                    action="Add professional skills",
                    reason=(
                        "Skills are required to evaluate career direction."
                    ),
                    priority="HIGH",
                )
            )


        # -------------------------------------------------
        # Project intelligence
        # -------------------------------------------------

        if professional.projects:

            insights.append(
                CareerInsight(
                    title="Project Experience",
                    description=(
                        "Professional has practical project evidence."
                    ),
                    category="Strength",
                )
            )

        else:

            recommendations.append(
                Recommendation(
                    action="Build practical projects",
                    reason=(
                        "Projects demonstrate applied capability."
                    ),
                    priority="MEDIUM",
                )
            )


        return {
            "insights": insights,
            "recommendations": recommendations,
        }