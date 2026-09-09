"""
Domain Service:
Career Roadmap

Generates a learning roadmap
based on career skill gaps.
"""

from app.domain.professional.professional import Professional
from app.domain.services.skill_gap_service import (
    SkillGapService,
)


class CareerRoadmapService:
    """
    Creates career development roadmap.
    """

    def __init__(self):

        self._skill_gap_service = (
            SkillGapService()
        )

    def generate(
        self,
        professional: Professional,
        required_skills: list[str],
    ) -> list[dict]:

        gaps = self._skill_gap_service.calculate(
            professional,
            required_skills,
        )

        roadmap = []

        for gap in gaps:

            roadmap.append(
                {
                    "skill": gap,
                    "priority": self._priority(gap),
                    "stage": "Learning",
                }
            )

        return roadmap

    def _priority(
        self,
        skill: str,
    ) -> str:

        high_priority = [
            "python",
            "machine learning",
            "llm",
        ]

        if skill.lower() in high_priority:
            return "High"

        return "Medium"
