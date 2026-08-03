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

from app.exceptions.professional_not_found import (
    ProfessionalNotFoundException,
)

# =============================================================================
# Third Party
# =============================================================================

from fastapi import APIRouter
from fastapi import HTTPException
# =============================================================================
# Bootstrap
# =============================================================================

from app.bootstrap.container import container

# =============================================================================
# API Schemas
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

from app.interfaces.api.schemas.certificate_request import (
    CertificateRequest,
)
from app.interfaces.api.schemas.certificate_response import (
    CertificateResponse,
)

from app.interfaces.api.schemas.experience_request import (
    ExperienceRequest,
)
from app.interfaces.api.schemas.experience_response import (
    ExperienceResponse,
)

from app.interfaces.api.schemas.project_request import (
    ProjectRequest,
)
from app.interfaces.api.schemas.project_response import (
    ProjectResponse,
)
from app.interfaces.api.routes.education_routes import router as education_router
# =============================================================================
# API Mappers
# =============================================================================

from app.interfaces.api.mappers.professional_mapper import (
    ProfessionalMapper,
)
from fastapi import Response

from app.interfaces.api.mappers.achievement_mapper import (
    AchievementMapper,
)

from app.interfaces.api.mappers.experience_mapper import (
    ExperienceMapper,
)

from app.interfaces.api.mappers.project_mapper import (
    ProjectMapper,
)
from app.interfaces.api.schemas.skill_request import (
    SkillRequest,
)

from app.interfaces.api.schemas.skill_response import (
    SkillResponse,
)

from app.interfaces.api.mappers.skill_mapper import (
    SkillMapper,
)

from app.domain.skill.skill import Skill
# =============================================================================
# Domain - Achievement
# =============================================================================

from app.domain.achievement.achievement import (
    Achievement,
)

from app.domain.achievement.achievement_type import (
    AchievementType,
)

from app.domain.achievement.value_objects.achievement_title import (
    AchievementTitle,
)
from app.exceptions.professional_not_found import (
    ProfessionalNotFoundException,
)

from app.domain.achievement.value_objects.issuer import (
    Issuer as AchievementIssuer,
)

# =============================================================================
# Domain - Certificate
# =============================================================================

from app.domain.certificate.certificate import (
    Certificate,
)

from app.domain.certificate.certificate_status import (
    CertificateStatus,
)

from app.domain.certificate.value_objects.certificate_name import (
    CertificateName,
)

from app.domain.certificate.value_objects.certificate_issuer import (
    Issuer as CertificateIssuer,
)

from app.domain.certificate.value_objects.credential_id import (
    CredentialId,
)

# =============================================================================
# Domain - Experience
# =============================================================================

from app.domain.experience.experience import (
    Experience,
)

from app.domain.experience.employment_type import (
    EmploymentType,
)

from app.domain.experience.experience_description import (
    ExperienceDescription,
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

# =============================================================================
# Domain - Project
# =============================================================================

from app.domain.project.project import (
    Project,
)

from app.domain.project.value_objects.project_name import (
    ProjectName,
)
from app.interfaces.api.schemas.update_professional_request import (
    UpdateProfessionalRequest,
)
# =============================================================================
# Router
# =============================================================================

router = APIRouter()

router.include_router(
    education_router
)


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

    use_case = container.create_professional_use_case()

    professional = use_case.execute(
        full_name=request.full_name,
        primary_goal=request.primary_goal,
    )

    return ProfessionalResponse(
        id=str(professional.id),
        full_name=str(professional.full_name),
        primary_goal=professional.primary_goal,
        created_at=professional.created_at,
    )

@router.get(
    "/professionals/{professional_id}",
    response_model=ProfessionalResponse,
)
def get_professional(
    professional_id: str,
):
    """
    Retrieve a Professional.
    """

    try:
        professional_uuid = UUID(professional_id)
    except ValueError:
        raise HTTPException(
            status_code=400,
            detail="Invalid UUID format.",
        )

    use_case = container.get_professional_use_case()

    try:
        professional = use_case.execute(
            professional_uuid
        )
    except ProfessionalNotFoundException:
        raise HTTPException(
            status_code=404,
            detail="Professional not found.",
        )

    return ProfessionalResponse(
        id=str(professional.id),
        full_name=str(professional.full_name),
        primary_goal=professional.primary_goal,
        created_at=professional.created_at,
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
        issuer=CertificateIssuer(
            request.issuer
        ),
        credential_id=CredentialId(
            request.credential_id
        ),
        issued_date=request.issued_date,
        expiry_date=request.expiry_date,
        verification_url=request.verification_url,
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
        credential_id=str(certificate.credential_id),
        issued_date=certificate.issued_date,
        expiry_date=certificate.expiry_date,
        verification_url=certificate.verification_url,
        status=certificate.status.value,
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
            issued_date=item.issued_date,
            expiry_date=item.expiry_date,
            verification_url=item.verification_url,
            status=item.status.value,
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
@router.post(
    "/professionals/{professional_id}/projects",
    response_model=ProjectResponse,
)
def add_project(
    professional_id: str,
    request: ProjectRequest,
):
    """
    Add a Project to a Professional.
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

    project = Project(

        name=ProjectName(
            request.name
        ),

        description=request.description,

        repository_url=request.repository_url,

        live_url=request.live_url,

        technologies=request.technologies,
    )

    use_case = (
        container.add_project_use_case()
    )

    professional = use_case.execute(
        professional_uuid,
        project,
    )

    if professional is None:
        raise HTTPException(
            status_code=404,
            detail="Professional not found.",
        )

    return ProjectMapper.to_response(
        project
    )
@router.get(
    "/professionals/{professional_id}/projects",
    response_model=list[ProjectResponse],
)
def get_projects(
    professional_id: str,
):
    """
    Retrieve Projects belonging to a Professional.
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
        container.get_projects_use_case()
    )

    projects = use_case.execute(
        professional_uuid
    )

    return [

        ProjectMapper.to_response(
            project
        )

        for project in projects
    ]
# =============================================================================
# Skill Endpoints
# =============================================================================

@router.post(
    "/professionals/{professional_id}/skills",
    response_model=SkillResponse,
)
def add_skill(
    professional_id: str,
    request: SkillRequest,
):
    """
    Add a Skill to a Professional.
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

    skill = Skill(
        name=request.name,
    )

    use_case = (
        container.add_skill_use_case()
    )

    professional = use_case.execute(
        professional_uuid,
        skill,
    )

    if professional is None:
        raise HTTPException(
            status_code=404,
            detail="Professional not found.",
        )

    return SkillMapper.to_response(
        skill
    )


@router.get(
    "/professionals/{professional_id}/skills",
    response_model=list[SkillResponse],
)
def get_skills(
    professional_id: str,
):
    """
    Retrieve all Skills belonging to a Professional.
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
        container.get_skills_use_case()
    )

    skills = use_case.execute(
        professional_uuid
    )

    return [
        SkillMapper.to_response(
            skill
        )
        for skill in skills
    ]


@router.delete(
    "/professionals/{professional_id}/skills/{skill_id}",
    status_code=204,
)
def remove_skill(
    professional_id: str,
    skill_id: str,
):
    """
    Remove a Skill from a Professional.
    """

    try:
        professional_uuid = UUID(
            professional_id
        )

        skill_uuid = UUID(
            skill_id
        )

    except ValueError:
        raise HTTPException(
            status_code=400,
            detail="Invalid UUID.",
        )

    use_case = (
        container.remove_skill_use_case()
    )

    professional = use_case.execute(
        professional_uuid,
        skill_uuid,
    )

    if professional is None:
        raise HTTPException(
            status_code=404,
            detail="Professional not found.",
        )
@router.delete(
    "/professionals/{professional_id}",
    status_code=204,
)
def delete_professional(
    professional_id: str,
):
    """
    Delete a Professional.
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
        container.delete_professional_use_case()
    )

    try:
        use_case.execute(
            professional_uuid
        )

    except ProfessionalNotFoundException:
        raise HTTPException(
            status_code=404,
            detail="Professional not found.",
        )

    return
@router.patch(
    "/professionals/{professional_id}",
    response_model=ProfessionalResponse,
)
def update_professional(
    professional_id: str,
    request: UpdateProfessionalRequest,
):

    professional = (
        container.update_professional_use_case()
        .execute(
            UUID(professional_id),
            request.full_name,
            request.primary_goal,
        )
    )

    return ProfessionalResponse(
        id=str(professional.id),
        full_name=str(
            professional.full_name
        ),
        primary_goal=professional.primary_goal,
        created_at=professional.created_at,
    )


@router.delete(
    "/professionals/{professional_id}",
    status_code=204,
)
def delete_professional(
    professional_id: str,
):

    container.delete_professional_use_case().execute(
        UUID(professional_id)
    )

    return Response(
        status_code=204
    )