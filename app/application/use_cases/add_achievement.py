"""
Add Achievement Use Case.

Application service responsible for adding an Achievement
to a Professional Aggregate.

Responsibilities
----------------
- Retrieve the Professional.
- Add the Achievement.
- Persist the updated Aggregate.

Future Extensions
-----------------
- Achievement validation policies.
- Duplicate detection.
- Domain event publishing.
"""

from uuid import UUID

from app.domain.achievement.achievement import Achievement
from app.domain.professional.professional import Professional
from app.infrastructure.repositories.sqlite_professional_repository import (
    SQLiteProfessionalRepository,
)


class AddAchievement:
    """
    Adds an Achievement to a Professional.
    """

    def __init__(
        self,
        repository: SQLiteProfessionalRepository,
    ) -> None:
        self._repository = repository

    def execute(
        self,
        professional_id: UUID,
        achievement: Achievement,
    ) -> Professional:
        """
        Adds an Achievement to a Professional.
        """

        professional = self._repository.get_by_id(
            professional_id
        )

        if professional is None:
            raise ValueError(
                "Professional not found."
            )

        professional.add_achievement(
            achievement
        )

        self._repository.save(
            professional
        )

        return professional