"""
Experience API Routes.

Responsibilities
-----------------
- Expose Experience endpoints.
- Convert API requests into domain objects.
- Delegate logic to use cases.
- Convert domain objects into responses.

No business rules belong here.
"""

from uuid import UUID

from fastapi import APIRouter, HTTPException

from app.bootstrap.container import container


# ============================================================================
# Schemas
# ============================================================================

from app.api.schemas.experience_request import (
    ExperienceRequest,
)


# ============================================================================
# Mapper
# ============================================================================

from app.api.mappers.experience_mapper import (
    ExperienceMapper,
)


# ============================================================================
# Domain
# ============================================================================

from app.domain.experience.experience import (
    Experience,
)

from app.domain.experience.value_objects.job_title import (
    JobTitle,
)

from app.domain.experience.value_objects.company_name import (
    CompanyName,
)

from app.domain.experience.employment_type import (
    EmploymentType,
)

from app.domain.experience.value_objects.experience_period import (
    ExperiencePeriod,
)

from app.domain.experience.experience_description import (
    ExperienceDescription,
)



router = APIRouter(
    prefix="/experiences",
    tags=["Experiences"],
)



# ============================================================================
# ADD EXPERIENCE
# ============================================================================


@router.post(
    "/{professional_id}",
)
def add_experience(
    professional_id: UUID,
    request: ExperienceRequest,
):
    """
    Add experience to Professional.
    """


    experience = Experience(

        job_title=JobTitle(
            request.job_title
        ),

        company_name=CompanyName(
            request.company_name
        ),

        employment_type=EmploymentType(
            request.employment_type
        ),

        experience_period=ExperiencePeriod(
            start_date=request.start_date,
            end_date=request.end_date,
        ),

        description=ExperienceDescription(
            request.description
        ),
    )


    professional = (
        container
        .add_experience_use_case()
        .execute(
            professional_id,
            experience,
        )
    )


    if professional is None:

        raise HTTPException(
            status_code=404,
            detail="Professional not found",
        )


    return ExperienceMapper.to_response(
        experience
    )



# ============================================================================
# GET EXPERIENCES
# ============================================================================


@router.get(
    "/{professional_id}",
)
def get_experiences(
    professional_id: UUID,
):
    """
    Get all experiences of Professional.
    """


    experiences = (
        container
        .get_experiences_use_case()
        .execute(
            professional_id
        )
    )


    return [

        ExperienceMapper.to_response(
            experience
        )

        for experience in experiences

    ]



# ============================================================================
# REMOVE EXPERIENCE
# ============================================================================


@router.delete(
    "/{professional_id}/{experience_id}",
)
def remove_experience(
    professional_id: UUID,
    experience_id: UUID,
):
    """
    Remove experience from Professional.
    """


    professional = (
        container
        .remove_experience_use_case()
        .execute(
            professional_id,
            experience_id,
        )
    )


    if professional is None:

        raise HTTPException(
            status_code=404,
            detail="Experience not found",
        )


    return {
        "message": "Experience removed successfully"
    }



# ============================================================================
# UPDATE EXPERIENCE
# ============================================================================


@router.patch(
    "/{professional_id}/{experience_id}",
)
def update_experience(
    professional_id: UUID,
    experience_id: UUID,
    request: ExperienceRequest,
):
    """
    Update experience.
    """


    experience = Experience(

        job_title=JobTitle(
            request.job_title
        ),

        company_name=CompanyName(
            request.company_name
        ),

        employment_type=EmploymentType(
            request.employment_type
        ),

        experience_period=ExperiencePeriod(
            start_date=request.start_date,
            end_date=request.end_date,
        ),

        description=ExperienceDescription(
            request.description
        ),
    )


    experience.id = experience_id

    updated_experience = (
        container
        .update_experience_use_case()
        .execute(
            professional_id,
            experience,
        )
    )


    if updated_experience is None:

        raise HTTPException(
            status_code=404,
            detail="Professional not found",
        )

    return ExperienceMapper.to_response(
        updated_experience
    )