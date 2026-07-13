"""
Application Composition Root.

Responsible for constructing the application's
dependencies.

Only this module should know which concrete
implementations are used.
"""

from app.application.use_cases.create_professional import CreateProfessional
from app.application.use_cases.get_professional import GetProfessional
from app.infrastructure.repositories.memory_professional_repository import (
    MemoryProfessionalRepository,
)


class Container:
    """
    Builds and provides application services.
    """

    def __init__(self) -> None:
        # Shared repository instance.
        self.professional_repository = MemoryProfessionalRepository()

    def create_professional_use_case(self) -> CreateProfessional:
        """
        Creates the CreateProfessional use case.
        """

        return CreateProfessional(
            repository=self.professional_repository
        )

    def get_professional_use_case(self) -> GetProfessional:
        """
        Creates the GetProfessional use case.
        """

        return GetProfessional(
            repository=self.professional_repository
        )


# -----------------------------------------------------------------------------
# Global Dependency Container
# -----------------------------------------------------------------------------

container = Container()