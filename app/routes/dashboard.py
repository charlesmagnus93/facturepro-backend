from fastapi import APIRouter, Depends

from sqlalchemy.orm import Session

from sqlalchemy import func, extract

from app.db.session import get_db

from app.models.invoice import Invoice

from app.models.client import Client

from app.models.user import User

from app.core.dependencies import get_current_user

router = APIRouter(prefix="/dashboard", tags=["Dashboard"])


@router.get("/")
def dashboard(
    db: Session = Depends(get_db), current_user: User = Depends(get_current_user)
):

    clients_count = db.query(Client).filter(Client.user_id == current_user.id).count()

    invoices_count = (
        db.query(Invoice).filter(Invoice.user_id == current_user.id).count()
    )

    total_invoiced = (
        db.query(func.sum(Invoice.total_amount))
        .filter(Invoice.user_id == current_user.id)
        .scalar()
        or 0
    )

    total_paid = (
        db.query(func.sum(Invoice.amount_paid))
        .filter(Invoice.user_id == current_user.id)
        .scalar()
        or 0
    )

    unpaid = total_invoiced - total_paid

    monthly_revenue = (
        db.query(extract("month", Invoice.created_at), func.sum(Invoice.amount_paid))
        .filter(Invoice.user_id == current_user.id)
        .group_by(extract("month", Invoice.created_at))
        .all()
    )

    return {
        "clients": clients_count,
        "invoices": invoices_count,
        "total_invoiced": total_invoiced,
        "total_paid": total_paid,
        "unpaid": unpaid,
        "monthly_revenue": monthly_revenue
    }
