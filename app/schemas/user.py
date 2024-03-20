from pydantic import BaseModel
from typing import Optional

class SchemaUser(BaseModel):
    id:int
    first_name:str
    last_name:str
    email:str
    password:str
    is_active:bool

class SchemaUserCreate(BaseModel):
    first_name:Optional[str] = None
    last_name:Optional[str] = None
    email:Optional[str] = None
    password:Optional[str] = None