"""
Response DTO for Goal.
"""

from dataclasses import dataclass


@dataclass(slots=True, frozen=True)
class GoalResponse:

    id: str

    title: str

    status: str