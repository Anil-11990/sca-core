"""
Domain Service:
Career Gap Analysis

Identifies missing career capabilities.
"""


from app.domain.professional.professional import Professional


class CareerGapAnalysisService:
    """
    Analyses gaps between current profile
    and desired career direction.
    """


    def calculate(
        self,
        professional: Professional,
        required_skills: list[str],
    ) -> dict:

        current_skills = {
            skill.name.lower()
            for skill in professional.skills
        }


        missing_skills = [
            skill
            for skill in required_skills
            if skill.lower()
            not in current_skills
        ]


        achieved = (
            len(required_skills)
            -
            len(missing_skills)
        )


        percentage = 0

        if required_skills:
            percentage = int(
                (
                    achieved
                    /
                    len(required_skills)
                )
                *
                100
            )


        return {
            "missing_skills": missing_skills,
            "completion_percentage": percentage,
        }