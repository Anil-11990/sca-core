"""
DTO:
Analyze Career Request

Carries input data required
for career analysis.
"""

from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class AnalyzeCareerRequest:
    """
    Request object for career analysis.
    """

    professional_id: str
    required_skills: list[str]


    def __post_init__(self) -> None:

        if not self.professional_id:
            raise ValueError(
                "Professional ID cannot be empty."
            )


        if self.required_skills is None:
            raise ValueError(
                "Required skills cannot be None."
            )