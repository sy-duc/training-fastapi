from sqlmodel import SQLModel, Session, create_engine
from core.config import settings

# Create an engine to connect to the database
engine = create_engine(settings.DATABASE_URL, echo=True)

# A function to initialize the tables based on the models
def init_db():
    # Create tables if they do not exist
    SQLModel.metadata.create_all(engine)

def get_session():
    with Session(engine) as session:
        yield session
