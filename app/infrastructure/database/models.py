"""
SQLAlchemy ORM models.

Database models are kept separate from the Domain Model.

This keeps the Domain independent from SQLAlchemy.
"""

from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from sqlalchemy import String
from sqlalchemy import DateTime


class Base(DeclarativeBase):
    """
    Base class for every ORM model.
    """
    pass


class ProfessionalModel(Base):
    """
    Database representation of a Professional.
    """

    __tablename__ = "professionals"

    id: Mapped[str] = mapped_column(
        String,
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

    created_at: Mapped[DateTime] = mapped_column(
        DateTime,
        nullable=False,
    )