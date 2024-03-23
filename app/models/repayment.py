from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship

from .base import TimeStampBase
from app.schemas.repayment import SchemaRepaymentCreate


class Repayment(TimeStampBase):
    __tablename__ = "repayment"
    id = Column(Integer, primary_key=True)
    remark = Column(String(120))

    user_owner_id = Column(Integer, ForeignKey("user.id"))
    user_owner = relationship("User", back_populates="repayments")

    repayment_details = relationship(
        "RepaymentDetail", back_populates="repayment_owner")

    def __init__(self, repayment: SchemaRepaymentCreate):
        self.remark = repayment.remark
        self.user_owner_id = repayment.user_owner_id
