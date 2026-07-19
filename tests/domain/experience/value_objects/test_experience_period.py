from datetime import date

from app.domain.experience.value_objects.experience_period import (
    ExperiencePeriod,
)


def test_create_experience_period():
    period = ExperiencePeriod(
        start_date=date(2024, 1, 1),
        end_date=date(2025, 1, 1),
    )

    assert period.start_date == date(2024, 1, 1)
    assert period.end_date == date(2025, 1, 1)


def test_current_experience_has_no_end_date():
    period = ExperiencePeriod(
        start_date=date(2024, 1, 1),
        end_date=None,
    )

    assert period.end_date is None