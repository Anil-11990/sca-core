"""
Education Response DTO.
"""

from pydantic import BaseModel


class EducationResponse(BaseModel):

    id: str

    institution: str

    degree_level: str

    field_of_study: str

    graduation_status: str