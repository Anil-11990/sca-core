"""
Application Composition Root.

Responsible for constructing the application's
dependencies.

Only this module should know which concrete
implementations are used.
"""
from app.application.use_cases.add_experience import (
    AddExperienceUseCase,
)

from app.application.use_cases.get_experiences import (
    GetExperiencesUseCase,
)
from app.application.use_cases.create_professional import CreateProfessional
from app.application.use_cases.get_professional import GetProfessional
from app.infrastructure.repositories.memory_professional_repository import (
    MemoryProfessionalRepository,)
from app.application.use_cases.add_project import (AddProject,)
from app.application.use_cases.add_timeline_event import (
    AddTimelineEventUseCase,
)

from app.application.use_cases.get_timeline_events import (
    GetTimelineEventsUseCase,
)

from app.application.use_cases.remove_timeline_event import (
    RemoveTimelineEventUseCase,
)
from app.application.use_cases.get_projects import (GetProjects,)
from app.application.use_cases.add_achievement import AddAchievement
from app.application.use_cases.get_achievements import GetAchievements
from app.application.use_cases.add_certificate import AddCertificate
from app.application.use_cases.get_certificates import GetCertificates
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

    def add_achievement_use_case(self) -> AddAchievement:
        """
        Creates the AddAchievement use case.
        """

        return AddAchievement(
            repository=self.professional_repository
        )

    def get_achievements_use_case(self) -> GetAchievements:
        """
        Creates the GetAchievements use case.
        """

        return GetAchievements(
            repository=self.professional_repository
        )

    def add_certificate_use_case(
            self,
    ) -> AddCertificate:
        """
        Creates the AddCertificate use case.
        """

        return AddCertificate(
            repository=self.professional_repository,
        )

    def get_certificates_use_case(
            self,
    ) -> GetCertificates:
        """
        Creates the GetCertificates use case.
        """

        return GetCertificates(
            repository=self.professional_repository,
        )

    def add_experience_use_case(
            self,
    ):
        """
        Build AddExperienceUseCase.
        """

        return AddExperienceUseCase(
            self.professional_repository
        )

    def get_experiences_use_case(
            self,
    ):
        """
        Build GetExperiencesUseCase.
        """

        return GetExperiencesUseCase(
            self.professional_repository
        )

    def add_project_use_case(
            self,
    ):
        """
        Build AddProject use case.
        """

        return AddProject(
            self.professional_repository
        )

    def get_projects_use_case(
            self,
    ):
        """
        Build GetProjects use case.
        """

        return GetProjects(
            self.professional_repository
        )
    # -------------------------------------------------------------------------
    # Timeline Use Cases
    # -------------------------------------------------------------------------

    def add_timeline_event_use_case(
        self,
    ) -> AddTimelineEventUseCase:
        """
        Build AddTimelineEvent use case.
        """

        return AddTimelineEventUseCase(
            repository=self.professional_repository
        )


    def get_timeline_events_use_case(
        self,
    ) -> GetTimelineEventsUseCase:
        """
        Build GetTimelineEvents use case.
        """

        return GetTimelineEventsUseCase(
            repository=self.professional_repository
        )


    def remove_timeline_event_use_case(
        self,
    ) -> RemoveTimelineEventUseCase:
        """
        Build RemoveTimelineEvent use case.
        """

        return RemoveTimelineEventUseCase(
            repository=self.professional_repository
        )
# -----------------------------------------------------------------------------
# Global Dependency Container
# -----------------------------------------------------------------------------

container = Container()