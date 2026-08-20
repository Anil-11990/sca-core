"""
Response DTO for Project.
"""

from dataclasses import dataclass


@dataclass(slots=True, frozen=True)
class ProjectResponse:
    """
    Immutable response DTO for Project.
    """

    id: str

    name: str

    description: str

    technologies: list[str]

    repository_url: str | None

    live_url: str | None