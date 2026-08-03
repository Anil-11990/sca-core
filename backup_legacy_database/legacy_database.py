from sqlalchemy import create_engine

from app.infrastructure.database.legacy_models import Base

DATABASE_URL = "sqlite:///sca.db"

engine = create_engine(
    DATABASE_URL,
    echo=False,
)

Base.metadata.create_all(engine)