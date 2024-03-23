from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.services import handler_repayment
from app.schemas.repayment import SchemaRepaymentCreate, SchemaRepaymentUpdate
from app.setting.connection import get_db

router = APIRouter(prefix="/repayment", tags=["Router Repayment"])


@router.post("/create")
def create_repayment(repayment: SchemaRepaymentCreate, db: Session = Depends(get_db)):
    db_repayment = handler_repayment.create(db, repayment)
    if not db_repayment is None:
        raise HTTPException(status_code=404, detail="Repayment not created!")
    raise HTTPException(status_code=202, detail="Repayment created!")


@router.get("/find_id/{repayment_id}")
def get_repayment_by_id(repayment_id: int, db: Session = Depends(get_db)):
    db_repayment = handler_repayment.find_by_id(db, repayment_id)
    if db_repayment:
        return db_repayment
    raise HTTPException(status_code=404, detail="Repayment not found!")


@router.get("/find_user/{user_email}")
def get_repayment_by_user(user_email: str, db: Session = Depends(get_db)):
    db_repayment = handler_repayment.find_by_user(db, user_email)
    if db_repayment:
        return db_repayment
    raise HTTPException(status_code=404, detail="Repayment not found!")


@router.put("/update/{repayment_id}")
def update_repayment_by_id(
    repayment_id: int,
    repayment_update: SchemaRepaymentUpdate,
    db: Session = Depends(get_db)
):
    db_repayment = handler_repayment.update(
        db, repayment_id, repayment_update
    )
    if db_repayment:
        return db_repayment
    raise HTTPException(status_code=404, detail="Repayment not found!")


@router.delete("/repayment/{repayment_id}")
def delete_repayment_by_id(repayment_id: int, db: Session = Depends(get_db)):
    return handler_repayment.delete(db, repayment_id)
