from typing import Optional

from pydantic import BaseModel, EmailStr


class ClientCreate(BaseModel):
    name: str

    phone: Optional[str] = None

    email: Optional[EmailStr] = None

    address: Optional[str] = None


class ClientUpdate(BaseModel):
    name: Optional[str] = None

    phone: Optional[str] = None

    email: Optional[EmailStr] = None

    address: Optional[str] = None


class ClientResponse(BaseModel):
    id: int

    name: str

    phone: Optional[str]

    email: Optional[str]

    address: Optional[str]

    class Config:
        from_attributes = True
