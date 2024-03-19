from sqlalchemy.orm import Session

from app.schemas.user import SchemaUserCreate
from app.models.user import User

def create(db:Session ,user:SchemaUserCreate):
    new_user = User(user)
    db.add(new_user)
    db.commit()
    return db.refresh(new_user)

def find_by_email(db:Session, email:str):
    return db.query(User).filter(User.email == email).first()