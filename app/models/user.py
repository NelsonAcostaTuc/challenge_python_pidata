from pydantic import BaseModel, EmailStr
from typing import Optional
from bson import ObjectId

class UserBase(BaseModel):
    email: EmailStr
    is_active: bool = True
    is_superuser: bool = False

class UserCreate(UserBase):
    password: str

class UserInDB(UserBase):
    hashed_password: str

class User(UserBase):
    id: Optional[str] = None

    class Config:
        orm_mode = True
        json_encoders = {
            ObjectId: str
        }
