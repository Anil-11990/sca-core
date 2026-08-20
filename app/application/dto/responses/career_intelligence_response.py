"""
DTO:
Career Intelligence Response

Represents the output of career analysis.
"""

from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class CareerIntelligenceResponse:
    """
    Response returned after career analysis.
    """

    career_score: int
    profile_completion: int
    skill_gaps: list[str]
    career_readiness: int


    def __post_init__(self) -> None:

        if self.career_score < 0:
            raise ValueError(
                "Career score cannot be negative."
            )


        if self.profile_completion < 0:
            raise ValueError(
                "Profile completion cannot be negative."
            )


        if self.career_readiness < 0:
            raise ValueError(
                "Career readiness cannot be negative."
            )