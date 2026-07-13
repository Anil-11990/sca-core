"""
API Routes.

This module defines the HTTP endpoints exposed by the SCA API.

Responsibilities:
- Receive HTTP requests.
- Validate incoming data.
- Call the appropriate Application Use Case.
- Convert domain objects into API responses.
"""

from uuid import UUID

from fastapi import APIRouter, HTTPException

from app.bootstrap.container import container
from app.interfaces.api.models.professional_request import (
    CreateProfessionalRequest,
)
from app.interfaces.api.models.professional_response import (
    ProfessionalResponse,
)

# -----------------------------------------------------------------------------
# FastAPI Router
# -----------------------------------------------------------------------------

router = APIRouter()

# -----------------------------------------------------------------------------
# Create Professional
# -----------------------------------------------------------------------------


@router.post(
    "/professionals",
    response_model=ProfessionalResponse,
    status_code=201,
)
def create_professional(
    request: CreateProfessionalRequest,
) -> ProfessionalResponse:
    """
    Creates a new Professional.
    """

    use_case = container.create_professional_use_case()

    professional = use_case.execute(
        full_name=request.full_name,
        primary_goal=request.primary_goal,
    )

    return ProfessionalResponse(
        id=str(professional.id),
        full_name=str(professional.full_name),
        primary_goal=professional.primary_goal,
    )


# -----------------------------------------------------------------------------
# Get Professional
# -----------------------------------------------------------------------------


@router.get(
    "/professionals/{professional_id}",
    response_model=ProfessionalResponse,
)
def get_professional(
    professional_id: str,
) -> ProfessionalResponse:
    """
    Retrieves a Professional by UUID.
    """

    # Convert the incoming string into a UUID.
    try:
        professional_uuid = UUID(professional_id)
    except ValueError:
        raise HTTPException(
            status_code=400,
            detail="Invalid UUID format.",
        )

    use_case = container.get_professional_use_case()

    professional = use_case.execute(professional_uuid)

    if professional is None:
        raise HTTPException(
            status_code=404,
            detail="Professional not found.",
        )

    return ProfessionalResponse(
        id=str(professional.id),
        full_name=str(professional.full_name),
        primary_goal=professional.primary_goal,
    )