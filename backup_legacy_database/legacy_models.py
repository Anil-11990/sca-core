from datetime import datetime
from datetime import date
from sqlalchemy import Date
from sqlalchemy import DateTime
from sqlalchemy import ForeignKey
from sqlalchemy import String
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column


class Base(DeclarativeBase):
    """
    Base class for all SQLAlchemy models.
    """


class ProfessionalModel(Base):
    """
    Database representation of Professional.
    """

    __tablename__ = "professionals"

    id: Mapped[str] = mapped_column(
        String,
        primary_key=True,
    )

    full_name: Mapped[str] = mapped_column(
        String,
        nullable=False,
    )

    primary_goal: Mapped[str] = mapped_column(
        String,
        nullable=False,
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        nullable=False,
    )


class GoalModel(Base):
    """
    Database representation of Goal.
    """

    __tablename__ = "goals"

    id: Mapped[str] = mapped_column(
        String,
        primary_key=True,
    )

    professional_id: Mapped[str] = mapped_column(
        ForeignKey("professionals.id"),
        nullable=False,
    )

    title: Mapped[str] = mapped_column(
        String,
        nullable=False,
    )

    status: Mapped[str] = mapped_column(
        String,
        nullable=False,
    )

class AchievementModel(Base):
    """
    Database representation of Achievement.
    """

    __tablename__ = "achievements"

    id: Mapped[str] = mapped_column(
        String,
        primary_key=True,
    )

    professional_id: Mapped[str] = mapped_column(
        ForeignKey("professionals.id"),
        nullable=False,
    )

    title: Mapped[str] = mapped_column(
        String,
        nullable=False,
    )

    issuer: Mapped[str] = mapped_column(
        String,
        nullable=False,
    )

    achievement_type: Mapped[str] = mapped_column(
        String,
        nullable=False,
    )

    description: Mapped[str] = mapped_column(
        String,
        nullable=False,
        default="",
    )

    credential_url: Mapped[str] = mapped_column(
        String,
        nullable=False,
        default="",
    )

    awarded_at: Mapped[datetime] = mapped_column(
        DateTime,
        nullable=False,
    )
class EducationModel(Base):
    """
    Database representation of Education.
    """

    __tablename__ = "educations"


    id: Mapped[str] = mapped_column(
        String,
        primary_key=True,
    )


    professional_id: Mapped[str] = mapped_column(
        ForeignKey("professionals.id"),
        nullable=False,
    )


    institution: Mapped[str] = mapped_column(
        String,
        nullable=False,
    )


    degree_level: Mapped[str] = mapped_column(
        String,
        nullable=False,
    )


    field_of_study: Mapped[str] = mapped_column(
        String,
        nullable=False,
        default="",
    )


    graduation_status: Mapped[str] = mapped_column(
        String,
        nullable=False,
    )
class ExperienceModel(Base):
    """
    Database representation of Experience.
    """

    __tablename__ = "experiences"

    id: Mapped[str] = mapped_column(
        String,
        primary_key=True,
    )

    professional_id: Mapped[str] = mapped_column(
        ForeignKey("professionals.id"),
        nullable=False,
    )

    company: Mapped[str] = mapped_column(
        String,
        nullable=False,
    )

    role: Mapped[str] = mapped_column(
        String,
        nullable=False,
    )

    description: Mapped[str] = mapped_column(
        String,
        nullable=False,
    )

    employment_type: Mapped[str] = mapped_column(
        String,
        nullable=False,
    )

    start_date: Mapped[date] = mapped_column(
        Date,
        nullable=False,
    )

    end_date: Mapped[date | None] = mapped_column(
        Date,
        nullable=True,
    )
class TimelineEventModel(Base):
    """
    Database representation of TimelineEvent.
    """

    __tablename__ = "timeline_events"

    id: Mapped[str] = mapped_column(
        String,
        primary_key=True,
    )

    professional_id: Mapped[str] = mapped_column(
        ForeignKey("professionals.id"),
        nullable=False,
    )

    title: Mapped[str] = mapped_column(
        String,
        nullable=False,
    )

    event_type: Mapped[str] = mapped_column(
        String,
        nullable=False,
    )

    event_date: Mapped[datetime] = mapped_column(
        DateTime,
        nullable=False,
    )

    description: Mapped[str] = mapped_column(
        String,
        nullable=False,
        default="",
    )

    reference_id: Mapped[str] = mapped_column(
        String,
        nullable=False,
        default="",
    )