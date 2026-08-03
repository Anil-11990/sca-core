from sqlalchemy import Column, ForeignKey, String

from app.infrastructure.database.base import Base


class ProjectModel(Base):
    __tablename__ = "projects"

    id = Column(String, primary_key=True)
    professional_id = Column(
        String,
        ForeignKey("professionals.id"),
        nullable=False,
    )

    name = Column(String, nullable=False)
    description = Column(String)
    repository_url = Column(String)
    live_url = Column(String)
    technologies = Column(String)