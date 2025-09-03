# src/db/database.py
from sqlalchemy import create_engine # pyright: ignore[reportMissingImports]
from sqlalchemy.orm import sessionmaker, declarative_base # pyright: ignore[reportMissingImports]
import os

DATABASE_URL = f"postgresql://{os.getenv('POSTGRES_USER')}:{os.getenv('POSTGRES_PASSWORD')}@postgres:5432/{os.getenv('POSTGRES_DB')}"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()