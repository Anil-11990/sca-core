"""
SQLite implementation of the Professional Repository.

Responsibilities
----------------
- Persist Professional aggregates.
- Persist Goals.
- Persist Achievements.
- Persist Education.
- Persist Experiences.
- Persist Timeline Events.
- Restore the complete Professional Aggregate.
"""

from uuid import UUID

# ==========================================================
# Domain
# ==========================================================

from app.domain.professional.professional import Professional
from app.domain.common.value_objects.full_name import FullName

from app.domain.goal.goal import Goal
from app.domain.goal.status import GoalStatus
from app.domain.goal.value_objects.goal_title import GoalTitle

from app.domain.achievement.achievement import Achievement
from app.domain.achievement.achievement_type import AchievementType
from app.domain.achievement.value_objects.achievement_title import (
    AchievementTitle,
)
from app.domain.achievement.value_objects.issuer import Issuer

from app.domain.education.education import Education
from app.domain.education.degree_level import DegreeLevel
from app.domain.education.graduation_status import (
    GraduationStatus,
)

from app.domain.experience.experience import Experience

from app.domain.timeline.timeline_event import TimelineEvent
from app.domain.timeline.timeline_event_type import (
    TimelineEventType,
)
from app.domain.experience.value_objects.job_title import (
    JobTitle,
)

from app.domain.experience.value_objects.company_name import (
    CompanyName,
)

from app.domain.experience.value_objects.experience_period import (
    ExperiencePeriod,
)

from app.domain.experience.experience_description import (
    ExperienceDescription,
)

from app.domain.experience.employment_type import (
    EmploymentType,
)

# ==========================================================
# Infrastructure
# ==========================================================

from app.infrastructure.database.models import (
    ProfessionalModel,
    GoalModel,
    AchievementModel,
    EducationModel,
    ExperienceModel,
    TimelineEventModel,
)

from app.infrastructure.database.session import (
    SessionLocal,
)


from app.domain.repositories.professional_repository import (
    ProfessionalRepository,
)

class SQLiteProfessionalRepository(
    ProfessionalRepository,
):
    """
    SQLite implementation of the Professional Repository.
    """

    # ==========================================================
    # Save Aggregate
    # ==========================================================

    def save(
        self,
        professional: Professional,
    ) -> None:
        """
        Saves the complete Professional Aggregate.
        """

        session = SessionLocal()

        # ------------------------------------------------------
        # Professional
        # ------------------------------------------------------

        session.merge(
            ProfessionalModel(
                id=str(professional.id),
                full_name=str(
                    professional.full_name
                ),
                primary_goal=professional.primary_goal,
                created_at=professional.created_at,
            )
        )

        # ------------------------------------------------------
        # Goals
        # ------------------------------------------------------

        for goal in professional.goals:

            session.merge(
                GoalModel(
                    id=str(goal.id),
                    professional_id=str(
                        professional.id
                    ),
                    title=str(goal.title),
                    status=goal.status.value,
                )
            )

        # ------------------------------------------------------
        # Achievements
        # ------------------------------------------------------

        for achievement in professional.achievements:

            session.merge(
                AchievementModel(
                    id=str(
                        achievement.id
                    ),
                    professional_id=str(
                        professional.id
                    ),
                    title=str(
                        achievement.title
                    ),
                    issuer=str(
                        achievement.issuer
                    ),
                    achievement_type=(
                        achievement.achievement_type.value
                    ),
                    description=str(
                        achievement.description
                    ),
                    credential_url=str(
                        achievement.credential_url
                    ),
                    awarded_at=(
                        achievement.awarded_at
                    ),
                )
            )

        # ------------------------------------------------------
        # Education
        # ------------------------------------------------------

        for education in professional.educations:

            session.merge(
                EducationModel(
                    id=str(
                        education.id
                    ),
                    professional_id=str(
                        professional.id
                    ),
                    institution=str(
                        education.institution
                    ),
                    degree_level=(
                        education.degree_level.value
                    ),
                    field_of_study=(
                        education.field_of_study
                    ),
                    graduation_status=(
                        education.graduation_status.value
                    ),
                )
            )

        # ------------------------------------------------------
        # Experiences
        # ------------------------------------------------------

        for experience in professional.experiences:
            session.merge(
                ExperienceModel(
                    id=str(experience.id),
                    professional_id=str(
                        professional.id
                    ),
                    company=str(
                        experience.company_name
                    ),
                    role=str(
                        experience.job_title
                    ),
                    description=str(
                        experience.description
                    ),
                    employment_type=(
                        experience.employment_type.value
                    ),
                    start_date=(
                        experience.experience_period.start_date
                    ),
                    end_date=(
                        experience.experience_period.end_date
                    ),
                )
            )
        # ------------------------------------------------------
        # Timeline
        # ------------------------------------------------------

        for event in professional.timeline:

            session.merge(
                TimelineEventModel(
                    id=str(event.id),
                    professional_id=str(
                        professional.id
                    ),
                    title=str(event.title),
                    event_type=(
                        event.event_type.value
                    ),
                    event_date=(
                        event.event_date.value
                    ),
                    description=str(
                        event.description
                    ),
                    reference_id=(
                        event.reference_id
                    ),
                )
            )

        session.commit()
        session.close()

    # ==========================================================
    # Load Aggregate
    # ==========================================================

    def get_by_id(
        self,
        professional_id: UUID,
    ) -> Professional | None:
        """
        Restores the complete Professional Aggregate.
        """

        session = SessionLocal()

        # ------------------------------------------------------
        # Load Professional
        # ------------------------------------------------------

        model = session.get(
            ProfessionalModel,
            str(professional_id),
        )

        if model is None:
            session.close()
            return None

        professional = Professional(
            full_name=FullName(
                model.full_name
            ),
            primary_goal=model.primary_goal,
            created_at=model.created_at,
        )

        # ------------------------------------------------------
        # Restore Aggregate Identity
        # ------------------------------------------------------

        professional.id = UUID(model.id)

        # ------------------------------------------------------
        # Restore Goals
        # ------------------------------------------------------

        goal_models = (
            session.query(GoalModel)
            .filter_by(
                professional_id=str(
                    professional.id
                )
            )
            .all()
        )

        for goal_model in goal_models:

            goal = Goal(
                title=GoalTitle(
                    goal_model.title
                )
            )

            goal.id = UUID(
                goal_model.id
            )

            goal.status = GoalStatus(
                goal_model.status
            )

            professional.add_goal(
                goal
            )

        # ------------------------------------------------------
        # Restore Achievements
        # ------------------------------------------------------

        achievement_models = (
            session.query(
                AchievementModel
            )
            .filter_by(
                professional_id=str(
                    professional.id
                )
            )
            .all()
        )

        for achievement_model in achievement_models:

            achievement = Achievement(
                title=AchievementTitle(
                    achievement_model.title
                ),
                issuer=Issuer(
                    achievement_model.issuer
                ),
                achievement_type=AchievementType(
                    achievement_model.achievement_type
                ),
                description=achievement_model.description,
                credential_url=achievement_model.credential_url,
                awarded_at=achievement_model.awarded_at,
            )

            achievement.id = UUID(
                achievement_model.id
            )

            professional.add_achievement(
                achievement
            )

        # ------------------------------------------------------
        # Restore Education
        # ------------------------------------------------------

        education_models = (
            session.query(
                EducationModel
            )
            .filter_by(
                professional_id=str(
                    professional.id
                )
            )
            .all()
        )

        for education_model in education_models:

            education = Education(
                institution=education_model.institution,
                degree_level=DegreeLevel(
                    education_model.degree_level
                ),
                field_of_study=education_model.field_of_study,
                graduation_status=GraduationStatus(
                    education_model.graduation_status
                ),
            )

            education.id = UUID(
                education_model.id
            )

            professional.add_education(
                education
            )
        # ------------------------------------------------------
        # Restore Experiences
        # ------------------------------------------------------

        experience_models = (
            session.query(
                ExperienceModel
            )
            .filter_by(
                professional_id=str(
                    professional.id
                )
            )
            .all()
        )

        for experience_model in experience_models:
            experience = Experience(
                job_title=JobTitle(
                    experience_model.role
                ),
                company_name=CompanyName(
                    experience_model.company
                ),
                employment_type=EmploymentType(
                    experience_model.employment_type
                ),
                experience_period=ExperiencePeriod(
                    start_date=experience_model.start_date,
                    end_date=experience_model.end_date,
                ),
                description=ExperienceDescription(
                    experience_model.description
                ),
            )

            experience.id = UUID(
                experience_model.id
            )

            professional.add_experience(
                experience
            )

        # ------------------------------------------------------
        # Restore Timeline
        # ------------------------------------------------------

        timeline_models = (
            session.query(
                TimelineEventModel
            )
            .filter_by(
                professional_id=str(
                    professional.id
                )
            )
            .all()
        )

        for timeline_model in timeline_models:

            event = TimelineEvent(
                title=timeline_model.title,
                event_type=TimelineEventType(
                    timeline_model.event_type
                ),
                event_date=timeline_model.event_date.date(),
                description=timeline_model.description,
                reference_id=timeline_model.reference_id,
            )

            event.id = UUID(
                timeline_model.id
            )

            professional.add_timeline_event(
                event
            )

        # ------------------------------------------------------
        # Finish
        # ------------------------------------------------------

        session.close()

        session.close()
        return professional