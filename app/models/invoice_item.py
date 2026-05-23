from sqlalchemy import Column, Integer, String, Float, ForeignKey

from sqlalchemy.orm import relationship

from app.db.database import Base


class InvoiceItem(Base):
    __tablename__ = "invoice_items"

    id = Column(Integer, primary_key=True, index=True)

    description = Column(String, nullable=False)

    quantity = Column(Integer, nullable=False)

    unit_price = Column(Float, nullable=False)

    total_price = Column(Float, nullable=False)

    invoice_id = Column(Integer, ForeignKey("invoices.id"), nullable=False)

    invoice = relationship("Invoice", back_populates="items")
