"""
Project Request DTO.
"""

from pydantic import BaseModel


class ProjectRequest(BaseModel):

    name: str

    description: str = ""

    repository_url: str = ""

    live_url: str = ""

    technologies: list[str] = []