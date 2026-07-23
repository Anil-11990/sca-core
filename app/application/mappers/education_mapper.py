from app.domain.education.education import Education
from app.application.dto.responses.education_response import (
    EducationResponse,
)


class EducationMapper:
    """
    Maps Education entity to EducationResponse DTO.
    """

    @staticmethod
    def to_response(
        education: Education,
    ) -> EducationResponse:

        return EducationResponse(
            id=str(education.id),
            institution=str(
                education.institution
            ),
            degree_level=(
                education.degree_level.value
            ),
            field_of_study=(
                education.field_of_study
            ),
            graduation_status=(
                education.graduation_status.value
            ),
        )