"""
Shared fixtures for API tests.
"""

from fastapi.testclient import TestClient

from app.interfaces.api.main import app


def client():
    """
    Returns a FastAPI test client.
    """
    return TestClient(app)