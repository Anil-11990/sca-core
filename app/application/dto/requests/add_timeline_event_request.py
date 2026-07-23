"""
Request DTO for adding Timeline Event.
"""

from dataclasses import dataclass
from datetime import date


@dataclass(slots=True, frozen=True)
class AddTimelineEventRequest:

    professional_id: str

    title: str

    event_type: str

    event_date: date

    description: str = ""

    reference_id: str = ""