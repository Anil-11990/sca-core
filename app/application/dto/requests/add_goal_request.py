"""
Request DTO for adding a Goal.
"""

from dataclasses import dataclass


@dataclass(slots=True, frozen=True)
class AddGoalRequest:

    professional_id: str

    title: str