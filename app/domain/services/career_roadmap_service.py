"""
Domain Service:
Career Roadmap

Generates a learning roadmap
based on career gaps.
"""

from app.domain.professional.professional import Professional
from app.domain.services.career_gap_service import (
    CareerGapService,
)


class CareerRoadmapService:
    """
    Creates career development roadmap.
    """

    def __init__(self):

        self._gap_service = CareerGapService()


    def generate(
        self,
        professional: Professional,
    ) -> list[dict]:

        gaps = self._gap_service.analyse(
            professional
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

        if skill in high_priority:
            return "High"

        return "Medium"