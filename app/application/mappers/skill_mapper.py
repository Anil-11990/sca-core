from app.domain.skill.skill import Skill
from app.application.dto.responses.skill_response import SkillResponse


class SkillMapper:
    """
    Maps Skill domain entity to SkillResponse DTO.
    """

    @staticmethod
    def to_response(skill: Skill) -> SkillResponse:

        return SkillResponse(
            id=str(skill.id),
            name=str(skill.name),
            proficiency=skill.proficiency.value
            if hasattr(skill.proficiency, "value")
            else str(skill.proficiency),
        )