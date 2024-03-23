from pydantic import BaseModel
from typing import Optional


class SchemaRepayment(BaseModel):
    id: int
    remark: str
    user_owner_id: int


class SchemaRepaymentCreate(BaseModel):
    remark: Optional[str] = None
    user_owner_id: int


class SchemaRepaymentUpdate(BaseModel):
    remark: Optional[str] = None
    user_owner_id: Optional[int] = None
