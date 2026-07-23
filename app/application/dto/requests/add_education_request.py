"""
Request DTO for adding Education.
"""

from dataclasses import dataclass


@dataclass(slots=True, frozen=True)
class AddEducationRequest:

    professional_id: str

    institution: str

    degree_level: str

    field_of_study: str

    graduation_status: str