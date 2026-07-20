"""
Professional API Routes.

Responsibilities
----------------
- Expose HTTP endpoints for Professionals.
- Delegate business logic to Application Use Cases.
- Convert Request DTOs into Domain objects.
- Convert Domain objects into Response DTOs.

The API layer MUST NOT contain business rules.
Business rules belong in the Domain layer.
"""

# =============================================================================
# Standard Library
# =============================================================================
from datetime import date
from uuid import UUID



# =============================================================================
# Third Party
# =============================================================================

from fastapi import APIRouter
from fastapi import HTTPException

from datetime import date
# =============================================================================
# Bootstrap
# =============================================================================

from app.bootstrap.container import container


# =============================================================================
# Schemas
# =============================================================================

from app.interfaces.api.schemas.professional_request import (
    ProfessionalRequest,
)

from app.interfaces.api.schemas.professional_response import (
    ProfessionalResponse,
)

from app.interfaces.api.schemas.achievement_request import (
    AchievementRequest,
)

from app.interfaces.api.schemas.achievement_response import (
    AchievementResponse,
)
from app.interfaces.api.schemas.experience_response import (
    ExperienceResponse,
)
from app.interfaces.api.schemas.experience_request import (
    ExperienceRequest,
)
# =============================================================================
# API Mappers
# =============================================================================

from app.interfaces.api.mappers.professional_mapper import (
    ProfessionalMapper,
)

from app.interfaces.api.mappers.achievement_mapper import (
    AchievementMapper,
)
from app.interfaces.api.mappers.experience_mapper import (
    ExperienceMapper,
)

# =============================================================================
# Domain
# =============================================================================

from app.domain.achievement.achievement import Achievement

from app.domain.achievement.achievement_type import (
    AchievementType,
)

from app.domain.achievement.value_objects.achievement_title import (
    AchievementTitle,
)
from app.domain.experience.value_objects.job_title import (
    JobTitle,
)

from app.domain.experience.value_objects.company_name import (
    CompanyName,
)

from app.domain.experience.value_objects.experience_period import (
    ExperiencePeriod,
)
from app.domain.experience.experience import (
    Experience,
)

from app.domain.experience.employment_type import (
    EmploymentType,
)

from app.domain.experience.experience_description import (
    ExperienceDescription,
)
from app.domain.certificate.certificate import Certificate
from app.domain.certificate.certificate_status import CertificateStatus
from app.domain.certificate.value_objects.certificate_name import (
    CertificateName,
)
from app.domain.achievement.value_objects.issuer import (
    Issuer as AchievementIssuer,
)

from app.domain.certificate.value_objects.certificate_issuer import (
    Issuer as CertificateIssuer,
)
from app.domain.certificate.value_objects.credential_id import (
    CredentialId,
)

from app.interfaces.api.schemas.certificate_request import (
    CertificateRequest,
)
from app.interfaces.api.schemas.certificate_response import (
    CertificateResponse,
)

# =============================================================================
# Router
# =============================================================================

router = APIRouter()



# =============================================================================
# Professional Endpoints
# =============================================================================


@router.post(
    "/professionals",
    response_model=ProfessionalResponse,
    status_code=201,
)
def create_professional(
    request: ProfessionalRequest,
):
    """
    Create a new Professional.
    """

    use_case = (
        container.create_professional_use_case()
    )

    professional = use_case.execute(
        full_name=request.full_name,
        primary_goal=request.primary_goal,
    )

    return ProfessionalMapper.to_response(
        professional
    )



@router.get(
    "/professionals/{professional_id}",
    response_model=ProfessionalResponse,
)
def get_professional(
    professional_id: str,
):
    """
    Retrieve a Professional by ID.
    """

    try:
        professional_uuid = UUID(
            professional_id
        )

    except ValueError:
        raise HTTPException(
            status_code=400,
            detail="Invalid UUID.",
        )


    use_case = (
        container.get_professional_use_case()
    )

    professional = use_case.execute(
        professional_uuid
    )


    if professional is None:
        raise HTTPException(
            status_code=404,
            detail="Professional not found.",
        )


    return ProfessionalMapper.to_response(
        professional
    )



# =============================================================================
# Achievement Endpoints
# =============================================================================


@router.post(
    "/professionals/{professional_id}/achievements",
    response_model=AchievementResponse,
)
def add_achievement(
    professional_id: str,
    request: AchievementRequest,
):
    """
    Add an Achievement to a Professional.
    """


    try:
        professional_uuid = UUID(
            professional_id
        )

    except ValueError:
        raise HTTPException(
            status_code=400,
            detail="Invalid UUID.",
        )


    use_case = (
        container.add_achievement_use_case()
    )

    # Convert the incoming string into an AchievementType.

    achievement_lookup = {
        # Certification
        "certificate": AchievementType.CERTIFICATION,
        "certification": AchievementType.CERTIFICATION,
        "certified": AchievementType.CERTIFICATION,

        # Award
        "award": AchievementType.AWARD,

        # Publication
        "publication": AchievementType.PUBLICATION,

        # Patent
        "patent": AchievementType.PATENT,

        # Scholarship
        "scholarship": AchievementType.SCHOLARSHIP,

        # Hackathon
        "hackathon": AchievementType.HACKATHON,

        # Open Source
        "open_source": AchievementType.OPEN_SOURCE,
        "open source": AchievementType.OPEN_SOURCE,

        # Speaking
        "speaking": AchievementType.SPEAKING,

        # Other
        "other": AchievementType.OTHER,
    }

    achievement_type = achievement_lookup.get(
        request.achievement_type.lower().strip()
    )

    if achievement_type is None:
        raise HTTPException(
            status_code=400,
            detail="Invalid achievement type.",
        )

    achievement = Achievement(
        title=AchievementTitle(request.title),
        issuer=AchievementIssuer(
            request.issuer
        ),
        achievement_type=achievement_type,
        description=request.description,
        credential_url=request.credential_url,
    )


    professional = use_case.execute(
        professional_uuid,
        achievement,
    )


    if professional is None:
        raise HTTPException(
            status_code=404,
            detail="Professional not found.",
        )


    return AchievementMapper.to_response(
        achievement
    )



@router.get(
    "/professionals/{professional_id}/achievements",
    response_model=list[AchievementResponse],
)
def get_achievements(
    professional_id: str,
):
    """
    Retrieve every Achievement
    belonging to a Professional.
    """


    try:
        professional_uuid = UUID(
            professional_id
        )

    except ValueError:
        raise HTTPException(
            status_code=400,
            detail="Invalid UUID.",
        )


    use_case = (
        container.get_achievements_use_case()
    )


    achievements = use_case.execute(
        professional_uuid
    )


    return [
        AchievementMapper.to_response(
            achievement
        )

        for achievement in achievements
    ]
@router.post(
    "/professionals/{professional_id}/certificates",
    response_model=CertificateResponse,
)
def add_certificate(
    professional_id: str,
    request: CertificateRequest,
):
    """
    Add a Certificate to a Professional.
    """

    try:
        professional_uuid = UUID(
            professional_id
        )
    except ValueError:
        raise HTTPException(
            status_code=400,
            detail="Invalid UUID.",
        )

    status_lookup = {
        "active": CertificateStatus.ACTIVE,
        "expired": CertificateStatus.EXPIRED,
        "revoked": CertificateStatus.REVOKED,
    }

    status = status_lookup.get(
        request.status.lower()
    )

    if status is None:
        raise HTTPException(
            status_code=400,
            detail="Invalid certificate status.",
        )

    certificate = Certificate(
        name=CertificateName(
            request.name
        ),
        issuer=CertificateIssuer(request.issuer),
        credential_id=CredentialId(
            request.credential_id
        ),
        issued_date=date.today(),
        expiry_date=None,
        verification_url=request.credential_url,
        status=status,
    )

    use_case = (
        container.add_certificate_use_case()
    )

    professional = use_case.execute(
        professional_uuid,
        certificate,
    )

    if professional is None:
        raise HTTPException(
            status_code=404,
            detail="Professional not found.",
        )

    return CertificateResponse(
        id=str(certificate.id),
        name=str(certificate.name),
        issuer=str(certificate.issuer),
        credential_id=str(
            certificate.credential_id
        ),
        credential_url=certificate.verification_url,
        status=certificate.status.value,
        issued_at=certificate.issued_date,
    )
@router.get(
    "/professionals/{professional_id}/certificates",
    response_model=list[CertificateResponse],
)
def get_certificates(
    professional_id: str,
):
    """
    Retrieve certificates belonging
    to a Professional.
    """

    try:
        professional_uuid = UUID(
            professional_id
        )
    except ValueError:
        raise HTTPException(
            status_code=400,
            detail="Invalid UUID.",
        )

    use_case = (
        container.get_certificates_use_case()
    )

    certificates = use_case.execute(
        professional_uuid
    )

    return [
        CertificateResponse(
            id=str(item.id),
            name=str(item.name),
            issuer=str(item.issuer),
            credential_id=str(item.credential_id),
            credential_url=item.verification_url,
            status=item.status.value,
            issued_at=item.issued_date,
        )
        for item in certificates
    ]
@router.post(
    "/professionals/{professional_id}/experiences",
    response_model=ExperienceResponse,
)
def add_experience(
    professional_id: str,
    request: ExperienceRequest,
):
    """
    Add an Experience to a Professional.
    """

    try:
        professional_uuid = UUID(
            professional_id
        )

    except ValueError:

        raise HTTPException(
            status_code=400,
            detail="Invalid UUID.",
        )

    employment_lookup = {

        "full_time": EmploymentType.FULL_TIME,
        "part_time": EmploymentType.PART_TIME,
        "contract": EmploymentType.CONTRACT,
        "internship": EmploymentType.INTERNSHIP,
        "freelance": EmploymentType.FREELANCE,
        "volunteer": EmploymentType.VOLUNTEER,
    }

    employment_type = employment_lookup.get(
        request.employment_type.lower()
    )

    if employment_type is None:

        raise HTTPException(
            status_code=400,
            detail="Invalid employment type.",
        )

    period = ExperiencePeriod(
        start_date=date.fromisoformat(
            request.start_date
        ),
        end_date=(
            date.fromisoformat(
                request.end_date
            )
            if request.end_date
            else None
        ),
    )

    experience = Experience(

        job_title=JobTitle(
            request.job_title
        ),

        company_name=CompanyName(
            request.company_name
        ),

        employment_type=employment_type,

        experience_period=period,

        description=ExperienceDescription(
            request.description
        ),
    )

    use_case = (
        container.add_experience_use_case()
    )

    professional = use_case.execute(
        professional_uuid,
        experience,
    )

    if professional is None:

        raise HTTPException(
            status_code=404,
            detail="Professional not found.",
        )

    return ExperienceMapper.to_response(
        experience
    )
@router.get(
    "/professionals/{professional_id}/experiences",
    response_model=list[ExperienceResponse],
)
def get_experiences(
    professional_id: str,
):
    """
    Retrieve every Experience
    belonging to a Professional.
    """

    try:

        professional_uuid = UUID(
            professional_id
        )

    except ValueError:

        raise HTTPException(
            status_code=400,
            detail="Invalid UUID.",
        )

    use_case = (
        container.get_experiences_use_case()
    )

    experiences = use_case.execute(
        professional_uuid
    )

    return [

        ExperienceMapper.to_response(
            experience
        )

        for experience in experiences
    ]