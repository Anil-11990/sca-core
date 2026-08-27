"""
Application Composition Root.

Responsibility:
----------------

This file creates and connects all application dependencies.

The Container knows:

    - Which repository implementation to use
    - Which Use Case needs which repository
    - How objects are constructed

The Container DOES NOT:

    - Contain business rules
    - Modify domain objects
    - Handle API requests
"""

# =============================================================================
# Infrastructure
# =============================================================================

from app.infrastructure.repositories.sqlite_professional_repository import (
    SQLiteProfessionalRepository,
)


# =============================================================================
# Application Use Cases
# =============================================================================

# -----------------------------------------------------------------------------
# Professional
# -----------------------------------------------------------------------------

from app.application.use_cases.create_professional import (
    CreateProfessional,
)

from app.application.use_cases.get_professional import (
    GetProfessional,
)

from app.application.use_cases.update_professional import (
    UpdateProfessional,
)

from app.application.use_cases.delete_professional import (
    DeleteProfessional,
)


# -----------------------------------------------------------------------------
# Achievement
# -----------------------------------------------------------------------------

from app.application.use_cases.add_achievement import (
    AddAchievement,
)

from app.application.use_cases.get_achievements import (
    GetAchievements,
)

from app.application.use_cases.update_achievement import (
    UpdateAchievement,
)

from app.application.use_cases.remove_achievement import (
    RemoveAchievement,
)


# -----------------------------------------------------------------------------
# Certificate
# -----------------------------------------------------------------------------

from app.application.use_cases.add_certificate import (
    AddCertificate,
)

from app.application.use_cases.get_certificates import (
    GetCertificates,
)

from app.application.use_cases.update_certificate import (
    UpdateCertificate,
)

from app.application.use_cases.remove_certificate import (
    RemoveCertificate,
)


# -----------------------------------------------------------------------------
# Education
# -----------------------------------------------------------------------------

from app.application.use_cases.add_education import (
    AddEducation,
)

from app.application.use_cases.get_education import (
    GetEducation,
)

from app.application.use_cases.update_education import (
    UpdateEducation,
)

from app.application.use_cases.remove_education import (
    RemoveEducation,
)


# -----------------------------------------------------------------------------
# Goal
# -----------------------------------------------------------------------------

from app.application.use_cases.add_goal import (
    AddGoalUseCase,
)

from app.application.use_cases.get_goals import (
    GetGoalsUseCase,
)

from app.application.use_cases.update_goal import (
    UpdateGoalUseCase,
)

from app.application.use_cases.remove_goal import (
    RemoveGoalUseCase,
)


# -----------------------------------------------------------------------------
# Experience
# -----------------------------------------------------------------------------

from app.application.use_cases.add_experience import (
    AddExperienceUseCase,
)

from app.application.use_cases.get_experiences import (
    GetExperiencesUseCase,
)

from app.application.use_cases.update_experience import (
    UpdateExperience,
)

from app.application.use_cases.remove_experience import (
    RemoveExperience,
)


# -----------------------------------------------------------------------------
# Project
# -----------------------------------------------------------------------------

from app.application.use_cases.add_project import (
    AddProject,
)

from app.application.use_cases.get_projects import (
    GetProjects,
)

from app.application.use_cases.update_project import (
    UpdateProject,
)

from app.application.use_cases.remove_project import (
    RemoveProject,
)


# -----------------------------------------------------------------------------
# Skill
# -----------------------------------------------------------------------------

from app.application.use_cases.add_skill import (
    AddSkillUseCase,
)

from app.application.use_cases.get_skills import (
    GetSkillsUseCase,
)

from app.application.use_cases.update_skill import (
    UpdateSkill,
)

from app.application.use_cases.remove_skill import (
    RemoveSkillUseCase,
)


# -----------------------------------------------------------------------------
# Timeline
# -----------------------------------------------------------------------------

from app.application.use_cases.add_timeline_event import (
    AddTimelineEventUseCase,
)

from app.application.use_cases.get_timeline_events import (
    GetTimelineEventsUseCase,
)

from app.application.use_cases.update_timeline_event import (
    UpdateTimelineEvent,
)

from app.application.use_cases.remove_timeline_event import (
    RemoveTimelineEventUseCase,
)

# =============================================================================
# Intelligence
# =============================================================================

from app.application.use_cases.intelligence.analyze_career import (
    AnalyzeCareer,
)

from app.application.use_cases.intelligence.generate_career_insights import (
    GenerateCareerInsights,
)

from app.application.use_cases.intelligence.get_recommendations import (
    GetRecommendations,
)

from app.application.use_cases.intelligence.generate_career_roadmap import (
    GenerateCareerRoadmap,
)

from app.application.use_cases.intelligence.generate_market_intelligence import (
    GenerateMarketIntelligence,
)


# =============================================================================
# Intelligence Domain Services
# =============================================================================

from app.domain.intelligence.career_analyzer import (
    CareerAnalyzer,
)

from app.domain.intelligence.market_signal import (
    MarketSignal,
)

from app.domain.services.career_roadmap_service import (
    CareerRoadmapService,
)

from app.domain.services.market_intelligence_service import (
    MarketIntelligenceService,
)
# =============================================================================
# Container Class
# =============================================================================


class Container:
    """
    Dependency Injection Container.

    Creates application services.

    A single repository instance is shared
    between all use cases.
    """


    # -------------------------------------------------------------------------
    # Constructor
    # -------------------------------------------------------------------------

    def __init__(self):

        """
        Create shared infrastructure dependencies.

        Currently:

            SQLite Repository

        Later:

            PostgreSQL Repository
            Mongo Repository
            Cloud Database
        """


        self.professional_repository = (
            SQLiteProfessionalRepository()
        )
    # =========================================================================
    # Career Intelligence Use Cases
    # =========================================================================

    def analyze_career_use_case(
        self,
    ) -> AnalyzeCareer:

        return AnalyzeCareer(
            repository=self.professional_repository,
            analyzer=CareerAnalyzer(),
        )


    def generate_career_insights_use_case(
        self,
    ) -> GenerateCareerInsights:

        return GenerateCareerInsights(
            repository=self.professional_repository,
        )


    def get_recommendations_use_case(
        self,
    ) -> GetRecommendations:

        return GetRecommendations(
            repository=self.professional_repository,
        )


    def generate_career_roadmap_use_case(
        self,
    ) -> GenerateCareerRoadmap:

        return GenerateCareerRoadmap(
            repository=self.professional_repository,
            roadmap_service=CareerRoadmapService(),
        )
    # =========================================================================
    # Market Intelligence Use Case
    # =========================================================================

    def generate_market_intelligence_use_case(
        self,
    ) -> GenerateMarketIntelligence:

        """
        Build GenerateMarketIntelligence use case.

        This use case coordinates:

            - Professional repository
            - Market intelligence domain service
            - Market signals

        Version 1:

            Market signals are currently defined
            inside the composition root.

        Future versions can replace these
        hard-coded signals with:

            - MarketSignal repository
            - Job board ingestion
            - External market data provider
            - AI market intelligence pipeline

        Business rules do NOT belong here.
        The Container only connects dependencies.
        """

        # ---------------------------------------------------------------------
        # Version 1 Market Signals
        # ---------------------------------------------------------------------

        market_signals = [

            MarketSignal(
                skill="Python",
                demand_level="High",
                trend="Growing",
                source="Job Market",
            ),

            MarketSignal(
                skill="Machine Learning",
                demand_level="High",
                trend="Growing",
                source="Job Market",
            ),

            MarketSignal(
                skill="LLM",
                demand_level="High",
                trend="Growing",
                source="AI Job Market",
            ),

            MarketSignal(
                skill="Docker",
                demand_level="Medium",
                trend="Growing",
                source="Job Market",
            ),

            MarketSignal(
                skill="Kubernetes",
                demand_level="High",
                trend="Growing",
                source="Job Market",
            ),
        ]

        # ---------------------------------------------------------------------
        # Create Market Intelligence Use Case
        # ---------------------------------------------------------------------

        return GenerateMarketIntelligence(
            repository=self.professional_repository,

            market_intelligence_service=(
                MarketIntelligenceService()
            ),

            market_signals=market_signals,
        )

    # =========================================================================
    # Professional Use Cases
    # =========================================================================


    def create_professional_use_case(
        self,
    ) -> CreateProfessional:

        """
        Build CreateProfessional use case.
        """

        return CreateProfessional(
            repository=self.professional_repository
        )



    def get_professional_use_case(
        self,
    ) -> GetProfessional:

        """
        Build GetProfessional use case.
        """

        return GetProfessional(
            repository=self.professional_repository
        )

    def update_professional_use_case(
            self,
    ) -> UpdateProfessional:
        return UpdateProfessional(
            repository=self.professional_repository
        )

    def delete_professional_use_case(
            self,
    ) -> DeleteProfessional:
        return DeleteProfessional(
            repository=self.professional_repository
        )


    # =========================================================================
    # Achievement Use Cases
    # =========================================================================


    def add_achievement_use_case(
        self,
    ) -> AddAchievement:

        """
        Build AddAchievement use case.
        """

        return AddAchievement(
            repository=self.professional_repository
        )



    def get_achievements_use_case(
        self,
    ) -> GetAchievements:

        """
        Build GetAchievements use case.
        """

        return GetAchievements(
            repository=self.professional_repository
        )

    def update_achievement_use_case(
            self,
    ) -> UpdateAchievement:
        """
        Build UpdateAchievement use case.
        """
        return UpdateAchievement(
            repository=self.professional_repository
        )

    def remove_achievement_use_case(
            self,
    ) -> RemoveAchievement:
        """
        Build RemoveAchievement use case.
        """
        return RemoveAchievement(
            repository=self.professional_repository
        )



    # =========================================================================
    # Certificate Use Cases
    # =========================================================================


    def add_certificate_use_case(
        self,
    ) -> AddCertificate:

        """
        Build AddCertificate use case.
        """

        return AddCertificate(
            repository=self.professional_repository
        )



    def get_certificates_use_case(
        self,
    ) -> GetCertificates:

        """
        Build GetCertificates use case.
        """

        return GetCertificates(
            repository=self.professional_repository
        )

    def update_certificate_use_case(
            self,
    ) -> UpdateCertificate:
        """
        Build UpdateCertificate use case.
        """

        return UpdateCertificate(
            repository=self.professional_repository
        )

    def remove_certificate_use_case(
            self,
    ) -> RemoveCertificate:
        """
        Build RemoveCertificate use case.
        """

        return RemoveCertificate(
            repository=self.professional_repository
        )

    # =========================================================================
    # Education Use Cases
    # =========================================================================


    def add_education_use_case(
        self,
    ) -> AddEducation:

        """
        Build AddEducation use case.
        """

        return AddEducation(
            repository=self.professional_repository
        )


    def get_education_use_case(
        self,
    ) -> GetEducation:

        """
        Build GetEducation use case.
        """

        return GetEducation(
            repository=self.professional_repository
        )


    def remove_education_use_case(
        self,
    ) -> RemoveEducation:

        """
        Build RemoveEducation use case.
        """

        return RemoveEducation(
            repository=self.professional_repository
        )


    def update_education_use_case(
        self,
    ) -> UpdateEducation:

        """
        Build UpdateEducation use case.
        """

        return UpdateEducation(
            repository=self.professional_repository
        )

    # =========================================================================
    # Goal Use Cases
    # =========================================================================

    def add_goal_use_case(
            self,
    ) -> AddGoalUseCase:
        """
        Build AddGoal use case.
        """

        return AddGoalUseCase(
            repository=self.professional_repository
        )

    def get_goals_use_case(
        self,
    ) -> GetGoalsUseCase:

        """
        Build GetGoals use case.
        """

        return GetGoalsUseCase(
            repository=self.professional_repository
        )

    def update_goal_use_case(
        self,
    ) -> UpdateGoalUseCase:

        """
        Build UpdateGoal use case.
        """

        return UpdateGoalUseCase(
            repository=self.professional_repository
        )


    def remove_goal_use_case(
        self,
    ) -> RemoveGoalUseCase:

        """
        Build RemoveGoal use case.
        """

        return RemoveGoalUseCase(
            repository=self.professional_repository
        )

    # =========================================================================
    # Experience Use Cases
    # =========================================================================


    def add_experience_use_case(
        self,
    ) -> AddExperienceUseCase:

        """
        Build AddExperience use case.
        """

        return AddExperienceUseCase(
            repository=self.professional_repository
        )



    def get_experiences_use_case(
        self,
    ) -> GetExperiencesUseCase:

        """
        Build GetExperiences use case.
        """

        return GetExperiencesUseCase(
            repository=self.professional_repository
        )
    def remove_experience_use_case(
        self,
    ) -> RemoveExperience:

        """
        Build RemoveExperience use case.
        """

        return RemoveExperience(
            repository=self.professional_repository
        )



    def update_experience_use_case(
        self,
    ) -> UpdateExperience:

        """
        Build UpdateExperience use case.
        """

        return UpdateExperience(
            repository=self.professional_repository
        )



    # =========================================================================
    # Project Use Cases
    # =========================================================================


    def add_project_use_case(
        self,
    ) -> AddProject:

        """
        Build AddProject use case.
        """

        return AddProject(
            repository=self.professional_repository
        )



    def get_projects_use_case(
        self,
    ) -> GetProjects:

        """
        Build GetProjects use case.
        """

        return GetProjects(
            repository=self.professional_repository
        )
    def update_project_use_case(
        self,
    ) -> UpdateProject:
        """
        Build UpdateProject use case.
        """
        return UpdateProject(
            repository=self.professional_repository
        )


    def remove_project_use_case(
        self,
    ) -> RemoveProject:
        """
        Build RemoveProject use case.
        """
        return RemoveProject(
            repository=self.professional_repository
        )


    # =========================================================================
    # Skill Use Cases
    # =========================================================================


    def add_skill_use_case(
        self,
    ) -> AddSkillUseCase:

        """
        Build AddSkill use case.

        IMPORTANT:

        Do NOT write:

            self.professional_repository()

        because repository is already an object.

        Wrong:

            SQLiteRepository()

        Correct:

            SQLiteRepository
        """


        return AddSkillUseCase(
            repository=self.professional_repository
        )



    def get_skills_use_case(
        self,
    ) -> GetSkillsUseCase:

        """
        Build GetSkills use case.
        """


        return GetSkillsUseCase(
            repository=self.professional_repository
        )

    def update_skill_use_case(
            self,
    ) -> UpdateSkill:
        """
        Build UpdateSkill use case.
        """

        return UpdateSkill(
            repository=self.professional_repository
        )

    def remove_skill_use_case(
            self,
    ) -> RemoveSkillUseCase:
        """
        Build RemoveSkill use case.
        """

        return RemoveSkillUseCase(
            repository=self.professional_repository
        )


    # =========================================================================
    # Timeline Use Cases
    # =========================================================================


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

    def update_timeline_event_use_case(
            self,
    ) -> UpdateTimelineEvent:
        """
        Build UpdateTimelineEvent use case.
        """

        return UpdateTimelineEvent(
            repository=self.professional_repository
        )



# =============================================================================
# Global Container Instance
# =============================================================================

"""
The API imports this object:

from app.bootstrap.container import container

Example:

container.add_skill_use_case()

creates:

AddSkillUseCase(
    SQLiteProfessionalRepository
)

"""


container = Container()