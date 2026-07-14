"""
Database configuration.

Creates the SQLAlchemy Engine used by the application.
"""

from sqlalchemy import create_engine

DATABASE_URL = "sqlite:///sca.db"

engine = create_engine(
    DATABASE_URL,
    echo=False,
)