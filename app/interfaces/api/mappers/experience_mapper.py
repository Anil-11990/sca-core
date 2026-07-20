"""
Experience API Mapper.
"""

from app.domain.experience.experience import Experience

from app.interfaces.api.schemas.experience_response import (
    ExperienceResponse,
)


class ExperienceMapper:
    """
    Maps Experience entities
    into API DTOs.
    """

    @staticmethod
    def to_response(
        experience: Experience,
    ) -> ExperienceResponse:

        return ExperienceResponse(
            id=str(experience.id),
            job_title=str(
                experience.job_title
            ),
            company_name=str(
                experience.company_name
            ),
            employment_type=experience.employment_type.value,
            description=str(
                experience.description
            ),
            start_date=str(
                experience.experience_period.start_date
            ),
            end_date=(
                str(
                    experience.experience_period.end_date
                )
                if experience.experience_period.end_date
                else None
            ),
        )