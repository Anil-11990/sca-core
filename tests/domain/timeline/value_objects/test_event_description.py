import pytest

from app.domain.timeline.value_objects.event_description import (
    EventDescription,
)


def test_valid_description():

    description = EventDescription(
        "Completed Computer Science degree."
    )

    assert (
        str(description)
        ==
        "Completed Computer Science degree."
    )


def test_description_too_long():

    with pytest.raises(ValueError):

        EventDescription(
            "A" * 1001
        )