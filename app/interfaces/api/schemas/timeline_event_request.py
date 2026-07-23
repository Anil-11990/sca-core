"""
Timeline Event Request Schema.

Used when creating a timeline event through API.
"""

from datetime import date

from pydantic import BaseModel


class TimelineEventRequest(BaseModel):
    """
    Incoming timeline event data.
    """

    title: str

    event_type: str

    event_date: date

    description: str = ""

    reference_id: str = ""