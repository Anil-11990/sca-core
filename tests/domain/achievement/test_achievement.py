"""
Tests for the Achievement entity.
"""

from app.domain.achievement.achievement import Achievement
from app.domain.achievement.achievement_type import AchievementType
from app.domain.achievement.value_objects.achievement_title import (
    AchievementTitle,
)
from app.domain.achievement.value_objects.issuer import Issuer


def test_create_achievement():
    """
    A valid Achievement should be created successfully.
    """

    achievement = Achievement(
        title=AchievementTitle("AWS Certified Developer"),
        issuer=Issuer("Amazon Web Services"),
        achievement_type=AchievementType.CERTIFICATION,
    )

    assert achievement.title == AchievementTitle(
        "AWS Certified Developer"
    )

    assert achievement.issuer == Issuer(
        "Amazon Web Services"
    )

    assert (
        achievement.achievement_type
        == AchievementType.CERTIFICATION
    )


def test_description_defaults_to_empty():
    """
    Description should default to an empty string.
    """

    achievement = Achievement(
        title=AchievementTitle("Winner"),
        issuer=Issuer("Hackathon"),
        achievement_type=AchievementType.HACKATHON,
    )

    assert achievement.description == ""


def test_credential_url_defaults_to_empty():
    """
    Credential URL should default to an empty string.
    """

    achievement = Achievement(
        title=AchievementTitle("Winner"),
        issuer=Issuer("Hackathon"),
        achievement_type=AchievementType.HACKATHON,
    )

    assert achievement.credential_url == ""


def test_description_is_trimmed():
    """
    Description should be stripped of whitespace.
    """

    achievement = Achievement(
        title=AchievementTitle("Winner"),
        issuer=Issuer("Hackathon"),
        achievement_type=AchievementType.HACKATHON,
        description="  National Finalist  ",
    )

    assert achievement.description == "National Finalist"


def test_credential_url_is_trimmed():
    """
    Credential URL should be stripped of whitespace.
    """

    achievement = Achievement(
        title=AchievementTitle("Winner"),
        issuer=Issuer("Hackathon"),
        achievement_type=AchievementType.HACKATHON,
        credential_url="  https://example.com  ",
    )

    assert (
        achievement.credential_url
        == "https://example.com"
    )