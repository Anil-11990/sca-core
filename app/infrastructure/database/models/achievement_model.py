"""
Achievement ORM Model.
"""

from datetime import datetime

from sqlalchemy import DateTime
from sqlalchemy import ForeignKey
from sqlalchemy import String
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from app.infrastructure.database.base import Base


class AchievementModel(Base):
    """
    SQLAlchemy representation of Achievement.
    """

    __tablename__ = "achievements"

    id: Mapped[str] = mapped_column(
        String(36),
        primary_key=True,
    )

    professional_id: Mapped[str] = mapped_column(
        ForeignKey("professionals.id"),
        nullable=False,
    )

    title: Mapped[str] = mapped_column(
        String(200),
        nullable=False,
    )

    issuer: Mapped[str] = mapped_column(
        String(200),
        nullable=False,
    )

    achievement_type: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
    )

    description: Mapped[str] = mapped_column(
        String(500),
        nullable=False,
        default="",
    )

    credential_url: Mapped[str] = mapped_column(
        String(500),
        nullable=False,
        default="",
    )

    awarded_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        nullable=False,
    )