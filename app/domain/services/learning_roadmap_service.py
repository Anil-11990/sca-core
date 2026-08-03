"""
Domain Service:
Learning Roadmap

Generates learning priorities
from skill gaps.
"""


class LearningRoadmapService:
    """
    Creates a simple learning roadmap.
    """

    def generate(
        self,
        skill_gaps: list[str],
    ) -> list[str]:

        roadmap = []

        for index, skill in enumerate(
            skill_gaps,
            start=1,
        ):
            roadmap.append(
                f"Phase {index}: Learn {skill}"
            )

        return roadmap