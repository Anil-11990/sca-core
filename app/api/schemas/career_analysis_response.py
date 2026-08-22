"""
API Response Schema:
Career Analysis
"""

from pydantic import BaseModel, Field


class CareerAnalysisResponse(BaseModel):

    career_score: int = Field(..., ge=0)

    profile_completion: int = Field(..., ge=0)

    skill_gaps: list[str]

    career_readiness: int = Field(..., ge=0)