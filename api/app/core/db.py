from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.core.config import settings
from app.core.deps import Base

engine = create_engine(settings.DATABASE_URL, echo=True)

SessionLocal = sessionmaker(bind=engine)

Base.metadata.create_all(bind=engine)


def get_session():
    session = SessionLocal()

    try:
        yield session
    finally:
        session.close()
