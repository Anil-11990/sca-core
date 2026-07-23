"""
Application Use Case:
Add Education
"""

from uuid import UUID

from app.domain.education.education import Education
from app.domain.professional.repository import (
    ProfessionalRepository,
)


class AddEducation:
    """
    Adds Education to a Professional.
    """

    def __init__(
        self,
        repository: ProfessionalRepository,
    ) -> None:

        self._repository = repository


    def execute(
        self,
        professional_id: UUID,
        education: Education,
    ):

        professional = self._repository.get_by_id(
            professional_id
        )


        if professional is None:
            return None


        professional.add_education(
            education
        )


        self._repository.save(
            professional
        )


        return professional