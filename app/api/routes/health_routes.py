"""
Health check API routes.
"""

from fastapi import APIRouter


router = APIRouter()


@router.get("/health")
def health_check() -> dict[str, str]:
    """Return API health status."""
    return {"status": "ok"}


__all__ = ["router"]