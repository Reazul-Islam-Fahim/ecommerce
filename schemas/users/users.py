from pydantic import BaseModel, EmailStr
from models import *
from typing import Optional

class UserSchema(BaseModel):
    name: str
    email: EmailStr
    password: str
    phone: str
    dob: str
    gender: str
    isChecked: Optional[bool] = False
    role: Optional[str] = "user"
    
    class Config:
        orm_mode = True
        

class LoginSchema(BaseModel):
    email: EmailStr
    password: str
    
    class Config:
        orm_mode = True