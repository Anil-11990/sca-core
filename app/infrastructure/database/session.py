"""
Database Session Configuration.

Responsibilities
----------------
- Create the SQLAlchemy Engine.
- Create the Session Factory.
- Provide database sessions.
"""

from collections.abc import Generator

from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "sqlite:///sca.db"

engine = create_engine(
    DATABASE_URL,
    echo=False,
    future=True,
)

SessionLocal = sessionmaker(
    bind=engine,
    autoflush=False,
    autocommit=False,
    future=True,
)


def get_session() -> Generator[Session, None, None]:
    """
    Provides a database session.
    """

    session = SessionLocal()

    try:
        yield session

    finally:
        session.close()