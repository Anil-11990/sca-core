"""
Market Signal Domain Object.

Represents external career market information.
"""

from dataclasses import dataclass
from uuid import UUID, uuid4


@dataclass(eq=False, slots=True)
class MarketSignal:
    """
    Represents a career market signal.
    """

    skill: str
    demand_level: str
    trend: str
    source: str

    id: UUID = uuid4()

    def __post_init__(self) -> None:

        self.skill = self.skill.strip()
        self.demand_level = self.demand_level.strip()
        self.trend = self.trend.strip()
        self.source = self.source.strip()

        if not self.skill:
            raise ValueError(
                "Skill cannot be empty."
            )

        if not self.demand_level:
            raise ValueError(
                "Demand level cannot be empty."
            )

        if not self.trend:
            raise ValueError(
                "Trend cannot be empty."
            )

        if not self.source:
            raise ValueError(
                "Source cannot be empty."
            )