"""
Request DTO for adding a Skill.
"""

from dataclasses import dataclass


@dataclass(slots=True, frozen=True)
class AddSkillRequest:

    professional_id: str

    skill_name: str

    proficiency: str