from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.models.repayment import Repayment
from app.models.user import User
from app.schemas.repayment import SchemaRepaymentCreate, SchemaRepaymentUpdate
from app.services import handler_user


def create(db: Session, repayment: SchemaRepaymentCreate):
    new_repayment = Repayment(repayment)
    db.add(new_repayment)
    db.commit()
    return db.refresh(new_repayment)


def find_by_user(db: Session, user_email: str):
    db_user = handler_user.find_by_email(db, user_email)
    return db_user.repayments


def find_by_id(db: Session, repayment_id: int):
    db_repayment = db.query(Repayment).filter(
        Repayment.id == repayment_id).first()
    return db_repayment


def update(
        db: Session,
        repayment_id: int,
        repayment_update: SchemaRepaymentUpdate
):
    db.query(Repayment).filter(Repayment.id == repayment_id).update(
        values=repayment_update.model_dump(exclude_none=True)
    )
    db.commit()
    return find_by_id(db, repayment_id)


def delete(db: Session, repayment_id: int):
    db_repayment = find_by_id(db, repayment_id)
    try:
        db.query(Repayment).filter(Repayment.id == db_repayment.id).delete()
        db.commit()
    except AttributeError:
        raise HTTPException(
            status_code=404, detail=f"Repayment ID:{repayment_id} not found!")
    return HTTPException(status_code=202)
