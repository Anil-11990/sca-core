"""
Tests for the Professional aggregate.

These tests define the business rules of a Professional.
"""

import pytest

from app.domain.professional.professional import Professional


def test_professional_has_name():
    """A professional stores the provided name."""

    professional = Professional(
        full_name="Anil Khanal",
        primary_goal="Build ANIrex AI"
    )

    assert professional.full_name == "Anil Khanal"


def test_name_is_trimmed():
    """Leading and trailing spaces are removed."""

    professional = Professional(
        full_name="   Anil Khanal   ",
        primary_goal="Build ANIrex AI"
    )

    assert professional.full_name == "Anil Khanal"


def test_name_cannot_be_empty():
    """Creating a professional without a name is invalid."""

    with pytest.raises(ValueError):
        Professional(
            full_name="",
            primary_goal="Founder"
        )


def test_goal_cannot_be_empty():
    """A professional must always have a goal."""

    with pytest.raises(ValueError):
        Professional(
            full_name="Anil Khanal",
            primary_goal=""
        )