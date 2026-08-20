"""
Application Entry Point.

Provides a stable import location:

    from app.main import app

This file simply exposes the FastAPI application defined inside
interfaces/api/main.py.
"""

from app.api.main import app

__all__ = ["app"]