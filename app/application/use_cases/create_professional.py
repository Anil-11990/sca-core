"""
Application Use Case:
Create Professional
"""

from app.domain.common.value_objects.full_name import FullName
from app.domain.professional.professional import Professional
from app.domain.professional.repository import ProfessionalRepository


class CreateProfessional:
    """
    Creates and stores a Professional.

    The Application Layer coordinates the workflow,
    while the Domain Layer enforces business rules.
    """

    def __init__(
        self,
        repository: ProfessionalRepository,
    ) -> None:
        # Repository is injected instead of being created here.
        # This keeps the use case independent of storage details.
        self._repository = repository

    def execute(
        self,
        full_name: str,
        primary_goal: str,
    ) -> Professional:
        """
        Create a Professional and persist it.
        """

        professional = Professional(
            full_name=FullName(full_name),
            primary_goal=primary_goal,
        )

        self._repository.save(professional)

        return professional