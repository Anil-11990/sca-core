"""
Response DTO for Project.
"""

from dataclasses import dataclass


@dataclass(slots=True, frozen=True)
class ProjectResponse:

    id: str

    project_name: str

    description: str

    repository_url: str

    live_demo_url: str