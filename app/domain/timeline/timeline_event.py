"""
app/domain/timeline/timeline_event.py
"""

from dataclasses import dataclass
from datetime import date

from app.domain.common.entity import Entity
from app.domain.timeline.timeline_event_type import TimelineEventType
from app.domain.timeline.value_objects.event_date import EventDate
from app.domain.timeline.value_objects.event_description import EventDescription
from app.domain.timeline.value_objects.event_title import EventTitle


@dataclass(eq=False, slots=True)
class TimelineEvent(Entity):
    """
    Represents a single event in a Professional's career timeline.
    """

    title: str
    event_type: TimelineEventType
    event_date: date
    description: str = ""
    reference_id: str = ""

    def __post_init__(self):

        self.title = EventTitle(self.title)

        self.description = EventDescription(self.description)

        self.event_date = EventDate(self.event_date)