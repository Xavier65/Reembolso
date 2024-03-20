from pydantic import BaseModel, ConfigDict
from pydantic.dataclasses import dataclass
from typing import Optional

from .repayment import SchemaRepayment

class MyConfig():
    config_mode = ConfigDict(from_attributes=True)

@dataclass(config=MyConfig)
class SchemaUser(BaseModel):
    id:int
    first_name:str
    last_name:str
    email:str
    password:str
    is_active:bool

@dataclass(config=MyConfig)
class SchemaUserCreate(BaseModel):
    first_name:Optional[str] = None
    last_name:Optional[str] = None
    email:Optional[str] = None
    password:Optional[str] = None