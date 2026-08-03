"""
Evidence Entity.

Represents proof supporting a professional claim.
"""

from dataclasses import dataclass, field
from uuid import UUID, uuid4

from app.domain.common.entity import Entity


@dataclass(eq=False, slots=True)
class Evidence(Entity):
    """
    Represents career evidence.

    Evidence connects achievements,
    skills and professional growth.
    """

    title: str

    description: str = ""

    evidence_type: str = ""

    reference_url: str = ""

    def __post_init__(self) -> None:

        self.title = self.title.strip()

        self.description = (
            self.description.strip()
        )

        self.evidence_type = (
            self.evidence_type.strip()
        )

        self.reference_url = (
            self.reference_url.strip()
        )

        if not self.title:
            raise ValueError(
                "Evidence title cannot be empty."
            )