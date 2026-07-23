"""
Application Use Case:
Get Education
"""

from uuid import UUID

from app.domain.education.education import Education

from app.domain.professional.repository import (
    ProfessionalRepository,
)


class GetEducation:
    """
    Retrieves education records
    belonging to a Professional.
    """


    def __init__(
        self,
        repository: ProfessionalRepository,
    ) -> None:

        self._repository = repository



    def execute(
        self,
        professional_id: UUID,
    ) -> list[Education]:

        professional = self._repository.get_by_id(
            professional_id
        )


        if professional is None:
            return []


        return list(
            professional.educations
        )