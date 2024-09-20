from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Create a SQLite database
DATABASE_URL = 'sqlite:///bookshop.db'

# Create the engine and the declarative base
engine = create_engine(DATABASE_URL)
Base = declarative_base()

# Session setup
SessionLocal = sessionmaker(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
