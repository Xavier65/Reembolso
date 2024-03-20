from sqlalchemy.orm import Session

from app.schemas.repayment_detail import RepaymentDetailCreate
from app.models.repayment_detail import RepaymentDetail
from app.models.repayment import Repayment

def create(db:Session, repayment_detail:RepaymentDetailCreate):
    new_repayment_detail = RepaymentDetail(repayment_detail)
    db.add(new_repayment_detail)
    db.commit()
    return db.refresh(new_repayment_detail)

def find(db:Session, repayment_id:int):
    db_repayment = db.query(Repayment).filter(Repayment.id == repayment_id).first()
    return db_repayment.repayment_details