from datetime import datetime

from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey, Enum

from sqlalchemy.orm import relationship

from app.db.database import Base

from app.enums.invoice_status import InvoiceStatus


class Invoice(Base):
    __tablename__ = "invoices"

    id = Column(Integer, primary_key=True, index=True)

    invoice_number = Column(String, unique=True, nullable=False)

    total_amount = Column(Float, default=0)

    status = Column(Enum(InvoiceStatus), default=InvoiceStatus.PENDING, nullable=False)

    created_at = Column(DateTime, default=datetime.utcnow)

    client_id = Column(Integer, ForeignKey("clients.id"), nullable=False)

    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)

    client = relationship("Client")

    owner = relationship("User")

    items = relationship("InvoiceItem", back_populates="invoice", cascade="all, delete")
