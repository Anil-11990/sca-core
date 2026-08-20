"""
Goal API Routes.

Responsibilities
-----------------
- Expose Goal endpoints.
- Convert API requests into domain objects.
- Delegate business logic to use cases.
- Convert domain objects into API responses.

No business rules belong here.
"""

from uuid import UUID

from fastapi import APIRouter, HTTPException

from app.bootstrap.container import container


# Schemas
from app.api.schemas.goal_request import (
    GoalRequest,
)

from app.api.schemas.goal_response import (
    GoalResponse,
)


# Mapper
from app.api.mappers.goal_mapper import (
    to_goal_response,
)


# Domain
from app.domain.goal.goal import Goal
from app.domain.goal.value_objects.goal_title import (
    GoalTitle,
)


router = APIRouter(
    prefix="/goals",
    tags=["Goals"],
)



# ============================================================================
# ADD GOAL
# ============================================================================


@router.post(
    "/{professional_id}",
    response_model=GoalResponse,
    status_code=201,
)
def add_goal(
    professional_id: UUID,
    request: GoalRequest,
):
    """
    Add a new goal to a Professional.
    """


    goal = Goal(
        title=GoalTitle(
            request.title
        )
    )


    professional = (
        container
        .add_goal_use_case()
        .execute(
            professional_id,
            goal,
        )
    )


    if professional is None:
        raise HTTPException(
            status_code=404,
            detail="Professional not found",
        )


    return to_goal_response(
        goal
    )



# ============================================================================
# GET GOALS
# ============================================================================


@router.get(
    "/{professional_id}",
    response_model=list[GoalResponse],
)
def get_goals(
    professional_id: UUID,
):
    """
    Retrieve all goals belonging to a Professional.
    """

    try:
        goals = (
            container
            .get_goals_use_case()
            .execute(
                professional_id
            )
        )

    except Exception:
        raise HTTPException(
            status_code=404,
            detail="Professional not found",
        )

    return [
        to_goal_response(goal)
        for goal in goals
    ]
# ============================================================================
# REMOVE GOAL
# ============================================================================


@router.delete(
    "/{professional_id}/{goal_id}",
)
def remove_goal(
    professional_id: UUID,
    goal_id: UUID,
):
    """
    Remove a goal from Professional.
    """


    try:

        professional = (
            container
            .remove_goal_use_case()
            .execute(
                professional_id,
                goal_id,
            )
        )

    except Exception:

        raise HTTPException(
            status_code=404,
            detail="Goal not found",
        )


    return {
        "message": "Goal removed successfully"
    }



# ============================================================================
# UPDATE GOAL PROGRESS
# ============================================================================


@router.patch(
    "/{professional_id}/{goal_id}/progress",
    response_model=GoalResponse,
)
def update_goal_progress(
    professional_id: UUID,
    goal_id: UUID,
    progress: int,
):
    """
    Update goal progress percentage.
    """


    professional = (
        container
        .get_professional_use_case()
        .execute(
            professional_id
        )
    )


    if professional is None:
        raise HTTPException(
            status_code=404,
            detail="Professional not found",
        )


    goal = next(
        (
            item
            for item in professional.goals
            if item.id == goal_id
        ),
        None,
    )


    if goal is None:
        raise HTTPException(
            status_code=404,
            detail="Goal not found",
        )


    goal.update_progress(
        progress
    )


    container.professional_repository.save(
        professional
    )


    return to_goal_response(
        goal
    )



# ============================================================================
# COMPLETE GOAL
# ============================================================================


@router.patch(
    "/{professional_id}/{goal_id}/complete",
    response_model=GoalResponse,
)
def complete_goal(
    professional_id: UUID,
    goal_id: UUID,
):
    """
    Mark goal as completed.
    """


    professional = (
        container
        .get_professional_use_case()
        .execute(
            professional_id
        )
    )


    if professional is None:
        raise HTTPException(
            status_code=404,
            detail="Professional not found",
        )


    goal = next(
        (
            item
            for item in professional.goals
            if item.id == goal_id
        ),
        None,
    )


    if goal is None:
        raise HTTPException(
            status_code=404,
            detail="Goal not found",
        )


    goal.update_progress(
        100
    )


    container.professional_repository.save(
        professional
    )


    return to_goal_response(
        goal
    )