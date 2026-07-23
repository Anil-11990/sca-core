"""
API Routes package.
"""

from fastapi import APIRouter

from app.interfaces.api.routes.professional_routes import (
    router as professional_router,
)

from app.interfaces.api.routes.timeline_routes import (
    router as timeline_router,
)


router = APIRouter()

router.include_router(
    professional_router
)

router.include_router(
    timeline_router
)


__all__ = [
    "router",
]