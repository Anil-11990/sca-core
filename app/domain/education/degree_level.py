"""
Degree Level Value Object

Represents academic qualification level.
"""

from enum import Enum


class DegreeLevel(Enum):

    HIGH_SCHOOL = "High School"

    DIPLOMA = "Diploma"

    ASSOCIATE = "Associate Degree"

    BACHELOR = "Bachelor"

    MASTER = "Master"

    PHD = "PhD"


    def display_name(self) -> str:
        return self.value