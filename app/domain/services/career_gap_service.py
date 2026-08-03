"""
Domain Service:
Career Gap Analysis

Identifies missing career requirements
for a Professional profile.
"""

from app.domain.professional.professional import Professional


class CareerGapService:
    """
    Analyses missing career capabilities.
    """

    def analyse(
        self,
        professional: Professional,
    ) -> list[str]:

        gaps = []

        skill_names = [
            skill.name.lower()
            for skill in professional.skills
        ]

        goal = professional.primary_goal.lower()


        # AI Engineer pathway
        if "ai" in goal or "artificial intelligence" in goal:

            required_skills = [
                "python",
                "machine learning",
                "deep learning",
                "llm",
                "vector database",
            ]

            for skill in required_skills:

                if skill not in skill_names:
                    gaps.append(skill)


        return gaps