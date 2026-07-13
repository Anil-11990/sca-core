"""
Request models for the API.

These models define what data the client
must send when calling the API.
"""

from pydantic import BaseModel


class CreateProfessionalRequest(BaseModel):
    """
    Data required to create a Professional.
    """

    full_name: str
    primary_goal: str