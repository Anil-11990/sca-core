from dataclasses import dataclass, field
from datetime import UTC, datetime

from app.domain.common.entity import Entity
from app.domain.experience.value_objects.job_title import RoleTitle
from app.domain.experience.value_objects.company_name import CompanyName


@dataclass(eq=False, slots=True)
class Experience(Entity):

    # Required fields
    role: RoleTitle
    company: CompanyName
    description: str

    # Optional/default fields
    created_at: datetime = field(
        default_factory=lambda: datetime.now(UTC)
    )

    def __post_init__(self) -> None:
        self.description = self.description.strip()

        if not self.description:
            raise ValueError(
                "Description cannot be empty."
            )