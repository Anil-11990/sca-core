"""
Application Use Case:
Analyze Career
"""

from app.application.dto.responses.career_intelligence_response import (
    CareerIntelligenceResponse,
)

from app.domain.intelligence.career_analyzer import (
    CareerAnalyzer,
)

from app.domain.professional.repository import (
    ProfessionalRepository,
)


class AnalyzeCareer:
    """
    Generates career intelligence
    for a Professional.
    """

    def __init__(
        self,
        repository: ProfessionalRepository,
        analyzer: CareerAnalyzer,
    ) -> None:

        self._repository = repository
        self._analyzer = analyzer


    def execute(
        self,
        professional_id,
        required_skills: list[str],
    ) -> CareerIntelligenceResponse:

        professional = (
            self._repository.get_by_id(
                professional_id
            )
        )


        if professional is None:
            raise ValueError(
                "Professional not found"
            )


        result = (
            self._analyzer.analyze(
                professional,
                required_skills,
            )
        )


        return CareerIntelligenceResponse(
            career_score=result["career_score"],
            profile_completion=result["profile_completion"],
            skill_gaps=result["skill_gaps"],
            career_readiness=result["career_readiness"],
        )