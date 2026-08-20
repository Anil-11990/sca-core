"""
Application Use Case:
Generate Career Insights
"""

from uuid import UUID

from app.domain.intelligence.career_insight import CareerInsight
from app.exceptions.professional_not_found import (
    ProfessionalNotFoundException,
)


class GenerateCareerInsights:
    """
    Generates intelligence insights
    from a professional profile.
    """

    def __init__(
        self,
        repository,
    ) -> None:

        self._repository = repository


    def execute(
        self,
        professional_id: UUID,
    ) -> list[CareerInsight]:

        professional = (
            self._repository.get_by_id(
                professional_id
            )
        )


        if professional is None:
            raise ProfessionalNotFoundException()


        insights = []


        if len(professional.skills) >= 3:
            insights.append(
                CareerInsight(
                    title="Strong Skill Foundation",
                    description=(
                        "Professional has multiple "
                        "technical skills."
                    ),
                    category="Skills",
                )
            )


        if len(professional.projects) > 0:
            insights.append(
                CareerInsight(
                    title="Project Experience Available",
                    description=(
                        "Professional has practical "
                        "project evidence."
                    ),
                    category="Projects",
                )
            )


        return insights