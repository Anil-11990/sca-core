"""
Achievement Types.

Represents the different categories of professional
achievements recognised by SCA.
"""

from enum import Enum


class AchievementType(str, Enum):
    """
    Supported achievement categories.
    """

    CERTIFICATION = "Certification"
    AWARD = "Award"
    PUBLICATION = "Publication"
    PATENT = "Patent"
    SCHOLARSHIP = "Scholarship"
    HACKATHON = "Hackathon"
    OPEN_SOURCE = "Open Source"
    SPEAKING = "Speaking"
    OTHER = "Other"