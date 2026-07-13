"""
Domain Service:
Profile Completeness

Evaluates how complete a Professional profile is.
"""

from app.domain.professional.professional import Professional


class ProfileCompletenessService:
    """
    Calculates profile completeness.

    Version 1 scoring:

    Full name      = 40
    Skill          = 30
    Goal           = 30

    Maximum = 100
    """

    def calculate(
        self,
        professional: Professional,
    ) -> int:

        score = 0

        # Every professional has a validated FullName.
        if professional.full_name:
            score += 40

        # At least one skill.
        if professional.skills:
            score += 30

        # At least one goal.
        if professional.goals:
            score += 30

        return score