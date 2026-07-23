"""
Response DTO for Professional.
"""

from dataclasses import dataclass


@dataclass(slots=True, frozen=True)
class ProfessionalResponse:

    id: str

    full_name: str

    primary_goal: str

    current_title: str

    location: str