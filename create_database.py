from app.infrastructure.database.session import engine
from app.infrastructure.database.base import Base

# Import every model so SQLAlchemy registers them
from app.infrastructure.database.models import *

Base.metadata.create_all(bind=engine)

print("Database created successfully.")