"""
Response DTO for Timeline Event.
"""

from dataclasses import dataclass
from datetime import date


@dataclass(slots=True, frozen=True)
class TimelineEventResponse:

    id: str

    title: str

    event_type: str

    event_date: date

    description: str

    reference_id: str