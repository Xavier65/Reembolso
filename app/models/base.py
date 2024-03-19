from datetime import datetime
from sqlalchemy import Column, DateTime

from app.setting.connection import Base

class TimeStampBase(Base):
    __abstract__ = True
    created_at = Column(DateTime, default=datetime.now())
    updated_at = Column(DateTime, onupdate=datetime.now())