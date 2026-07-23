"""
In-Memory Professional Repository.

Responsibilities
----------------
- Store Professional aggregates.
- Retrieve Professional aggregates.
- Raise domain exceptions instead of returning None.
"""

from app.domain.professional.professional import Professional
from app.domain.repositories.professional_repository import (
    ProfessionalRepository,
)

from app.exceptions.professional_not_found import (
    ProfessionalNotFoundException,
)


class MemoryProfessionalRepository(
    ProfessionalRepository,
):
    """
    In-memory implementation of the Professional Repository.

    Used for:
    - Development
    - Unit Tests

    Later replaced by SQLite/PostgreSQL implementation.
    """

    def __init__(self) -> None:
        self._professionals: dict = {}

    # ==========================================================
    # Save
    # ==========================================================

    def save(
        self,
        professional: Professional,
    ) -> None:
        """
        Save or update a Professional.
        """

        self._professionals[
            professional.id
        ] = professional

    # ==========================================================
    # Get
    # ==========================================================

    def get_by_id(
        self,
        professional_id,
    ) -> Professional:
        """
        Retrieve a Professional.

        Raises
        ------
        ProfessionalNotFoundException
            If the Professional does not exist.
        """

        professional = self._professionals.get(
            professional_id
        )

        if professional is None:
            raise ProfessionalNotFoundException(
                professional_id
            )

        return professional

    # ==========================================================
    # Exists
    # ==========================================================

    def exists(
        self,
        professional_id,
    ) -> bool:
        """
        Check whether a Professional exists.
        """

        return (
            professional_id
            in self._professionals
        )

    # ==========================================================
    # Delete
    # ==========================================================

    def delete(
        self,
        professional_id,
    ) -> None:
        """
        Remove a Professional.
        """

        if (
            professional_id
            not in self._professionals
        ):
            raise ProfessionalNotFoundException(
                professional_id
            )

        del self._professionals[
            professional_id
        ]