import pytest

from app.domain.goal.value_objects.goal_title import GoalTitle


def test_goal_title_stores_value():
    """
    A GoalTitle stores the provided title.
    """
    title = GoalTitle("Become AI Engineer")

    assert title.value == "Become AI Engineer"


def test_goal_title_is_trimmed():
    """
    Leading and trailing whitespace should be removed.
    """
    title = GoalTitle("   Become AI Engineer   ")

    assert title.value == "Become AI Engineer"


def test_goal_title_cannot_be_empty():
    """
    Empty titles are invalid.
    """
    with pytest.raises(ValueError):
        GoalTitle("")


def test_goal_title_cannot_be_only_spaces():
    """
    Titles containing only whitespace are invalid.
    """
    with pytest.raises(ValueError):
        GoalTitle("     ")


def test_equal_goal_titles_are_equal():
    """
    GoalTitle compares by value.
    """
    assert GoalTitle("Learn Python") == GoalTitle("Learn Python")


def test_different_goal_titles_are_not_equal():
    """
    Different values should not compare equal.
    """
    assert GoalTitle("Learn Python") != GoalTitle("Learn Rust")


def test_goal_title_has_reasonable_length():
    """
    Extremely long titles should not be allowed.
    """
    with pytest.raises(ValueError):
        GoalTitle("A" * 201)