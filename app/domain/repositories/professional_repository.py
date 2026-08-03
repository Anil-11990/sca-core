"""
Professional Repository Contract.

Defines the persistence operations required by the
Application layer.

Infrastructure implementations such as SQLite,
Memory or PostgreSQL repositories must implement
this interface.
"""

from abc import ABC
from abc import abstractmethod
from uuid import UUID

from app.domain.professional.professional import Professional


class ProfessionalRepository(ABC):
    """
    Abstract repository for Professional aggregates.
    """

    @abstractmethod
    def save(
        self,
        professional: Professional,
    ) -> None:
        """
        Persist a Professional aggregate.
        """
        raise NotImplementedError

    @abstractmethod
    def get_by_id(
        self,
        professional_id: UUID,
    ) -> Professional | None:
        """
        Retrieve a Professional by ID.
        """
        raise NotImplementedError
    @abstractmethod
    def delete(
        self,
        professional_id: UUID,
    ) -> None:
        """
        Delete a Professional aggregate.
        """
        raise NotImplementedError