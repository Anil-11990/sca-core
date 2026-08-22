"""
API Response Schema:
Career Roadmap
"""

from pydantic import BaseModel


class CareerRoadmapItemSchema(BaseModel):

    skill: str
    priority: str
    stage: str