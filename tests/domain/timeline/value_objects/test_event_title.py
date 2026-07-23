import pytest

from app.domain.timeline.value_objects.event_title import (
    EventTitle,
)


def test_valid_event_title():

    title = EventTitle(
        "Started Bachelor's Degree"
    )

    assert str(title) == "Started Bachelor's Degree"


def test_empty_title():

    with pytest.raises(ValueError):

        EventTitle("")


def test_title_too_long():

    with pytest.raises(ValueError):

        EventTitle("A" * 151)