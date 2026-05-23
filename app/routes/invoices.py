from fastapi import APIRouter, Depends

from fastapi.responses import Response

from sqlalchemy.orm import Session

from app.db.session import get_db

from app.models.user import User

from app.core.dependencies import get_current_user

from app.schemas.invoice import InvoiceCreate, InvoiceResponse, InvoicePayment

from app.services.invoice_service import (
    create_new_invoice,
    list_invoices,
    generate_invoice_pdf_service,
    register_invoice_payment,
)

router = APIRouter(prefix="/invoices", tags=["Invoices"])


@router.post("/", response_model=InvoiceResponse)
def create(
    payload: InvoiceCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):

    return create_new_invoice(db=db, user_id=current_user.id, payload=payload)


@router.get("/", response_model=list[InvoiceResponse])
def get_all(
    db: Session = Depends(get_db), current_user: User = Depends(get_current_user)
):

    return list_invoices(db, current_user.id)


@router.get("/{invoice_id}/pdf")
def download_pdf(
    invoice_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):

    pdf = generate_invoice_pdf_service(db, invoice_id, current_user.id)

    return Response(
        content=pdf,
        media_type="application/pdf",
        headers={"Content-Disposition": f"inline; filename=invoice-{invoice_id}.pdf"},
    )


@router.post("/{invoice_id}/pay")
def pay_invoice(
    invoice_id: int,
    payload: InvoicePayment,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):

    invoice = register_invoice_payment(
        db=db, invoice_id=invoice_id, user_id=current_user.id, amount=payload.amount
    )

    return {
        "message": "Payment registered",
        "invoice_status": invoice.status,
        "amount_paid": invoice.amount_paid,
    }
