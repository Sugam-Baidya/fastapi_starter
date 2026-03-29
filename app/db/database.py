from sqlmodel import SQLModel, create_engine, Session

from app.core.config import settings

DATABASE_URL = f'postgresql://{settings.postgres_username}:{settings.postgres_password}@{settings.postgres_hostname}:{settings.postgres_port}/{settings.postgres_dbname}'

engine = create_engine(
    DATABASE_URL,
    echo=True  # logs SQL queries (good for debugging)
)

# Create DB tables
def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

# Dependency (for FastAPI routes)
def get_session():
    with Session(engine) as session:
        yield session