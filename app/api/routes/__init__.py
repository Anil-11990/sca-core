"""
API Router.

All REST endpoints are registered here.
"""

from fastapi import APIRouter

from app.api.routes.professional_routes import (
    router as professional_router,
)

from app.api.routes.skill_routes import (
    router as skill_router,
)

from app.api.routes.education_routes import (
    router as education_router,
)

from app.api.routes.experience_routes import (
    router as experience_router,
)

from app.api.routes.project_routes import (
    router as project_router,
)

from app.api.routes.goal_routes import (
    router as goal_router,
)

from app.api.routes.achievement_routes import (
    router as achievement_router,
)

from app.api.routes.certificate_routes import (
    router as certificate_router,
)

from app.api.routes.timeline_routes import (
    router as timeline_router,
)

router = APIRouter()

router.include_router(professional_router)
router.include_router(skill_router)
router.include_router(education_router)
router.include_router(experience_router)
router.include_router(project_router)
router.include_router(goal_router)
router.include_router(achievement_router)
router.include_router(certificate_router)
router.include_router(timeline_router)

__all__ = [
    "router",
]