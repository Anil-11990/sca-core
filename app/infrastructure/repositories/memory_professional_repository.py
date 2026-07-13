"""
In-memory implementation of the Professional Repository.

Used for testing and early development.
"""

from app.domain.professional.professional import Professional
from app.domain.professional.repository import ProfessionalRepository


class MemoryProfessionalRepository(ProfessionalRepository):

    def __init__(self) -> None:
        self._storage: dict = {}

    def save(self, professional: Professional) -> None:
        self._storage[professional.id] = professional

    def get_by_id(self, entity_id):
        return self._storage.get(entity_id)