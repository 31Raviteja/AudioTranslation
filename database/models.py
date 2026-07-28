from datetime import datetime

from sqlalchemy import Column, DateTime, Integer, String

from database.database import Base


class Translation(Base):
    __tablename__ = "translations"

    id = Column(Integer, primary_key=True, index=True)
    file_name = Column(String, nullable=False)
    original_text = Column(String, nullable=False)
    language = Column(String, nullable=False)
    translated_text = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)