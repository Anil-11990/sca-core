"""
Timeline API Routes.

Responsibilities
-----------------
- Expose Timeline Event endpoints.
- Delegate logic to Application Use Cases.
- Convert domain objects to API responses.

No business rules belong here.
"""

from uuid import UUID

from fastapi import APIRouter, HTTPException

from app.bootstrap.container import container

from app.api.schemas.timeline_event_request import (
    TimelineEventRequest,
)

from app.api.schemas.timeline_event_response import (
    TimelineEventResponse,
)

from app.api.mappers.timeline_event_mapper import (
    TimelineEventMapper,
)

from app.domain.timeline.timeline_event import (
    TimelineEvent,
)

from app.domain.timeline.timeline_event_type import (
    TimelineEventType,
)


router = APIRouter(
    prefix="/professionals",
    tags=["Timeline"],
)


# ==========================================================
# ADD TIMELINE EVENT
# ==========================================================

@router.post(
    "/{professional_id}/timeline",
    response_model=TimelineEventResponse,
    status_code=201,
)
def add_timeline_event(
    professional_id: str,
    request: TimelineEventRequest,
):
    """
    Add timeline event to Professional.
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


    try:
        event_type = TimelineEventType(
            request.event_type
        )

    except ValueError:
        raise HTTPException(
            status_code=400,
            detail="Invalid timeline event type.",
        )


    event = TimelineEvent(
        title=request.title,
        event_type=event_type,
        event_date=request.event_date,
        description=request.description,
        reference_id=request.reference_id,
    )


    professional = (
        container
        .add_timeline_event_use_case()
        .execute(
            professional_uuid,
            event,
        )
    )


    if professional is None:
        raise HTTPException(
            status_code=404,
            detail="Professional not found.",
        )


    return TimelineEventMapper.to_response(
        event
    )



# ==========================================================
# GET TIMELINE EVENTS
# ==========================================================

@router.get(
    "/{professional_id}/timeline",
    response_model=list[TimelineEventResponse],
)
def get_timeline_events(
    professional_id: str,
):
    """
    Get all timeline events.
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


    events = (
        container
        .get_timeline_events_use_case()
        .execute(
            professional_uuid
        )
    )


    return [
        TimelineEventMapper.to_response(
            event
        )
        for event in events
    ]



# ==========================================================
# REMOVE TIMELINE EVENT
# ==========================================================

@router.delete(
    "/{professional_id}/timeline/{event_id}",
)
def remove_timeline_event(
    professional_id: str,
    event_id: str,
):
    """
    Remove timeline event.
    """

    try:

        professional_uuid = UUID(
            professional_id
        )

        event_uuid = UUID(
            event_id
        )

    except ValueError:

        raise HTTPException(
            status_code=400,
            detail="Invalid UUID.",
        )


    professional = (
        container
        .remove_timeline_event_use_case()
        .execute(
            professional_uuid,
            event_uuid,
        )
    )


    if professional is None:

        raise HTTPException(
            status_code=404,
            detail="Professional not found.",
        )


    return {
        "message": "Timeline event removed successfully."
    }



# ==========================================================
# UPDATE TIMELINE EVENT
# ==========================================================

@router.patch(
    "/{professional_id}/timeline/{event_id}",
    response_model=TimelineEventResponse,
)
def update_timeline_event(
    professional_id: str,
    event_id: str,
    request: TimelineEventRequest,
):
    """
    Update a timeline event.
    """

    try:

        professional_uuid = UUID(
            professional_id
        )

        event_uuid = UUID(
            event_id
        )

    except ValueError:

        raise HTTPException(
            status_code=400,
            detail="Invalid UUID.",
        )


    try:

        event_type = TimelineEventType(
            request.event_type
        )

    except ValueError:

        raise HTTPException(
            status_code=400,
            detail="Invalid timeline event type.",
        )


    event = TimelineEvent(
        title=request.title,
        event_type=event_type,
        event_date=request.event_date,
        description=request.description,
        reference_id=request.reference_id,
    )


    event.id = event_uuid


    professional = (
        container
        .update_timeline_event_use_case()
        .execute(
            professional_uuid,
            event,
        )
    )


    if professional is None:

        raise HTTPException(
            status_code=404,
            detail="Professional not found.",
        )


    return TimelineEventMapper.to_response(
        event
    )