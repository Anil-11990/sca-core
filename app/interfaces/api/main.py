"""
SCA API Entry Point.
"""

from fastapi import FastAPI
from app.interfaces.api.routes import router

app = FastAPI(
    title="SCA API",
    description="Sovereign Career Architect Backend",
    version="0.1.0",
)

# Register all API routes.
app.include_router(router)