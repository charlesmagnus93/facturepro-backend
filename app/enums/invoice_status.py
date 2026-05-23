from enum import Enum


class InvoiceStatus(str, Enum):
    PENDING = "pending"

    PARTIALLY_PAID = "partially_paid"

    PAID = "paid"

    CANCELLED = "cancelled"

    OVERDUE = "overdue"
