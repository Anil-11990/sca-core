"""
Tests for AchievementType.
"""

from app.domain.achievement.achievement_type import (
    AchievementType,
)


def test_certification_value():
    assert (
        AchievementType.CERTIFICATION.value
        == "Certification"
    )


def test_award_value():
    assert AchievementType.AWARD.value == "Award"


def test_publication_value():
    assert (
        AchievementType.PUBLICATION.value
        == "Publication"
    )


def test_patent_value():
    assert AchievementType.PATENT.value == "Patent"


def test_open_source_value():
    assert (
        AchievementType.OPEN_SOURCE.value
        == "Open Source"
    )