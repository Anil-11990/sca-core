"""
Skill ORM Model.
"""

from sqlalchemy import ForeignKey
from sqlalchemy import String
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from app.infrastructure.database.base import Base


class SkillModel(Base):
    """
    SQLAlchemy representation of a Professional Skill.
    """

    __tablename__ = "skills"

    id: Mapped[str] = mapped_column(
        String(36),
        primary_key=True,
    )

    professional_id: Mapped[str] = mapped_column(
        String(36),
        ForeignKey("professionals.id"),
        nullable=False,
    )

    name: Mapped[str] = mapped_column(
        String(200),
        nullable=False,
    )