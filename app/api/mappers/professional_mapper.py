"""
Professional API Mapper.

Responsible for converting Domain Professional
objects into API Response DTOs.

The route layer should not manually build
response objects.
"""

from app.domain.professional.professional import Professional

from app.api.schemas.professional_response import (
    ProfessionalResponse,
)


class ProfessionalMapper:
    """
    Converts Professional domain objects
    into API response models.
    """

    @staticmethod
    def to_response(
        professional: Professional,
    ) -> ProfessionalResponse:
        """
        Convert Domain Professional
        into ProfessionalResponse DTO.
        """

        return ProfessionalResponse(
            id=str(professional.id),
            full_name=str(professional.full_name),
            primary_goal=professional.primary_goal,
            created_at=professional.created_at,
        )