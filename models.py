# 📄 models.py

from sqlalchemy import Column, Integer, String, Text, DateTime
from sqlalchemy.sql import func
from db import Base

class Insight(Base):
    __tablename__ = "insights"

    id = Column(Integer, primary_key=True, index=True)
    input_text = Column(Text, nullable=False)
    summary = Column(Text, nullable=False)
    sentiment = Column(String(20), nullable=True)
    tags = Column(Text, nullable=True)  # comma-separated tags
    created_at = Column(DateTime(timezone=True), server_default=func.now())
