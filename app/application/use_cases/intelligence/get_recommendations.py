"""
Application Use Case:
Get Recommendations
"""

from uuid import UUID

from app.domain.intelligence.recommendation import (
    Recommendation,
)

from app.exceptions.professional_not_found import (
    ProfessionalNotFoundException,
)


class GetRecommendations:
    """
    Generates career recommendations
    for a Professional.
    """


    def __init__(
        self,
        repository,
    ) -> None:

        self._repository = repository



    def execute(
        self,
        professional_id: UUID,
    ) -> list[Recommendation]:

        professional = (
            self._repository.get_by_id(
                professional_id
            )
        )


        if professional is None:
            raise ProfessionalNotFoundException()



        recommendations = []


        # Missing skills recommendation
        if len(professional.skills) < 3:

            recommendations.append(
                Recommendation(
                    action="Improve technical skills",
                    reason=(
                        "Professional profile "
                        "has limited skill evidence."
                    ),
                    priority="HIGH",
                )
            )


        # Missing projects recommendation
        if len(professional.projects) == 0:

            recommendations.append(
                Recommendation(
                    action="Build practical projects",
                    reason=(
                        "Projects provide "
                        "career evidence."
                    ),
                    priority="MEDIUM",
                )
            )


        return recommendations