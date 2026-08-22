"""
Career Intelligence API Routes.

Career Intelligence is generated from the
current Professional profile.

The API layer:
    - receives HTTP requests
    - delegates to application use cases
    - converts results into API responses

Business rules remain outside this layer.
"""

from uuid import UUID

from fastapi import APIRouter, HTTPException

from app.bootstrap.container import container

from app.api.schemas.career_analysis_request import (
    CareerAnalysisRequest,
)

from app.api.schemas.career_analysis_response import (
    CareerAnalysisResponse,
)

from app.api.schemas.career_intelligence_response import (
    CareerInsightSchema,
    RecommendationSchema,
)

from app.exceptions.professional_not_found import (
    ProfessionalNotFoundException,
)
from app.api.schemas.career_roadmap_response import (
    CareerRoadmapItemSchema,
)


router = APIRouter(
    prefix="/career-intelligence",
    tags=["Career Intelligence"],
)


# ============================================================================
# CAREER ANALYSIS
# ============================================================================


@router.post(
    "/{professional_id}/analysis",
    response_model=CareerAnalysisResponse,
    status_code=200,
)
def analyze_career(
    professional_id: UUID,
    request: CareerAnalysisRequest,
):
    """
    Generate a complete career analysis.
    """

    use_case = (
        container.analyze_career_use_case()
    )

    try:

        result = use_case.execute(
            professional_id=professional_id,
            required_skills=request.required_skills,
        )

    except ValueError as exc:

        raise HTTPException(
            status_code=404,
            detail=str(exc),
        )

    return CareerAnalysisResponse(
        career_score=result.career_score,
        profile_completion=result.profile_completion,
        skill_gaps=result.skill_gaps,
        career_readiness=result.career_readiness,
    )


# ============================================================================
# GET CAREER ANALYSIS
# ============================================================================


@router.get(
    "/{professional_id}/analysis",
    response_model=CareerAnalysisResponse,
)
def get_career_analysis(
    professional_id: UUID,
):
    """
    Generate the current career analysis.

    This endpoint uses the Professional's
    current profile data.

    No JSON body is required.
    """

    # The existing AnalyzeCareer use case requires
    # required_skills, so this endpoint uses an empty
    # required-skill list until a stored career target
    # exists in the domain.

    use_case = (
        container.analyze_career_use_case()
    )

    try:

        result = use_case.execute(
            professional_id=professional_id,
            required_skills=[],
        )

    except ValueError as exc:

        raise HTTPException(
            status_code=404,
            detail=str(exc),
        )

    return CareerAnalysisResponse(
        career_score=result.career_score,
        profile_completion=result.profile_completion,
        skill_gaps=result.skill_gaps,
        career_readiness=result.career_readiness,
    )


# ============================================================================
# CAREER INSIGHTS
# ============================================================================


@router.get(
    "/{professional_id}/insights",
    response_model=list[CareerInsightSchema],
)
def get_career_insights(
    professional_id: UUID,
):
    """
    Generate career insights for a Professional.
    """

    use_case = (
        container
        .generate_career_insights_use_case()
    )

    try:

        insights = use_case.execute(
            professional_id
        )

    except ProfessionalNotFoundException:

        raise HTTPException(
            status_code=404,
            detail="Professional not found.",
        )

    return [
        CareerInsightSchema(
            title=insight.title,
            description=insight.description,
            category=insight.category,
        )

        for insight in insights
    ]


# ============================================================================
# CAREER RECOMMENDATIONS
# ============================================================================


@router.get(
    "/{professional_id}/recommendations",
    response_model=list[RecommendationSchema],
)
def get_career_recommendations(
    professional_id: UUID,
):
    """
    Generate career recommendations for a Professional.
    """

    use_case = (
        container
        .get_recommendations_use_case()
    )

    try:

        recommendations = use_case.execute(
            professional_id
        )

    except ProfessionalNotFoundException:

        raise HTTPException(
            status_code=404,
            detail="Professional not found.",
        )

    return [
        RecommendationSchema(
            action=recommendation.action,
            reason=recommendation.reason,
            priority=recommendation.priority,
        )

        for recommendation in recommendations
    ]
# ============================================================================
# CAREER ROADMAP
# ============================================================================


@router.get(
    "/{professional_id}/roadmap",
    response_model=list[CareerRoadmapItemSchema],
)
def get_career_roadmap(
    professional_id: UUID,
):
    """
    Generate a career development roadmap
    for a Professional.
    """

    use_case = (
        container
        .generate_career_roadmap_use_case()
    )

    try:

        roadmap = use_case.execute(
            professional_id
        )

    except ProfessionalNotFoundException:

        raise HTTPException(
            status_code=404,
            detail="Professional not found.",
        )

    return [
        CareerRoadmapItemSchema(
            skill=item["skill"],
            priority=item["priority"],
            stage=item["stage"],
        )
        for item in roadmap
    ]