from typing import List

from sqlalchemy import String, Integer, Boolean, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.orm import relationship

from app.setting.connection import Base

class User(Base):
    __tablename__ = "user_table"
    id:Mapped[int] = mapped_column(Integer, primary_key=True)
    username:Mapped[str] = mapped_column(String(30))
    password:Mapped[str] = mapped_column(String(40))
    repayment:Mapped[List["Repayment"]] = relationship(back_populates="user")

class Repayment(Base):
    __tablename__ ="repayment_table"
    id:Mapped[int] = mapped_column(Integer, primary_key=True)
    user_id:Mapped[int] = mapped_column(ForeignKey("user_table.id"))
    user:Mapped["User"] = relationship(back_populates="repayment")
