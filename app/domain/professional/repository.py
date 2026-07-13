"""
Repository contract for Professional aggregates.

The domain depends on this abstraction rather than a concrete
database implementation.
"""

from __future__ import annotations

from abc import ABC, abstractmethod

from app.domain.common.entity import Entity
from app.domain.professional.professional import Professional


class ProfessionalRepository(ABC):
    """
    Abstract repository for Professional aggregates.
    """

    @abstractmethod
    def save(self, professional: Professional) -> None:
        """Persist a Professional."""
        raise NotImplementedError

    @abstractmethod
    def get_by_id(self, entity_id) -> Professional | None:
        """Return a Professional by its ID."""
        raise NotImplementedError