"""
Education ORM Model.
"""

from sqlalchemy import ForeignKey
from sqlalchemy import String
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from app.infrastructure.database.base import Base


class EducationModel(Base):

    __tablename__ = "educations"

    id: Mapped[str] = mapped_column(
        String(36),
        primary_key=True,
    )

    professional_id: Mapped[str] = mapped_column(
        ForeignKey("professionals.id"),
        nullable=False,
    )

    institution: Mapped[str] = mapped_column(
        String(200),
        nullable=False,
    )

    degree_level: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
    )

    field_of_study: Mapped[str] = mapped_column(
        String(200),
        nullable=False,
        default="",
    )

    graduation_status: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
    )