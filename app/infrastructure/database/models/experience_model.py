"""
Experience ORM Model.
"""

from datetime import date

from sqlalchemy import Date
from sqlalchemy import ForeignKey
from sqlalchemy import String

from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from app.infrastructure.database.base import Base


class ExperienceModel(Base):
    """
    SQLAlchemy representation of Experience.
    """

    __tablename__ = "experiences"

    id: Mapped[str] = mapped_column(
        String(36),
        primary_key=True,
    )

    professional_id: Mapped[str] = mapped_column(
        ForeignKey("professionals.id"),
        nullable=False,
    )

    company: Mapped[str] = mapped_column(
        String(200),
        nullable=False,
    )

    role: Mapped[str] = mapped_column(
        String(200),
        nullable=False,
    )

    description: Mapped[str] = mapped_column(
        String(1000),
        nullable=False,
    )

    employment_type: Mapped[str] = mapped_column(
        String(100),
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