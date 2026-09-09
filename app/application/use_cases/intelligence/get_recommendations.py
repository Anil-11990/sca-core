"""
Application Use Case:
Get Recommendations
"""

from uuid import UUID

from app.domain.intelligence.recommendation import (
    Recommendation,
)

from app.domain.services.skill_gap_service import (
    SkillGapService,
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
        skill_gap_service: SkillGapService | None = None,
    ) -> None:

        self._repository = repository

        self._skill_gap_service = (
            skill_gap_service
            if skill_gap_service is not None
            else SkillGapService()
        )


    def execute(
        self,
        professional_id: UUID,
        required_skills: list[str] | None = None,
    ) -> list[Recommendation]:

        professional = (
            self._repository.get_by_id(
                professional_id
            )
        )


        if professional is None:
            raise ProfessionalNotFoundException()


        recommendations: list[Recommendation] = []


        # Target-role skill gap recommendation
        if required_skills:

            gaps = self._skill_gap_service.calculate(
                professional,
                required_skills,
            )

            if gaps:

                recommendations.append(
                    Recommendation(
                        action="Close target-role skill gaps",
                        reason=(
                            f"{len(gaps)} target-role "
                            "capabilities are missing: "
                            f"{', '.join(gaps)}."
                        ),
                        priority="HIGH",
                    )
                )


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
