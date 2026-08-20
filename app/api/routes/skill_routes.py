"""
Skill API Routes.

Responsibilities
-----------------
- Expose Skill endpoints.
- Convert API requests into domain objects.
- Call application use cases.
- Convert domain objects into API responses.

No business rules belong here.
"""

from uuid import UUID

from fastapi import APIRouter, HTTPException


from app.bootstrap.container import container


# ============================================================================
# Schemas
# ============================================================================

from app.api.schemas.skill_request import (
    SkillRequest,
)



# ============================================================================
# Mapper
# ============================================================================

from app.api.mappers.skill_mapper import (
    SkillMapper,
)



# ============================================================================
# Domain
# ============================================================================

from app.domain.skill.skill import Skill



router = APIRouter(
    prefix="/skills",
    tags=["Skills"],
)



# ============================================================================
# ADD SKILL
# ============================================================================


@router.post(
    "/{professional_id}",
)
def add_skill(
    professional_id: UUID,
    request: SkillRequest,
):
    """
    Add skill to Professional.
    """


    skill = Skill(
        name=request.name,
    )


    professional = (
        container
        .add_skill_use_case()
        .execute(
            professional_id,
            skill,
        )
    )


    if professional is None:
        raise HTTPException(
            status_code=404,
            detail="Professional not found",
        )


    return SkillMapper.to_response(
        skill
    )



# ============================================================================
# GET SKILLS
# ============================================================================


@router.get(
    "/{professional_id}",
)
def get_skills(
    professional_id: UUID,
):
    """
    Get all skills of Professional.
    """


    skills = (
        container
        .get_skills_use_case()
        .execute(
            professional_id
        )
    )


    return [

        SkillMapper.to_response(
            skill
        )

        for skill in skills

    ]



# ============================================================================
# REMOVE SKILL
# ============================================================================


@router.delete(
    "/{professional_id}/{skill_id}",
)
def remove_skill(
    professional_id: UUID,
    skill_id: UUID,
):
    """
    Remove skill from Professional.
    """


    result = (
        container
        .remove_skill_use_case()
        .execute(
            professional_id,
            skill_id,
        )
    )


    if result is None:
        raise HTTPException(
            status_code=404,
            detail="Skill not found",
        )


    return {
        "message": "Skill removed successfully"
    }



# ============================================================================
# UPDATE SKILL
# ============================================================================


@router.patch(
    "/{professional_id}/{skill_id}",
)
def update_skill(
    professional_id: UUID,
    skill_id: UUID,
    request: SkillRequest,
):
    """
    Update existing skill.
    """


    skill = Skill(
        name=request.name,
    )


    skill.id = skill_id


    professional = (
        container
        .update_skill_use_case()
        .execute(
            professional_id,
            skill,
        )
    )


    if professional is None:
        raise HTTPException(
            status_code=404,
            detail="Professional not found",
        )


    return SkillMapper.to_response(
        skill
    )