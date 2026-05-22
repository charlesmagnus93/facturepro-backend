from typing import Optional

from pydantic import BaseModel, EmailStr, Field


class UserCreate(BaseModel):
    phone: str
    password: str = Field(min_length=6, max_length=72)
    full_name: str

    email: Optional[EmailStr] = None


class UserLogin(BaseModel):
    phone: str
    password: str = Field(min_length=6, max_length=72)


class Token(BaseModel):
    access_token: str
    token_type: str
