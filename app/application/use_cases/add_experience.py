"""
Add Experience Use Case.
"""

from uuid import UUID

from app.domain.experience.experience import Experience


class AddExperienceUseCase:
    """
    Adds an Experience to a Professional.
    """

    def __init__(
        self,
        repository,
    ):
        self._repository = repository

    def execute(
        self,
        professional_id: UUID,
        experience: Experience,
    ):
        professional = self._repository.get_by_id(
            professional_id
        )

        if professional is None:
            return None

        professional.add_experience(
            experience
        )

        self._repository.save(
            professional
        )

        return professional