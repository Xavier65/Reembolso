from pydantic import BaseModel, ConfigDict
from pydantic.dataclasses import dataclass
from typing import Optional

class MyConfig():
    config_mode = ConfigDict(from_attributes=True)

@dataclass(config=MyConfig)
class SchemaRepayment(BaseModel):
    id:int
    remark:str 
    user_owner_id:int 

class SchemaRepaymentCreate(BaseModel):
    remark:Optional[str] = None 
    user_owner_id:int 