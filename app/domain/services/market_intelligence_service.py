"""
Domain Service:
Market Intelligence

Compares a Professional's current skills
against external market signals.
"""

from app.domain.professional.professional import Professional
from app.domain.intelligence.market_signal import MarketSignal


class MarketIntelligenceService:
    """
    Analyses market signals against a Professional profile.

    Version 1 identifies:

        - matched skills
        - market opportunity skills
        - high-priority opportunities
    """

    def analyse(
        self,
        professional: Professional,
        market_signals: list[MarketSignal],
    ) -> dict:

        current_skills = {
            skill.name.lower()
            for skill in professional.skills
        }

        matched_skills = []
        opportunity_skills = []
        high_priority_opportunities = []

        for signal in market_signals:

            skill_name = signal.skill.strip()

            if skill_name.lower() in current_skills:

                matched_skills.append(
                    skill_name
                )

            else:

                opportunity_skills.append(
                    skill_name
                )

                if (
                    signal.demand_level.lower() == "high"
                    and signal.trend.lower() == "growing"
                ):

                    high_priority_opportunities.append(
                        skill_name
                    )

        return {
            "matched_skills": matched_skills,
            "opportunity_skills": opportunity_skills,
            "high_priority_opportunities": (
                high_priority_opportunities
            ),
        }