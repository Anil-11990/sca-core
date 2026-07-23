"""
Response DTO for Education.
"""

from dataclasses import dataclass


@dataclass(slots=True, frozen=True)
class EducationResponse:

    id: str

    institution: str

    degree_level: str

    field_of_study: str

    graduation_status: str