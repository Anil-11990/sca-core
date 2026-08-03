"""
Update Experience Use Case.

Responsible for replacing an existing
Experience record inside a Professional profile.
"""

from uuid import UUID

from app.domain.experience.experience import Experience

from app.domain.repositories.professional_repository import (
    ProfessionalRepository,
)


class UpdateExperience:
    """
    Updates an existing Experience.

    Flow:
    1. Find Professional.
    2. Remove old Experience using its ID.
    3. Add updated Experience.
    4. Save Professional.
    5. Return updated Professional.
    """


    def __init__(
        self,
        repository: ProfessionalRepository,
    ):
        """
        Inject repository dependency.
        """

        self._repository = repository



    def execute(
        self,
        professional_id: UUID,
        experience_id: UUID,
        experience: Experience,
    ):
        """
        Execute update operation.

        Args:
            professional_id:
                Owner Professional ID.

            experience_id:
                Existing Experience ID
                that should be replaced.

            experience:
                New Experience object.

        Returns:
            Updated Professional
            or None if Professional does not exist.
        """


        # ---------------------------------
        # Find Professional
        # ---------------------------------

        professional = self._repository.get_by_id(
            professional_id
        )


        # Professional not found
        if professional is None:
            return None



        # ---------------------------------
        # Remove old experience
        # ---------------------------------

        professional.remove_experience(
            experience_id
        )



        # ---------------------------------
        # Add new updated experience
        # ---------------------------------

        professional.add_experience(
            experience
        )



        # ---------------------------------
        # Persist changes
        # ---------------------------------

        self._repository.save(
            professional
        )


        # Return updated aggregate
        return professional