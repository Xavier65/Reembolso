from typing import List

from sqlalchemy import Integer, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.orm import relationship

from .base import TimeStampBase

class Repayment(TimeStampBase):
    __tablename__ ="repayment"
    id:Mapped[int] = mapped_column(Integer, primary_key=True)

    repayment_detail:Mapped[List["ReplaymentDetail"]] = relationship(back_populates="repayment")

    user_id:Mapped[int] = mapped_column(ForeignKey("user.id"))
    user:Mapped["User"] = relationship(back_populates="repayment")