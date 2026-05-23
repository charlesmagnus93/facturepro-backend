from sqlalchemy.orm import Session

from app.models.invoice import Invoice
from app.models.invoice_item import InvoiceItem


def create_invoice(db: Session, invoice: Invoice):

    db.add(invoice)
    db.commit()
    db.refresh(invoice)

    return invoice


def create_invoice_item(db: Session, item: InvoiceItem):

    db.add(item)
    db.commit()
    db.refresh(item)

    return item


def get_invoices(db: Session, user_id: int):

    return db.query(Invoice).filter(Invoice.user_id == user_id).all()


def get_invoice_by_id(db: Session, invoice_id: int, user_id: int):

    return (
        db.query(Invoice)
        .filter(Invoice.id == invoice_id, Invoice.user_id == user_id)
        .first()
    )
