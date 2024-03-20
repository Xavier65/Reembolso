from sqlalchemy.orm import Session

from app.models.repayment import Repayment
from app.models.user import User
from app.schemas.repayment import SchemaRepayment

def create(db:Session, repayment:SchemaRepayment):
    new_repayment = Repayment(repayment)
    db.add(new_repayment)
    db.commit()
    return db.refresh(new_repayment)

def find_by_id(db:Session, repayment_id:int):
    db_repayment = db.query(Repayment).filter(Repayment.id == repayment_id).first()
    return db_repayment

def find_by_user(db:Session, user_email:str):
    db_user = db.query(User).filter(User.email == user_email).first()
    return db_user.repayments
