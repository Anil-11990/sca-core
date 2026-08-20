"""
Education API Routes.

Responsibilities
-----------------
- Expose Education endpoints.
- Convert API requests into domain objects.
- Delegate logic to application use cases.
- Convert domain objects into response DTOs.

No business rules belong here.
"""

from uuid import UUID

from fastapi import APIRouter, HTTPException

from app.bootstrap.container import container


# ============================================================================
# Schemas
# ============================================================================

from app.api.schemas.education_request import (
    EducationRequest,
)


# ============================================================================
# Mapper
# ============================================================================

from app.api.mappers.education_mapper import (
    EducationMapper,
)


# ============================================================================
# Domain
# ============================================================================

from app.domain.education.education import Education

from app.domain.education.degree_level import (
    DegreeLevel,
)

from app.domain.education.graduation_status import (
    GraduationStatus,
)


# ============================================================================

router = APIRouter(
    prefix="/education",
    tags=["Education"],
)


# ============================================================================
# ADD EDUCATION
# ============================================================================


@router.post(
    "/{professional_id}",
)
def add_education(
    professional_id: UUID,
    request: EducationRequest,
):
    """
    Add education record to Professional.
    """


    education = Education(
        institution=request.institution,

        degree_level=DegreeLevel(
            request.degree_level
        ),

        field_of_study=request.field_of_study,

        graduation_status=GraduationStatus(
            request.graduation_status
        ),
    )


    professional = (
        container
        .add_education_use_case()
        .execute(
            professional_id,
            education,
        )
    )


    if professional is None:
        raise HTTPException(
            status_code=404,
            detail="Professional not found",
        )


    return EducationMapper.to_response(
        education
    )



# ============================================================================
# GET EDUCATION
# ============================================================================


@router.get(
    "/{professional_id}",
)
def get_education(
    professional_id: UUID,
):
    """
    Retrieve all education records
    belonging to Professional.
    """


    educations = (
        container
        .get_education_use_case()
        .execute(
            professional_id
        )
    )


    return [

        EducationMapper.to_response(
            education
        )

        for education in educations

    ]



# ============================================================================
# REMOVE EDUCATION
# ============================================================================


@router.delete(
    "/{professional_id}/{education_id}",
)
def remove_education(
    professional_id: UUID,
    education_id: UUID,
):
    """
    Remove education record.
    """


    professional = (
        container
        .remove_education_use_case()
        .execute(
            professional_id,
            education_id,
        )
    )


    if professional is None:
        raise HTTPException(
            status_code=404,
            detail="Education not found",
        )


    return {
        "message": "Education removed successfully"
    }



# ============================================================================
# UPDATE EDUCATION
# ============================================================================


@router.patch(
    "/{professional_id}/{education_id}",
)
def update_education(
    professional_id: UUID,
    education_id: UUID,
    request: EducationRequest,
):
    """
    Update education record.
    """

    education = Education(
        institution=request.institution,
        degree_level=DegreeLevel(
            request.degree_level
        ),
        field_of_study=request.field_of_study,
        graduation_status=GraduationStatus(
            request.graduation_status
        ),
    )

    education.id = education_id


    professional = (
        container
        .update_education_use_case()
        .execute(
            professional_id,
            education,
        )
    )


    if professional is None:
        raise HTTPException(
            status_code=404,
            detail="Professional not found",
        )


    return EducationMapper.to_response(
        education
    )