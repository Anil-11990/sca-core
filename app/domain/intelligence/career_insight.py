"""
Career Insight Domain Object.

Represents an intelligence observation
about a Professional career profile.
"""

from dataclasses import dataclass
from uuid import UUID, uuid4


@dataclass(eq=False, slots=True)
class CareerInsight:
    """
    Represents a career intelligence insight.
    """

    title: str
    description: str
    category: str

    id: UUID = uuid4()

    def __post_init__(self) -> None:
        self.title = self.title.strip()
        self.description = self.description.strip()
        self.category = self.category.strip()

        if not self.title:
            raise ValueError(
                "Insight title cannot be empty."
            )

        if not self.description:
            raise ValueError(
                "Insight description cannot be empty."
            )

        if not self.category:
            raise ValueError(
                "Insight category cannot be empty."
            )