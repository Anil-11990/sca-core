from pydantic import BaseModel


class SkillRequest(BaseModel):
    """
    Request DTO for adding a Skill.
    """

    name: str