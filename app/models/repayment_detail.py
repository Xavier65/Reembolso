from sqlalchemy import Column, Integer, String, Float
from sqlalchemy import ForeignKey 
from sqlalchemy.orm import relationship

from .base import TimeStampBase
from app.schemas.repayment_detail import RepaymentDetailCreate

class RepaymentDetail(TimeStampBase):
    __tablename__ = "repayment_detail"
    id = Column(Integer, primary_key=True)
    rtn = Column(String(14))
    cai = Column(String(40))
    invoice = Column(String(20))
    conception = Column(String(50))
    amount = Column(Float)
    tax = Column(Float)
    repayment_owner_id = Column(Integer, ForeignKey("repayment.id"))
    repayment_owner = relationship("Repayment", back_populates="repayment_details")

    def __init__(self,repayment_detail:RepaymentDetailCreate):
        self.rtn = repayment_detail.rtn
        self.cai = repayment_detail.cai
        self.invoice = repayment_detail.invoice
        self.conception = repayment_detail.conception
        self.amount = repayment_detail.amount
        self.tax = repayment_detail.tax
        self.repayment_owner_id = repayment_detail.repayment_owner_id