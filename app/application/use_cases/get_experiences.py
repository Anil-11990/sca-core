"""
Get Experiences Use Case.
"""

from uuid import UUID


class GetExperiencesUseCase:
    """
    Returns every Experience belonging to a Professional.
    """

    def __init__(
        self,
        repository,
    ):
        self._repository = repository

    def execute(
        self,
        professional_id: UUID,
    ):
        professional = self._repository.get_by_id(
            professional_id
        )

        if professional is None:
            return []

        return professional.experiences