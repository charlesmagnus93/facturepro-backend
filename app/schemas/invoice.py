from typing import List

from pydantic import BaseModel

from app.enums.invoice_status import InvoiceStatus


class InvoiceItemCreate(BaseModel):
    description: str

    quantity: int

    unit_price: float


class InvoiceCreate(BaseModel):
    client_id: int

    items: List[InvoiceItemCreate]


class InvoiceItemResponse(BaseModel):
    id: int

    description: str

    quantity: int

    unit_price: float

    total_price: float

    class Config:
        from_attributes = True


class InvoiceResponse(BaseModel):
    id: int

    invoice_number: str

    total_amount: float

    status: InvoiceStatus

    items: List[InvoiceItemResponse]

    class Config:
        from_attributes = True
