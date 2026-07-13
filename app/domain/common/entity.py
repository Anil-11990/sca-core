"""
Base Entity for all Domain objects.

Every Entity automatically receives
a globally unique identifier (UUID).

The ID is generated internally and is
never supplied manually.
"""

from dataclasses import dataclass, field
from uuid import UUID, uuid4


@dataclass(eq=False, slots=True)
class Entity:
    """
    Base class for all entities.

    Every entity receives an immutable UUID
    when created.
    """

    # Automatically generated unique identifier.
    # init=False means developers never pass it manually.
    id: UUID = field(default_factory=uuid4, init=False)

    def __eq__(self, other):
        return (
            isinstance(other, Entity)
            and self.id == other.id
        )

    def __hash__(self):
        return hash(self.id)