"""
API Request Schema:
Career Analysis
"""

from pydantic import BaseModel, Field


class CareerAnalysisRequest(BaseModel):
    required_skills: list[str] = Field(
        default_factory=list
    )