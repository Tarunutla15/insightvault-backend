# 📄 init_db.py

from db import engine
from models import Base
from loguru import logger

logger.add("logs/init_db.log", rotation="500 KB", level="INFO")

try:
    logger.info("🔨 Creating tables...")
    Base.metadata.create_all(bind=engine)
    logger.success("✅ Tables created successfully.")
except Exception as e:
    logger.exception("❌ Failed to create tables")
