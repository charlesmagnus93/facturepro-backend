from fastapi import APIRouter, Depends

from sqlalchemy.orm import Session

from app.db.session import get_db

from app.models.user import User

from app.core.dependencies import get_current_user

from app.schemas.invoice import InvoiceCreate, InvoiceResponse

from app.services.invoice_service import create_new_invoice, list_invoices

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
