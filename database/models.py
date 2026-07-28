from datetime import datetime

from sqlalchemy import Column, DateTime, Integer, String, Text

from database.database import Base


class Translation(Base):
    __tablename__ = "translations"

    id = Column(Integer, primary_key=True, index=True)
    file_name = Column(String(255), nullable=False)
    original_text = Column(Text, nullable=False)
    language = Column(String(50), nullable=False)
    translated_text = Column(Text, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)