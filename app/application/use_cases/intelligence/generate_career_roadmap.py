"""
Application Use Case:
Generate Career Roadmap
"""

from uuid import UUID

from app.domain.services.career_roadmap_service import (
    CareerRoadmapService,
)

from app.exceptions.professional_not_found import (
    ProfessionalNotFoundException,
)


class GenerateCareerRoadmap:
    """
    Generates a career development roadmap
    for a Professional.
    """

    def __init__(
        self,
        repository,
        roadmap_service: CareerRoadmapService,
    ) -> None:

        self._repository = repository
        self._roadmap_service = roadmap_service

    def execute(
        self,
        professional_id: UUID,
    ) -> list[dict]:

        professional = (
            self._repository.get_by_id(
                professional_id
            )
        )

        if professional is None:
            raise ProfessionalNotFoundException(
                professional_id
            )

        return self._roadmap_service.generate(
            professional
        )