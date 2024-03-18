
from sqlalchemy import Integer, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.orm import relationship

from .base import TimeStampBase

class RepaymentDetail(TimeStampBase):
    __tablename__ = "repayment_detail"
    id:Mapped[int] = mapped_column(Integer, primary_key=True)

    supplier_id:Mapped[int] = mapped_column(ForeignKey("supplier.id"))

    repatment_id:Mapped[int] = mapped_column(ForeignKey("repayment.id"))
    repayment:Mapped["Repayment"] = relationship(back_populates="repayment_detial")