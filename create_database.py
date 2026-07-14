from app.infrastructure.database.database import engine
from app.infrastructure.database.models import Base

Base.metadata.create_all(bind=engine)

print("Database created successfully.")