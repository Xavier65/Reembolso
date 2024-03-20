from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.services import handler_repayment_detail
from app.setting.connection import get_db
from app.schemas.repayment_detail import RepaymentDetailCreate

router = APIRouter(prefix="/repaymentdetail",tags=["Router Repayment Detail"])

@router.post("/create")
def create(repayment_detail:RepaymentDetailCreate, db:Session = Depends(get_db)):
    db_repayment_detail = handler_repayment_detail.create(db,repayment_detail)
    if not db_repayment_detail is None:
        raise HTTPException(status_code=202, detail="repayment_detail is created!")
    raise HTTPException(status_code=404 , detail="repayment_detail not created!")

@router.get("/find/{repayment_id}")
def find_by_repayment_id(repayment_id:int, db:Session = Depends(get_db)):
    db_repayment_detail = handler_repayment_detail.find(db, repayment_id)
    if not db_repayment_detail is None:
        return db_repayment_detail
    raise HTTPException(status_code=404 , detail="repayment_detail not found!")
