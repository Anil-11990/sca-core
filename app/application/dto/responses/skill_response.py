"""
Response DTO for Skill.
"""

from dataclasses import dataclass


@dataclass(slots=True, frozen=True)
class SkillResponse:
    """
    Immutable response DTO for Skill.
    """

    id: str

    name: str

    proficiency: str