"""
Education Request DTO.
"""

from pydantic import BaseModel


class EducationRequest(BaseModel):

    institution: str

    degree_level: str

    field_of_study: str = ""

    graduation_status: str