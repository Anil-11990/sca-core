"""
SQLite implementation of the Professional Repository.

Responsibilities
----------------
- Persist Professional aggregates.
- Persist Goals belonging to a Professional.
- Persist Achievements belonging to a Professional.
- Restore the complete Professional aggregate.

Future Extensions
-----------------
- Skills
- Experiences
- Education
- Projects
- Certificates
- Timeline
"""

from uuid import UUID

from app.domain.achievement.achievement import Achievement
from app.domain.achievement.achievement_type import AchievementType
from app.domain.achievement.value_objects.achievement_title import (
    AchievementTitle,
)
from app.domain.achievement.value_objects.issuer import Issuer
from app.domain.common.value_objects.full_name import FullName
from app.domain.goal.goal import Goal
from app.domain.goal.status import GoalStatus
from app.domain.goal.value_objects.goal_title import GoalTitle
from app.domain.professional.professional import Professional

from app.infrastructure.database.models import (
    AchievementModel,
    GoalModel,
    ProfessionalModel,
)
from app.infrastructure.database.session import SessionLocal


class SQLiteProfessionalRepository:
    """
    SQLite implementation of the Professional Repository.
    """

    # ==========================================================
    # Save Aggregate
    # ==========================================================

    def save(self, professional: Professional) -> None:
        """
        Persists a Professional Aggregate.

        Responsibilities
        ----------------
        - Save Professional.
        - Save Goals.
        - Save Achievements.
        """

        session = SessionLocal()

        professional_model = ProfessionalModel(
            id=str(professional.id),
            full_name=str(professional.full_name),
            primary_goal=professional.primary_goal,
            created_at=professional.created_at,
        )

        session.merge(professional_model)

        # ------------------------------------------------------
        # Persist Goals
        # ------------------------------------------------------

        for goal in professional.goals:
            session.merge(
                GoalModel(
                    id=str(goal.id),
                    professional_id=str(professional.id),
                    title=str(goal.title),
                    status=goal.status.value,
                )
            )

        # ------------------------------------------------------
        # Persist Achievements
        # ------------------------------------------------------

        for achievement in professional.achievements:
            session.merge(
                AchievementModel(
                    id=str(achievement.id),
                    professional_id=str(professional.id),
                    title=str(achievement.title),
                    issuer=str(achievement.issuer),
                    achievement_type=achievement.achievement_type.value,
                    description=achievement.description,
                    credential_url=achievement.credential_url,
                    awarded_at=achievement.awarded_at,
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
        Retrieves a Professional Aggregate by ID.
        """

        session = SessionLocal()

        model = session.get(
            ProfessionalModel,
            str(professional_id),
        )

        if model is None:
            session.close()
            return None

        professional = Professional(
            full_name=FullName(model.full_name),
            primary_goal=model.primary_goal,
            created_at=model.created_at,
        )

        # Restore Aggregate Identity
        professional.id = UUID(model.id)

        # ------------------------------------------------------
        # Restore Goals
        # ------------------------------------------------------

        goal_models = (
            session.query(GoalModel)
            .filter_by(
                professional_id=str(professional.id)
            )
            .all()
        )

        for goal_model in goal_models:
            goal = Goal(
                title=GoalTitle(goal_model.title),
            )

            goal.id = UUID(goal_model.id)
            goal.status = GoalStatus(goal_model.status)

            professional.add_goal(goal)

        # ------------------------------------------------------
        # Restore Achievements
        # ------------------------------------------------------

        achievement_models = (
            session.query(AchievementModel)
            .filter_by(
                professional_id=str(professional.id)
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

        session.close()

        return professional