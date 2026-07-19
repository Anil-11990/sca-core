"""
Tests for AchievementTitle.
"""

import pytest

from app.domain.achievement.value_objects.achievement_title import (
    AchievementTitle,
)


def test_create_title():
    title = AchievementTitle("AWS Certified")

    assert str(title) == "AWS Certified"


def test_title_is_trimmed():
    title = AchievementTitle("  AWS Certified  ")

    assert str(title) == "AWS Certified"


def test_empty_title_raises_error():
    with pytest.raises(ValueError):
        AchievementTitle("")


def test_whitespace_title_raises_error():
    with pytest.raises(ValueError):
        AchievementTitle("     ")