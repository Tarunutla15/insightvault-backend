# 📄 db.py

import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Load environment variables from `.env` file
load_dotenv()

# Safely read Supabase DB URL
DB_URL = os.getenv("SUPABASE_DB_URL")

# Defensive check in case .env is misconfigured
if not DB_URL:
    raise ValueError("❌ Missing SUPABASE_DB_URL in your environment variables.")

# SQLAlchemy setup
engine = create_engine(DB_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
