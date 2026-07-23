from datetime import date, timedelta

import pytest

from app.domain.timeline.value_objects.event_date import (
    EventDate,
)


def test_valid_event_date():

    event_date = EventDate(
        date.today()
    )

    assert (
        event_date.value
        == date.today()
    )


def test_future_date_not_allowed():

    with pytest.raises(ValueError):

        EventDate(
            date.today() + timedelta(days=1)
        )