from app.domain.experience.experience import Experience
from app.application.dto.responses.experience_response import (
    ExperienceResponse,
)


class ExperienceMapper:
    """
    Maps Experience entity to ExperienceResponse DTO.
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
            employment_type=(
                experience.employment_type.value
            ),
            start_date=(
                experience.experience_period.start_date
            ),
            end_date=(
                experience.experience_period.end_date
            ),
            description=str(
                experience.description
            ),
        )