"""
Graduation Status Value Object

Tracks the completion state of an education record.
"""

from enum import Enum


class GraduationStatus(Enum):
    """
    Possible education completion states.
    """

    COMPLETED = "Completed"

    IN_PROGRESS = "In Progress"

    DROPPED = "Dropped"


    def display_name(self) -> str:
        """
        Returns readable status.
        """

        return self.value