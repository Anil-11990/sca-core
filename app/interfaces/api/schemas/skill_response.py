from pydantic import BaseModel


class SkillResponse(BaseModel):
    """
    Response DTO for Skill.
    """

    id: str
    name: str