"""
Timeline Event ORM Model.
"""

from datetime import datetime

from sqlalchemy import DateTime
from sqlalchemy import ForeignKey
from sqlalchemy import String

from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from app.infrastructure.database.base import Base


class TimelineEventModel(Base):
    """
    SQLAlchemy representation of Professional timeline events.
    """

    __tablename__ = "timeline_events"

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

    event_type: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
    )

    event_date: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        nullable=False,
    )

    description: Mapped[str] = mapped_column(
        String(1000),
        nullable=False,
        default="",
    )

    reference_id: Mapped[str] = mapped_column(
        String(36),
        nullable=False,
        default="",
    )