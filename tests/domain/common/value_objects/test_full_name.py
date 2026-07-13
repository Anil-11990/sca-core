import pytest

from app.domain.common.value_objects.full_name import FullName


def test_full_name_value_is_stored():
    """
    A FullName object should store the provided value.
    """
    name = FullName("Anil Khanal")

    assert name.value == "Anil Khanal"


def test_full_name_is_trimmed():
    """
    Leading and trailing whitespace should be removed.
    """
    name = FullName("   Anil Khanal   ")

    assert name.value == "Anil Khanal"


def test_full_name_cannot_be_empty():
    """
    Empty names are invalid.
    """
    with pytest.raises(ValueError):
        FullName("")


def test_full_name_cannot_contain_only_spaces():
    """
    A name made only of spaces is invalid.
    """
    with pytest.raises(ValueError):
        FullName("      ")


def test_two_equal_names_are_equal():
    """
    Value Objects compare by value.
    """
    assert FullName("Anil Khanal") == FullName("Anil Khanal")


def test_two_different_names_are_not_equal():
    """
    Different values should not compare equal.
    """
    assert FullName("Anil") != FullName("Khanal")