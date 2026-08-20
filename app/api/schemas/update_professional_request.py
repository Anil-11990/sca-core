from pydantic import BaseModel


class UpdateProfessionalRequest(
    BaseModel
):
    full_name: str
    primary_goal: str