"""
Domain Intelligence:
Career Analyzer

Combines multiple career intelligence
signals into a single professional analysis.
"""

from app.domain.professional.professional import Professional

from app.domain.services.career_score_service import (
    CareerScoreService,
)

from app.domain.services.profile_completeness_service import (
    ProfileCompletenessService,
)

from app.domain.services.career_readiness_service import (
    CareerReadinessService,
)

from app.domain.services.skill_gap_service import (
    SkillGapService,
)


class CareerAnalyzer:
    """
    Generates a complete career intelligence report.
    """

    def __init__(self):

        self._career_score_service = (
            CareerScoreService()
        )

        self._profile_service = (
            ProfileCompletenessService()
        )

        self._readiness_service = (
            CareerReadinessService()
        )

        self._skill_gap_service = (
            SkillGapService()
        )


    def analyze(
        self,
        professional: Professional,
        required_skills: list[str],
    ) -> dict:

        career_score = (
            self._career_score_service.calculate(
                professional
            )
        )


        profile_completion = (
            self._profile_service.calculate(
                professional
            )
        )


        skill_gaps = (
            self._skill_gap_service.calculate(
                professional,
                required_skills,
            )
        )


        readiness = (
            self._readiness_service.calculate(
                professional,
                career_score,
                skill_gaps,
            )
        )


        return {
            "career_score": career_score,
            "profile_completion": profile_completion,
            "skill_gaps": skill_gaps,
            "career_readiness": readiness,
        }