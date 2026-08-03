"""
Domain Service:
Career Readiness

Evaluates professional readiness
for career progression.
"""

from app.domain.professional.professional import Professional


class CareerReadinessService:
    """
    Calculates career readiness percentage.
    """

    def calculate(
        self,
        professional: Professional,
        career_score: int,
        skill_gaps: list[str],
    ) -> int:

        readiness = career_score

        penalty = len(skill_gaps) * 5

        readiness -= penalty

        if readiness < 0:
            readiness = 0

        return readiness