"""
Get Achievements Use Case.

Application service responsible for retrieving every
Achievement belonging to a Professional.

Responsibilities
----------------
- Retrieve the Professional.
- Return read-only Achievements.

Future Extensions
-----------------
- Pagination.
- Filtering.
- Sorting.
"""

from uuid import UUID

from app.domain.achievement.achievement import Achievement
from app.infrastructure.repositories.sqlite_professional_repository import (
    SQLiteProfessionalRepository,
)


class GetAchievements:
    """
    Retrieves all Achievements for a Professional.
    """

    def __init__(
        self,
        repository: SQLiteProfessionalRepository,
    ) -> None:
        self._repository = repository

    def execute(
        self,
        professional_id: UUID,
    ) -> tuple[Achievement, ...]:
        """
        Returns every Achievement belonging
        to a Professional.
        """

        professional = self._repository.get_by_id(
            professional_id
        )

        if professional is None:
            raise ValueError(
                "Professional not found."
            )

        return professional.achievements