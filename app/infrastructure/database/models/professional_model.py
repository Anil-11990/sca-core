"""
Professional ORM Model.
"""

from datetime import datetime

from sqlalchemy import DateTime
from sqlalchemy import String
from sqlalchemy.orm import (
    Mapped,
    mapped_column,
    relationship,
)

from app.infrastructure.database.base import Base


class ProfessionalModel(Base):
    """
    SQLAlchemy representation of Professional.
    """

    __tablename__ = "professionals"

    id: Mapped[str] = mapped_column(
        String(36),
        primary_key=True,
    )

    full_name: Mapped[str] = mapped_column(
        String(200),
        nullable=False,
    )

    primary_goal: Mapped[str] = mapped_column(
        String(500),
        nullable=False,
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        nullable=False,
    )
    goals = relationship(
        "GoalModel",
        cascade="all, delete-orphan",
        back_populates="professional",
    )