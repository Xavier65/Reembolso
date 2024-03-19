from sqlalchemy import Column, String, Integer, Boolean
from sqlalchemy.orm import relationship

from .base import TimeStampBase
from .repayment import Repayment
from app.schemas.user import SchemaUserCreate

class User(TimeStampBase):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True)
    first_name = Column(String(25))
    last_name = Column(String(15))
    email = Column(String(50), unique=True)
    password = Column(String(40))
    is_active = Column(Boolean, default=True)

    repayments = relationship("Repayment", back_populates="user_owner")

    def __init__(self,user:SchemaUserCreate):
        self.first_name = user.first_name
        self.last_name = user.last_name
        self.email = user.email
        self.password = self.fake_hashed(user.password)

    def fake_hashed(self, password:str):
        return f"{password}hashed"