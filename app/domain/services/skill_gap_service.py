"""
Domain Service:
Skill Gap Analysis

Identifies missing skills required
for career progression.
"""

from app.domain.professional.professional import Professional


class SkillGapService:
    """
    Calculates missing skills.
    """

    def calculate(
        self,
        professional: Professional,
        required_skills: list[str],
    ) -> list[str]:

        current_skills = {
            skill.name.lower()
            for skill in professional.skills
        }

        gaps = []

        for skill in required_skills:
            if skill.lower() not in current_skills:
                gaps.append(skill)

        return gaps