"""
Domain Service:
Career Score

Evaluates the strength of a Professional profile.
"""

from app.domain.professional.professional import Professional


class CareerScoreService:
    """
    Calculates career strength score.

    Maximum score = 100
    """

    def calculate(
        self,
        professional: Professional,
    ) -> int:

        score = 0

        # Experience - 25
        if professional.experiences:
            if len(professional.experiences) >= 2:
                score += 25
            else:
                score += 15

        # Projects - 25
        if professional.projects:
            if len(professional.projects) >= 2:
                score += 25
            else:
                score += 15

        # Skills - 20
        if professional.skills:
            if len(professional.skills) >= 3:
                score += 20
            else:
                score += 10

        # Education - 10
        if professional.educations:
            score += 10

        # Certificates - 10
        if professional.certificates:
            score += 10

        # Achievements - 10
        if professional.achievements:
            score += 10

        return score