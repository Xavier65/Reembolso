from typing import List

from sqlalchemy import String, Integer, Boolean, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.orm import relationship

from .base import TimeStampBase

class Supplier(TimeStampBase):
    __tablename__ = "supplier"
    id:Mapped[int] = mapped_column(Integer, primary_key=True)
    name:Mapped[str] = mapped_column(String(60), unique=True)