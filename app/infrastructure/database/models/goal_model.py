"""
Goal ORM Model.
"""

from sqlalchemy import ForeignKey
from sqlalchemy import String
from sqlalchemy.orm import (
    Mapped,
    mapped_column,
    relationship,
)

from app.infrastructure.database.base import Base


class GoalModel(Base):
    """
    SQLAlchemy representation of Goal.
    """

    __tablename__ = "goals"

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

    status: Mapped[str] = mapped_column(
        String(50),
        nullable=False,
    )
    professional = relationship(
        "ProfessionalModel",
        back_populates="goals",
    )