"""
Simple in-memory Event Bus.

Version 1 stores published events.

Future versions will dispatch events to
handlers, AI agents, analytics, and other
parts of the system.
"""

from app.domain.events.domain_event import DomainEvent


class EventBus:
    """
    Publishes Domain Events.

    Version 1 simply stores events.
    """

    def __init__(self) -> None:
        # Stores every published event.
        self._events: list[DomainEvent] = []

    @property
    def events(self) -> tuple[DomainEvent, ...]:
        """
        Read-only view of published events.
        """
        return tuple(self._events)

    def publish(
        self,
        event: DomainEvent,
    ) -> None:
        """
        Publishes an event.

        Future versions will notify
        registered subscribers.
        """

        self._events.append(event)