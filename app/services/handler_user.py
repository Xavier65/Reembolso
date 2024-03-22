from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.schemas.user import SchemaUserCreate, SchemaUserUpdate
from app.models.user import User


def create(db: Session, user: SchemaUserCreate):
    new_user = User(user)
    db.add(new_user)
    db.commit()
    return db.refresh(new_user)


def find_by_email(db: Session, email: str):
    return db.query(User).filter(User.email == email).first()


def update_by_email(db: Session, email: str, user: SchemaUserUpdate):
    db_user = find_by_email(db, email)
    try:
        db.query(User).filter(User.id == db_user.id).update(
            values=user.model_dump(exclude_none=True)
        )
        db.commit()
    except AttributeError:
        raise HTTPException(
            status_code=404, detail=f"User:{email} not updated!")
    return db.query(User).filter(User.id == db_user.id).first()


def delete_by_email(db: Session, email: str):
    db_user = find_by_email(db, email)
    try:
        db.query(User).filter(User.id == db_user.id).delete()
        db.commit()
    except AttributeError:
        raise HTTPException(
            status_code=404, detail=f"User:{email} not found!")
    return HTTPException(status_code=202)
