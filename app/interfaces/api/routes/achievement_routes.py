"""
Achievement API Routes.

Responsibilities
-----------------
- Expose Achievement endpoints.
- Convert requests into domain objects.
- Delegate work to use cases.
- Convert domain objects into responses.

No business rules belong here.
"""

from uuid import UUID

from fastapi import APIRouter, HTTPException

from app.bootstrap.container import container


# Schemas
from app.interfaces.api.schemas.achievement_request import (
    AchievementRequest,
)


# Mapper
from app.interfaces.api.mappers.achievement_mapper import (
    AchievementMapper,
)


# Domain
from app.domain.achievement.achievement import Achievement
from app.domain.achievement.achievement_type import (
    AchievementType,
)

from app.domain.achievement.value_objects.achievement_title import (
    AchievementTitle,
)

from app.domain.achievement.value_objects.issuer import (
    Issuer,
)



router = APIRouter(
    prefix="/achievements",
    tags=["Achievements"],
)



# ============================================================================
# ADD ACHIEVEMENT
# ============================================================================


@router.post("/{professional_id}")
def add_achievement(
    professional_id: UUID,
    request: AchievementRequest,
):
    """
    Add achievement to Professional.
    """


    achievement = Achievement(
        title=AchievementTitle(
            request.title
        ),
        issuer=Issuer(
            request.issuer
        ),
        achievement_type=AchievementType(
            request.achievement_type
        ),
        description=request.description,
        credential_url=request.credential_url,
    )


    professional = (
        container
        .add_achievement_use_case()
        .execute(
            professional_id,
            achievement,
        )
    )


    if professional is None:
        raise HTTPException(
            status_code=404,
            detail="Professional not found",
        )


    return AchievementMapper.to_response(
        achievement
    )



# ============================================================================
# GET ACHIEVEMENTS
# ============================================================================


@router.get("/{professional_id}")
def get_achievements(
    professional_id: UUID,
):
    """
    Get all achievements.
    """


    achievements = (
        container
        .get_achievements_use_case()
        .execute(
            professional_id
        )
    )


    return [

        AchievementMapper.to_response(
            achievement
        )

        for achievement in achievements

    ]



# ============================================================================
# REMOVE ACHIEVEMENT
# ============================================================================


@router.delete(
    "/{professional_id}/{achievement_id}"
)
def remove_achievement(
    professional_id: UUID,
    achievement_id: UUID,
):
    """
    Remove achievement.
    """


    professional = (
        container
        .remove_achievement_use_case()
        .execute(
            professional_id,
            achievement_id,
        )
    )


    if professional is None:
        raise HTTPException(
            status_code=404,
            detail="Achievement not found",
        )


    return {
        "message": "Achievement removed successfully"
    }



# ============================================================================
# UPDATE ACHIEVEMENT
# ============================================================================


@router.patch(
    "/{professional_id}/{achievement_id}"
)
def update_achievement(
    professional_id: UUID,
    achievement_id: UUID,
    request: AchievementRequest,
):
    """
    Update achievement.
    """


    achievement = Achievement(
        title=AchievementTitle(
            request.title
        ),
        issuer=Issuer(
            request.issuer
        ),
        achievement_type=AchievementType(
            request.achievement_type
        ),
        description=request.description,
        credential_url=request.credential_url,
    )


    achievement.id = achievement_id


    professional = (
        container
        .update_achievement_use_case()
        .execute(
            professional_id,
            achievement_id,
            achievement,
        )
    )


    if professional is None:
        raise HTTPException(
            status_code=404,
            detail="Professional not found",
        )


    return AchievementMapper.to_response(
        achievement
    )