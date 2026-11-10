import os
import logging
from pathlib import Path
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from app.config import DATABASE_URL

logger = logging.getLogger(__name__)

# Fallback to local SQLite if no external PostgreSQL URL is provided
if DATABASE_URL:
    logger.info("Configuring PostgreSQL connection from DATABASE_URL.")
    engine = create_engine(
        DATABASE_URL,
        pool_pre_ping=True,
        pool_recycle=300
    )
else:
    db_file = Path(__file__).resolve().parent.parent.parent / "sahayak.db"
    sqlite_url = f"sqlite:///{db_file}"
    logger.info(f"No DATABASE_URL set. Using persistent local SQLite database: {sqlite_url}")
    engine = create_engine(
        sqlite_url,
        connect_args={"check_same_thread": False}
    )

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    """FastAPI Dependency for database session management."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def init_db():
    """Initializes tables in database."""
    try:
        from app.db import models  # noqa: F401
        Base.metadata.create_all(bind=engine)
        logger.info("Database tables initialized successfully.")
    except Exception as e:
        logger.error(f"Error initializing database: {e}")
