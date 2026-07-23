"""
Request DTO for creating a Professional.
"""

from dataclasses import dataclass


@dataclass(slots=True, frozen=True)
class CreateProfessionalRequest:
    """
    Request data required to create a Professional.
    """

    full_name: str
    primary_goal: str