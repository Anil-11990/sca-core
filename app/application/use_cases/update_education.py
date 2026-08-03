"""
Update Education Use Case.

Responsible for replacing an existing education
record inside a Professional profile.
"""

from uuid import UUID

from app.domain.education.education import Education

from app.domain.repositories.professional_repository import (
    ProfessionalRepository,
)


class UpdateEducation:
    """
    Updates an existing Education record.

    Flow:
    1. Find Professional.
    2. Remove old education using old education id.
    3. Add new education object.
    4. Save updated Professional.
    """


    def __init__(
        self,
        repository: ProfessionalRepository,
    ):
        """
        Inject Professional repository.
        """

        self._repository = repository



    def execute(
        self,
        professional_id: UUID,
        education_id: UUID,
        education: Education,
    ):
        """
        Replace existing education.

        Args:
            professional_id:
                Owner professional identifier.

            education_id:
                Existing education identifier
                that should be replaced.

            education:
                New education object.

        Returns:
            Updated Professional object.
            None if professional does not exist.
        """


        # ---------------------------------
        # Find Professional aggregate
        # ---------------------------------

        professional = self._repository.get_by_id(
            professional_id
        )


        # Professional does not exist
        if professional is None:
            return None



        # ---------------------------------
        # Remove old education
        # ---------------------------------

        professional.remove_education(
            education_id
        )



        # ---------------------------------
        # Add replacement education
        # ---------------------------------

        professional.add_education(
            education
        )



        # ---------------------------------
        # Persist changes
        # ---------------------------------

        self._repository.save(
            professional
        )


        return professional