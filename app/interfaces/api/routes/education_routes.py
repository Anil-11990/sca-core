"""
Education API Routes.

Handles education operations
for Professional aggregate.
"""

from fastapi import APIRouter, HTTPException

from app.bootstrap.container import container

from app.interfaces.api.schemas.education_request import (
    EducationRequest,
)

from app.interfaces.api.mappers.education_mapper import (
    EducationMapper,
)

from app.domain.education.education import Education

from app.domain.education.degree_level import (
    DegreeLevel,
)

from app.domain.education.graduation_status import (
    GraduationStatus,
)


router = APIRouter()


repository = container.professional_repository


@router.post(
    "/professionals/{professional_id}/education"
)
def add_education(
    professional_id: str,
    request: EducationRequest,
):

    professional = repository.get(
        professional_id
    )

    if not professional:
        raise HTTPException(
            status_code=404,
            detail="Professional not found",
        )


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


    professional.add_education(
        education
    )

    repository.save(
        professional
    )


    return EducationMapper.to_response(
        education
    )


@router.get(
    "/professionals/{professional_id}/education"
)
def get_education(
    professional_id: str,
):

    professional = repository.get(
        professional_id
    )

    if not professional:
        raise HTTPException(
            status_code=404,
            detail="Professional not found",
        )


    return [
        EducationMapper.to_response(
            education
        )
        for education
        in professional.educations
    ]