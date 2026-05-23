from sqlalchemy.orm import Session

from app.models.invoice import Invoice
from app.models.invoice_item import InvoiceItem

from app.repositories.invoice_repository import (
    create_invoice,
    create_invoice_item,
    get_invoices,
)

from app.repositories.client_repository import get_client_by_id


from app.utils.invoice import generate_invoice_number

from app.enums.invoice_status import InvoiceStatus

from app.utils.pdf import generate_invoice_pdf

from app.repositories.invoice_repository import get_invoice_by_id


def create_new_invoice(db: Session, user_id: int, payload):

    client = get_client_by_id(db, payload.client_id, user_id)

    if not client:
        raise Exception("Client not found")

    invoice = Invoice(
        invoice_number=generate_invoice_number(),
        user_id=user_id,
        client_id=payload.client_id,
        status=InvoiceStatus.PENDING,
    )

    invoice = create_invoice(db, invoice)

    total_amount = 0

    for item in payload.items:

        total_price = item.quantity * item.unit_price

        invoice_item = InvoiceItem(
            description=item.description,
            quantity=item.quantity,
            unit_price=item.unit_price,
            total_price=total_price,
            invoice_id=invoice.id,
        )

        create_invoice_item(db, invoice_item)

        total_amount += total_price

    invoice.total_amount = total_amount

    db.commit()
    db.refresh(invoice)

    return invoice


def list_invoices(db: Session, user_id: int):

    return get_invoices(db, user_id)


def generate_invoice_pdf_service(db: Session, invoice_id: int, user_id: int):

    invoice = get_invoice_by_id(db, invoice_id, user_id)

    if not invoice:
        raise Exception("Invoice not found")

    pdf = generate_invoice_pdf(invoice)

    return pdf
