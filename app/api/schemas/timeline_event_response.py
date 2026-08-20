"""
Timeline Event Response Schema.

Returned by API.
"""

from datetime import date

from pydantic import BaseModel


class TimelineEventResponse(BaseModel):
    """
    Timeline event API response.
    """

    id: str

    title: str

    event_type: str

    event_date: date

    description: str

    reference_id: str