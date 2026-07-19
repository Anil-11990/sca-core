"""
Employment Type.

Represents the type of employment
for a professional experience.
"""

from enum import Enum


class EmploymentType(str, Enum):
    """
    Supported employment types.
    """

    FULL_TIME = "Full-time"
    PART_TIME = "Part-time"
    CONTRACT = "Contract"
    INTERNSHIP = "Internship"
    FREELANCE = "Freelance"