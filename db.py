import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from loguru import logger

# Set up logging
logger.add("logs/db.log", rotation="500 KB", level="INFO")

# Load environment variables from `.env` file
load_dotenv()

# Safely read Supabase DB URL
DB_URL = os.getenv("SUPABASE_DB_URL")

# Defensive check in case .env is misconfigured
if not DB_URL:
    logger.critical("❌ Missing SUPABASE_DB_URL in your environment variables.")
    raise ValueError("❌ Missing SUPABASE_DB_URL in your environment variables.")
else:
    logger.info("🔌 Connecting to Supabase PostgreSQL...")

# SQLAlchemy setup
try:
    engine = create_engine(DB_URL)
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    Base = declarative_base()
    logger.success("✅ SQLAlchemy engine created successfully.")
except Exception as e:
    logger.exception("❌ Failed to create SQLAlchemy engine.")
    raise
