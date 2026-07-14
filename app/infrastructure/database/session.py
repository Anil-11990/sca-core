"""
Database Session Factory.
"""

from sqlalchemy.orm import sessionmaker

from app.infrastructure.database.database import engine

SessionLocal = sessionmaker(
    bind=engine,
    autoflush=False,
    autocommit=False,
)