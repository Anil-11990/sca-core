"""
Response DTO for Skill.
"""

from dataclasses import dataclass


@dataclass(slots=True, frozen=True)
class SkillResponse:

    id: str

    skill_name: str

    proficiency: str