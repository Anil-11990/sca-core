"""
SQLAlchemy Declarative Base.

Every ORM model in SCA inherits from this Base.

Responsibilities
----------------
- Provide the declarative base class.
- Act as the metadata root for Alembic migrations.
"""

from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    """
    Root class for every SQLAlchemy ORM model.
    """

    pass