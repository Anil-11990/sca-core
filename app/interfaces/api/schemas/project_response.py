"""
Project Response DTO.
"""

from pydantic import BaseModel


class ProjectResponse(BaseModel):

    id: str

    name: str

    description: str

    repository_url: str

    live_url: str

    technologies: list[str]