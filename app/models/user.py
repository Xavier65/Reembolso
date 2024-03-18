from typing import List

from sqlalchemy import String, Integer, Boolean, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.orm import relationship

from .base import TimeStampBase

class User(TimeStampBase):
    __tablename__ = "user"
    id:Mapped[int] = mapped_column(Integer, primary_key=True)
    username:Mapped[str] = mapped_column(String(30), unique=True)
    password:Mapped[str] = mapped_column(String(40))
    is_active:Mapped[bool] = mapped_column(Boolean, default=True)

    repayment:Mapped[List["Repayment"]] = relationship(back_populates="user")
