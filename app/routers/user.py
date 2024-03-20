from fastapi import APIRouter, Depends
from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.setting.connection import get_db
from app.schemas.user import SchemaUserCreate
from app.services import handler_user

router = APIRouter(prefix="/user", tags=["Router User"])

@router.post("/create")
def create_user(user:SchemaUserCreate,db:Session = Depends(get_db)):
    new_user = handler_user.create(db,user)
    if new_user is None:
        raise HTTPException(status_code=202, detail=f"User:{user.first_name} {user.last_name} created!")
    raise HTTPException(status_code=404, detail="User not created!")

@router.get("/find/{user_email}")
def get_user_by_email(user_email:str, db:Session = Depends(get_db)):
    db_user = handler_user.find_by_email(db, user_email)
    if db_user is None:
        return HTTPException(status_code=404, detail="User not found!")
    return db_user