from pydantic import BaseModel
from typing import Optional

class RepaymentDetail(BaseModel):
    id:int 
    rtn:str 
    cai:str
    invoice:str 
    conception:str
    amount:float
    tax:float
    repayment_owner_id:int 

class RepaymentDetailCreate(BaseModel):
    rtn:Optional[str] = None
    cai:Optional[str] = None
    invoice:Optional[str] = None
    conception:Optional[str] = None
    amount:Optional[float] = 0.0
    tax:Optional[float] = 0.0
    repayment_owner_id:Optional[int] = None