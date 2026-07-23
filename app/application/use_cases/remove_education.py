"""
Application Use Case:
Remove Education
"""

from uuid import UUID

from app.domain.professional.repository import (
    ProfessionalRepository,
)



class RemoveEducation:
    """
    Removes education from a Professional.
    """

    def __init__(
        self,
        repository: ProfessionalRepository,
    ) -> None:

        self._repository = repository



    def execute(
        self,
        professional_id: UUID,
        education_id: UUID,
    ):

        professional = self._repository.get_by_id(
            professional_id
        )


        if professional is None:
            return None


        professional.remove_education(
            education_id
        )


        self._repository.save(
            professional
        )


        return professional