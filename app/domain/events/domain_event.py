"""
Base class for all Domain Events.
"""

from dataclasses import dataclass, field
from datetime import UTC, datetime
from uuid import UUID, uuid4


@dataclass(frozen=True, slots=True)
class DomainEvent:
    """
    Base class for all domain events.
    """

    # These are generated automatically.
    # init=False keeps them out of the constructor,
    # allowing subclasses to define their own required fields.
    event_id: UUID = field(
        default_factory=uuid4,
        init=False
    )

    occurred_at: datetime = field(
        default_factory=lambda: datetime.now(UTC),
        init=False
    )