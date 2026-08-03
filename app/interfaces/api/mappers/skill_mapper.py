from app.domain.skill.skill import Skill
from app.interfaces.api.schemas.skill_response import (
    SkillResponse,
)


class SkillMapper:
    """
    Converts Skill domain objects into API responses.
    """

    @staticmethod
    def to_response(
        skill: Skill,
    ) -> SkillResponse:

        return SkillResponse(
            id=str(skill.id),
            name=skill.name,
        )