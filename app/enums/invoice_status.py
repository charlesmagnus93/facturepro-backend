from enum import Enum


class InvoiceStatus(str, Enum):
    PENDING = "pending"

    PAID = "paid"

    CANCELLED = "cancelled"

    OVERDUE = "overdue"
