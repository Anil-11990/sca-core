from datetime import datetime

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